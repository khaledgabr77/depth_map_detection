from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node

def generate_launch_description():
    depth_map_detection_localization_node = Node(
        package='ros2_depth_map_detection_localization_cpp',  
        executable='depth_map_detection_localization',  
        name='depth_map_detection_localization',
        parameters=[
            {'width_': 650, 'height_': 650, 'scale_': 50, 
             'MinDepth': 0.2, 'MaxDepth': 30.0}  # Setup your parameters as needed
        ],
        remappings=[
            ('/scan/points', '/scan/points'),  # The lidar point cloud topic
            ('/yolo/tracking', '/yolo/tracking')  # The YOLOv8 tracking topic
        ]
    )

    yolov8_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare('yolov8_bringup'),
                'launch/yolov8.launch.py'  
            ])
        ]),
        launch_arguments={
            'model': '/home/user/shared_volume/ros2_ws/src/d2dtracker_drone_detector/config/depth_map_drone_detection.pt',  # Adjust path to your YOLOv8 model
            'threshold': '0.5',
            'input_image_topic': '/depth_map',  
            'namespace': 'depth_map',  
            'device': 'cuda:0'
        }.items()
    )

    return LaunchDescription([
        depth_map_detection_localization_node,
        yolov8_launch
    ])
