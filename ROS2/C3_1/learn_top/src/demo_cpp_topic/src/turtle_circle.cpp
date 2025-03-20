#include <rclcpp/rclcpp.hpp>
#include <geometry_msgs/msg/twist.hpp>
#include <turtlesim/msg/pose.hpp>
#include <memory>
#include <chrono>

class TurtleControl : public rclcpp::Node
{
private:
    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
    geometry_msgs::msg::Twist msg_;
    turtlesim::msg::Pose pose_;
    bool pose_received_ = false;

public:
    TurtleControl(const std::string& node_name) : Node(node_name)
    {
        publisher_ = this->create_publisher<geometry_msgs::msg::Twist>("/turtle1/cmd_vel", 10);
        // 修正时间单位
        timer_ = this->create_wall_timer(std::chrono::milliseconds(1000), std::bind(&TurtleControl::timer_callback, this));
    }

    void timer_callback()
    {
        auto msg = geometry_msgs::msg::Twist();
        msg.linear.x = 1.0;
        msg.angular.z = 1.0;
        publisher_->publish(msg);
    }
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<TurtleControl>("turtle_circle");
    rclcpp::spin(node);
    rclcpp::shutdown();

    return 0;
}    