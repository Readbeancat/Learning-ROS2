import rclpy
from rclpy.node import Node
from tf2_ros import StaticTransformBroadcaster, TransformListener  # 修改 import 部分
from tf2_ros import Buffer
from geometry_msgs.msg import TransformStamped
from tf_transformations import quaternion_from_euler, euler_from_quaternion
import math

class TFLister(Node):
    def __init__(self):
        super().__init__('static_tf_broadcaster')
        self.buffer_ = Buffer()
        self.listener_ = TransformListener(self.buffer_, self)  # 修改实例化部分
        self.timer_ = self.create_timer(1.0, self.get_transform)

    def get_transform(self):
        try:
            result = self.buffer_.lookup_transform('base_link', 'laser', rclpy.time.Time(seconds=0), rclpy.time.Duration(seconds=1))
            transform_ = result.transform
            self.get_logger().info('translation: x=%f, y=%f, z=%f' % (transform_.translation.x, transform_.translation.y, transform_.translation.z))
            rotation_euler = euler_from_quaternion([transform_.rotation.x, transform_.rotation.y, transform_.rotation.z, transform_.rotation.w])
            self.get_logger().info('rotation: roll=%f, pitch=%f, yaw=%f' % (rotation_euler[0], rotation_euler[1], rotation_euler[2]))
        except Exception as e:
            self.get_logger().info('Failed to get transform: %s' % e)

def main(args=None):
    rclpy.init(args=args)
    node = TFLister()
    rclpy.spin(node)
    rclpy.shutdown()