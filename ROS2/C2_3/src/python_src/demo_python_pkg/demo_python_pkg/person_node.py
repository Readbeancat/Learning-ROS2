import rclpy
from rclpy.node import Node


class PersonNode(Node):
    def __init__(self, name_value:str, age_value: int,node_name:str) -> None:
        super().__init__(node_name)
        self.name = name_value
        self.age = age_value

    def eat(self, food:str) -> None:    
        self.get_logger().info(f"{self.name} is eating {food}")


def main():
    rclpy.init()
    person = PersonNode("Zhangsan", 18,"person_node_san")
    person.eat("yuxiangshousi")

    rclpy.spin(person)
    rclpy.shutdown()

