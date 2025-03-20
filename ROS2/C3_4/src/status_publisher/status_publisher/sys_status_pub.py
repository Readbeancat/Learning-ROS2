import rclpy
from rclpy.node import Node
from status_interfaces.msg import SystemStatus
import  psutil
import platform

class SysStatusPub(Node):
    def __init__(self,node_name):
        super().__init__(node_name)
        self.pub = self.create_publisher(SystemStatus, 'sys_status', 10)
        self.timer = self.create_timer(1, self.timer_callback)

    def timer_callback(self):
        """"
        
        builtin_interfaces/Time timestamp # time recode
        string host_name 
        float32 cpu_percent
        float32 memory_percent
        float32 memory_total
        float32 memory_available
        float64 net_sent
        float64 net_recv
        
        """
        cpu_percent = psutil.cpu_percent()
        mem = psutil.virtual_memory()
        net_io_counters = psutil.net_io_counters()

        msg = SystemStatus()
        msg.timestamp = self.get_clock().now().to_msg()
        msg.host_name = platform.node()
        msg.cpu_percent = cpu_percent
        msg.memory_percent = mem.percent
        msg.memory_total = mem.total  /1024 / 1024
        msg.memory_available = mem.available  /1024 / 1024
        msg.net_sent = net_io_counters.bytes_sent / 1024 / 1024
        msg.net_recv = net_io_counters.bytes_recv  / 1024 / 1024


        self.get_logger().info(f"Publishing: {str(msg)}")
        self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = SysStatusPub("sys_status_pub")
    rclpy.spin(node)
    rclpy.shutdown()
