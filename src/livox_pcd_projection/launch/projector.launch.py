from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    config = os.path.join(get_package_share_directory('livox_pcd_projection'),
        'config',
        'projector.yaml'
    )

    return LaunchDescription([
        Node(
            package='livox_pcd_projection',
            executable='projector',
            name='projector',
            parameters = [config]
        ),
    ])
