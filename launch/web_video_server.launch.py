import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def get_env_value(key):
    result = ''
    # check environment param
    if key in os.environ.keys():
        # if environment param name has ROBOT_NAME
        env_value = os.environ[key]
        if env_value != None:
        # set namespace with ROBOT_NAME
            result = env_value
    return result

def find_robot_name():
    env_robot_name = get_env_value('ROBOT_NAME')
    robot_name = LaunchConfiguration('robot_name', default=env_robot_name)
    return robot_name

def find_video_port():
    env_video_port = get_env_value('VIDEO_PORT')
    if env_video_port == '':
        env_video_port = 18888
    video_port = LaunchConfiguration('video_port', default=env_video_port)
    return video_port

def generate_launch_description():
    # Get namespace in argument
    namespace = find_robot_name()
    video_port = find_video_port()
    
    return LaunchDescription([
        Node(
            package='web_video_server', node_executable='web_video_server',
            parameters=[{
                'port': video_port
            }],
            node_namespace=namespace,
            output='screen'
        )
    ])
