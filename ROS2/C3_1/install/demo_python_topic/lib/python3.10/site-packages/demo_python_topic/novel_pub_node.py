import rclpy
import requests
from example_interfaces.msg import String
from rclpy.node import Node
from queue import Queue

class NovelPubNode(Node):

    def __init__(self,node_name):
        super().__init__(node_name)
        self.get_logger().info(f'Node {node_name} has been started')
        self.novels_queue = Queue()
        self.novel_publisher = self.create_publisher(String,'novel',10)
        self.create_timer(5,self.timer_callback)
    

    def timer_callback(self):
        if self.novels_queue.qsize() > 0:
            lines = self.novels_queue.get()
            msg = String()
            msg.data = lines
            self.novel_publisher.publish(msg)
            self.get_logger().info(f"Published novel: {msg.data}")

  
    def download(self,url):
        response = requests.get(url)
        response.encoding = 'utf-8'
        novel = response.text
        self.get_logger().info(f"Downloaded novel: {novel}")
        for line in novel.splitlines():
            self.novels_queue.put(line)
  


def main():
    rclpy.init()
    node = NovelPubNode("novel_pub_node")
    node.download("http://127.0.0.1:8000/novel1.txt")
    rclpy.spin(node)
    rclpy.shutdown()








