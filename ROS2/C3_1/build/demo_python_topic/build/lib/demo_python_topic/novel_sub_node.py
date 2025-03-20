import espeakng
import threading
import rclpy
import requests
from queue import Queue
from example_interfaces.msg import String
from rclpy.node import Node
import time


class NovelSubNode(Node):

    def __init__(self,node_name):
        super().__init__(node_name)
        self.get_logger().info(f'Node {node_name} has been started')
        self.novels_queue = Queue()
        self.novel_subscriber = self.create_subscription(String,'novel',self.novel_callback,10)
        self.speak_thread = threading.Thread(target=self.speakkkk)
        self.speak_thread.start()


    def novel_callback(self,msg):
        self.novels_queue.put(msg.data)
        self.get_logger().info(f"Received novel: {msg.data}")

    def speakkkk(self):
        speaker = espeakng.Speaker()
        speaker.voice = 'zh'

        while rclpy.ok():
            if self.novels_queue.qsize() > 0:
                lines = self.novels_queue.get()
                self.get_logger().info(f"Speaking novel: {lines}")
                speaker.say(lines)
                speaker.wait()
            else:
                time.sleep(1)

def main():
    rclpy.init()
    node = NovelSubNode("novel_sub_node")
    rclpy.spin(node)
    rclpy.shutdown()