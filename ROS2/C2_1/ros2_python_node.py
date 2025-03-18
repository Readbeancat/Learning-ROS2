import rclpy
from rclpy.node import Node


def main():
    rclpy.init() # Initialize the ROS 2 client library
    node = Node('python_node') # Create a new ROS 2 node
    node.get_logger().info("已启动python节点") # Log a message to the console
    node.get_logger().warn("警告") # Log a warning message to the console
    rclpy.spin(node) # Keep the node running until it's shutdown
    rclpy.shutdown()


if __name__ == '__main__':
    main()
