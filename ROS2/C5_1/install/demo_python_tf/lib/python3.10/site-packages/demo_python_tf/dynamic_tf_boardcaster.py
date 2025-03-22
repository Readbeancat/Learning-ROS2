import rclpy
from rclpy.node import Node
from tf2_ros import StaticTransformBroadcaster
from geometry_msgs.msg import TransformStamped
from tf_transformations import quaternion_from_euler
import math

class TFBroadcaster(Node):
    def __init__(self):
        super().__init__('static_tf_broadcaster')
        self.broadcaster_ = StaticTransformBroadcaster(self)
        self.timer_ = self.create_timer(0.01, self.publish_tf)

    def publish_tf(self):
        dy_transformStamped = TransformStamped()
        dy_transformStamped.header.frame_id = 'camer_link'
        dy_transformStamped.child_frame_id = 'bottle_link'
        dy_transformStamped.header.stamp = self.get_clock().now().to_msg()


        dy_transformStamped.transform.translation.x = 0.3
        dy_transformStamped.transform.translation.y = 0.2
        dy_transformStamped.transform.translation.z = 0.5
        
        # 欧拉角转四元数
        quat = quaternion_from_euler(0, 0, 0)

        dy_transformStamped.transform.rotation.x = quat[0]
        dy_transformStamped.transform.rotation.y = quat[1]
        dy_transformStamped.transform.rotation.z = quat[2]
        dy_transformStamped.transform.rotation.w = quat[3]

        self.broadcaster_.sendTransform(dy_transformStamped)
        self.get_logger().info("发布tf成功")
        # 修改为输出 TransformStamped 对象的字符串表示
        self.get_logger().info(str(dy_transformStamped))

def main(args=None):
    rclpy.init(args=args)
    node = TFBroadcaster()
    rclpy.spin(node)
    rclpy.shutdown()