import launch
import launch_ros 


def generate_launch_description():

    action_node_turtlesim_node = launch_ros.actions.Node(
        package='turtlesim',
        executable='turtlesim_node',
        name='turtlesim_node',
        output='screen'
    )

    # turtle_control
    action_node_turtle_control = launch_ros.actions.Node(
        package='demo_cpp_service',
        executable='turtle_control',
        name='turtle_control',
        output='both'
    )

    return launch.LaunchDescription([
        action_node_turtlesim_node,
        action_node_turtle_control

    ])