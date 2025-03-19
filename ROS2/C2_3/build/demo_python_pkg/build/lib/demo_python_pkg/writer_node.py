from demo_python_pkg.person_node import PersonNode
import rclpy

class WriterNode(PersonNode):
    def __init__(self, name_value: str, age_value: int, node_name:str ,book_value: str) -> None:
        super().__init__(name_value, age_value, node_name)
        self.book = book_value

    def write(self) -> None:
        self.get_logger().info(f"{self.name} is writing {self.book}")


def main():
    rclpy.init()
    writer = WriterNode("Zhangsan", 18, "writer","Python")
    writer.eat("apple")
    writer.write()
    rclpy.spin(writer)
    rclpy.shutdown()