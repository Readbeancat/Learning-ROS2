import rclpy
from rclpy.node import Node
from tf2_ros import StaticTransformBroadcaster
from geometry_msgs.msg import TransformStamped
from tf_transformations import quaternion_from_euler
import math

class StaticTFBroadcaster(Node):
    def __init__(self):
        super().__init__('static_tf_broadcaster')
        self.broadcaster_ = StaticTransformBroadcaster(self)
        self.publish_static_tf()
        
    def publish_static_tf(self):
        static_transformStamped = TransformStamped()
        static_transformStamped.header.frame_id = 'base_link'
        static_transformStamped.header.stamp = self.get_clock().now().to_msg()
        static_transformStamped.child_frame_id = 'laser'
        static_transformStamped.transform.translation.x = 0.5
        static_transformStamped.transform.translation.y = 0.3
        static_transformStamped.transform.translation.z = 0.6
        
        # 欧拉角转四元数
        quat = quaternion_from_euler(math.radians(180), 0, 0)

        static_transformStamped.transform.rotation.x = quat[0]
        static_transformStamped.transform.rotation.y = quat[1]
        static_transformStamped.transform.rotation.z = quat[2]
        static_transformStamped.transform.rotation.w = quat[3]

        self.broadcaster_.sendTransform(static_transformStamped)
        self.get_logger().info("发布静态tf成功")
        # 修改为输出 TransformStamped 对象的字符串表示
        self.get_logger().info(str(static_transformStamped))

def main(args=None):
    rclpy.init(args=args)
    node = StaticTFBroadcaster()
    rclpy.spin(node)
    rclpy.shutdown()