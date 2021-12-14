cmake_minimum_required(VERSION 3.0.2)
project(Avoider)


find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  message_generation
  rospy
  sensor_msgs
)

catkin_package(
  CATKIN_DEPENDS geometry_msgs rospy sensor_msgs
)
