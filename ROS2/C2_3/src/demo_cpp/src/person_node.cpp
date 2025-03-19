#include "rclcpp/rclcpp.hpp"


class PersonNode : public rclcpp::Node
{
private:
    std::string name;
    int age;

public:
    PersonNode(const std::string &node_name, const std::string &name, const int &age) : Node(node_name), age(age)
    {
        this->name = name;
        this->age = age;
    }

    void eat(const std::string &food)
    {
        RCLCPP_INFO(this->get_logger(), "%s ,%d  is eating %s", this->name.c_str(),
        this->age ,food.c_str());
    }

};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<PersonNode>("ros2_cpp_node", "Frank", 25);
    node->eat("DOUFU");
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}