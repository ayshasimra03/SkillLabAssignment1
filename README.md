# ROS 2 Assignment 1

## Objective

To create a ROS 2 package using the `ament_python` build type and implement a publisher node and a subscriber node in Python.

The publisher periodically publishes messages on a topic, while the subscriber receives and displays the messages.

Both nodes are configured as executables and can be launched together using a single ROS 2 launch command.

## Package Information

- **Package Name:** assignment1
- **Build Type:** ament_python
- **Programming Language:** Python
- **ROS 2 Distribution:** Humble

## Publisher Node

- **File Name:** pub.py
- **Node Name:** publisher_node
- **Function:** Periodically publishes messages on the `/chatter` topic.
- **Message Type:** std_msgs/msg/String

The publisher sends messages such as:

```text
Hello ROS 2 - Message 0
Hello ROS 2 - Message 1
Hello ROS 2 - Message 2
```

## Subscriber Node

- **File Name:** sub.py
- **Node Name:** subscriber_node
- **Function:** Subscribes to the `/chatter` topic and displays the received messages.
- **Message Type:** std_msgs/msg/String

The subscriber receives and displays the messages published by the publisher node.

## Topic Information

- **Topic Name:** /chatter
- **Message Type:** std_msgs/msg/String
- **Publisher Count:** 1
- **Subscription Count:** 1

## Launch File

- **File Name:** display.launch.py

The launch file starts both the publisher and subscriber nodes together using a single command.

## Package Structure

```text
assignment1/
├── assignment1/
│   ├── __init__.py
│   ├── pub.py
│   └── sub.py
├── launch/
│   └── display.launch.py
├── resource/
│   └── assignment1
├── test/
├── package.xml
├── setup.py
├── setup.cfg
├── README.md
└── .gitignore
```

## Build Instructions

Open a terminal and execute the following commands:

```bash
cd ~/ros2_ws3

source /opt/ros/humble/setup.bash

colcon build --packages-select assignment1

source install/setup.bash
```

## Run the Publisher Node

```bash
ros2 run assignment1 pub
```

## Run the Subscriber Node

```bash
ros2 run assignment1 sub
```

## Launch Both Nodes Together

```bash
ros2 launch assignment1 display.launch.py
```

## Verify Topic Communication

To list the available topics:

```bash
ros2 topic list
```

To check the topic information:

```bash
ros2 topic info /chatter
```

To display the messages published on the topic:

```bash
ros2 topic echo /chatter
```

## Execution Output

The publisher and subscriber nodes were successfully executed using the launch file.

The publisher periodically publishes messages on the `/chatter` topic, and the subscriber receives and displays the same messages.

The topic communication was verified using ROS 2 topic commands.

## Conclusion

The ROS 2 Python package was successfully created using the `ament_python` build type.

The publisher and subscriber nodes communicate through the `/chatter` topic using the `std_msgs/msg/String` message type.

Both nodes were successfully launched together using a single ROS 2 launch command.