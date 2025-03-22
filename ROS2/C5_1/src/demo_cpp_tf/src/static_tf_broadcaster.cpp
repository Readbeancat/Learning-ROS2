#include <rclcpp/rclcpp.hpp>
#include <geometry_msgs/msg/transform_stamped.hpp>
#include <tf2_ros/static_transform_broadcaster.h>
#include <tf2/LinearMath/Quaternion.h>
#include <tf2_geometry_msgs/tf2_geometry_msgs.h>

class StaticTfBroadcaster : public rclcpp::Node
{
private:
    std::shared_ptr<tf2_ros::StaticTransformBroadcaster> static_broadcaster;

public:
    StaticTfBroadcaster() : Node("static_tf_broadcaster")
    {
        this->static_broadcaster = std::make_shared<tf2_ros::StaticTransformBroadcaster>(this);
        this->publish();
    }

    void publish()
    {
        geometry_msgs::msg::TransformStamped transformStamped;
        transformStamped.header.stamp = this->get_clock()->now();
        transformStamped.header.frame_id = "map";
        transformStamped.child_frame_id = "target_point";
        transformStamped.transform.translation.x = 5.0;
        transformStamped.transform.translation.y = 3.0;
        transformStamped.transform.translation.z = 0.0;

        tf2::Quaternion q;
        q.setRPY(0, 0, 60 * M_PI / 180);

        // 手动设置 geometry_msgs::msg::Quaternion 的成员
        transformStamped.transform.rotation.x = q.x();
        transformStamped.transform.rotation.y = q.y();
        transformStamped.transform.rotation.z = q.z();
        transformStamped.transform.rotation.w = q.w();

        this->static_broadcaster->sendTransform(transformStamped);
    }
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<StaticTfBroadcaster>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}