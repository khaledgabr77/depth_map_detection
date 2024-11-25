# ROS2 Depth Map Detection and Localization Package
Using PCL to Convert Point Cloud Data into a Depth Map for Object Detection and Localization

## Description

This ROS2 package provides a robust solution for converting point cloud data into depth maps, integrating advanced detection capabilities with YOLO to detect objects within the depth map. The package generates two types of depth maps: one representing the original scene and another highlighting the depths of detected objects. Additionally, it publishes pose data (x,y,z) for detected objects, aiding in accurate object localization in 3D space.

---

## Table of Contents
1. [Demonstration](#demonstration)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Node](#node)
6. [Contributing](#contributing)

---
## Demonstration

### Depth Map Detection and Localization in in Action


<p align="center">
</p>

<p align="center">
  <img src="images/1.png" alt="Depth Map Detection 1" width="500"/>
  <img src="images/2.png" alt="Depth Map representing highlighting the depths of detected objects 2" width="500"/>
</p>

<p align="center">
  <img src="images/3.gif" alt="Depth Map representing highlighting the depths of detected objects and pose gif" width="500"/>
</p>

---

## Features

- **Original Depth Map Generation**: Converts the lidar point clouds to depth maps representing the entire scene.
- **Object-specific Depth Map**: Isolates and enhances depth data specifically for detected objects, based on YOLOv8 outputs.
- **3D Position Estimation**: Calculates and publishes the average pose of detected objects based on depth data.
- **Detected Object Point Cloud Streaming**: Publishes the points within bounding boxes (BB) as distinct point clouds for each detected object.
- **Multi-Object Detection and Localization**: Simultaneously detects and estimates positions for multiple detected objects in real-time.
- **ROS2 Integration**: Fully compatible with ROS2 for seamless integration in robotics applications.
---

## Installation

### Prerequisites
- **ROS2 Humble**: Ensure you have ROS2 Humble installed on your machine. [Installation Guide](https://docs.ros.org/en/humble/Installation.html)
- **yolovX_ros**: Follow the instructions to set up YOLOvX in ROS2 for object detection. [Installation Guide](https://github.com/mgonzs13/yolov8_ros)
- **C++ compiler (GCC 8 or newer).**
- **PCL (Point Cloud Library), OpenCV, and other ROS2 dependencies.**

### Install Dependencies:
Install the necessary dependencies using the following command:
```bash
sudo apt-get update
sudo apt-get install libpcl-dev libopencv-dev
```
### Clone the Repository
```bash
cd ~/ros2_ws/src
git clone https://github.com/AbdullahGM1/ros2_depth_map_detection_localization_cpp.git
```
### Build the Package:
Navigate back to your ROS2 workspace root and use ``colcon`` to build the package:
```bash
cd ~/ros2_ws
colcon build --packages-select ros2_depth_map_detection_localization_cpp
```
### Source the setup files:
To make the ROS2 package available in your environment, source the setup file::
```bash
source install/setup.bash
```
---

## Usage

### Modifying the Launch File
Before running the package, make sure to modify the `launch` files located in the `ros2_depth_map_detection_localization_cpp/launch` directory to match your setup:

1. **Set the Depth Map Parameters**: Set the `width`, `height`, and the `scale` values of the depth map.
   Example:
```python
 'width': 650, 'height': 650, 'scale': 50, 
```
2. **Set the max and mini frames**: Set the maximum and minimum for the point cloud range. `x-axis` is the depth axis.  
   Example:
```python
'min_depth': 0.2, 'max_depth': 30.0
```
3. **Set the Topic Names**: Set the `topics` names the node needs to generate the depth map and estimate the object pose. 
   Example:
```python
remappings=[
            ('/scan/points', '/change/it/to/your/topic'),  # The lidar point cloud topic
            ('/yolo/tracking', '/change/it/to/your/topic')  # The YOLOv8 tracking topic
```
4. **Set the Yolo Parameters**: Set the `yolo_ros` package arguments for the `model`, and `threshold`. Don't change the `input_image_topic` 
   Example:
```python
        launch_arguments={
            'model': '/home/user/shared_volume/ros2_ws/src/d2dtracker_drone_detector/config/yolo11s.pt',
            'threshold': '0.5',
            'input_image_topic': '/depth_map', 
            'device': 'cuda:0'
        }.items()
```
### Build the Package
After modifying the `launch` file, build your package:
```bash
cd ~/ros2_ws
colcon build --packages-select ros2_depth_map_detection_localization_cpp
```
### Source the Workspace
Before running the package, ensure you source the workspace to have access to the built packages:

For **Bash**:
```bash
source ~/ros2_ws/install/setup.bash
```

### Run the Node
To run the package:
```bash
ros2 launch ros2_depth_map_detection_localization_cpp depth_map_detection_localization_yolo.launch.py
```
---
## Contributing

Feel free to contribute to this project by creating pull requests or opening issues.
