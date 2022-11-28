cmake_minimum_required(VERSION 3.0.2)
project(covid_bot_teleop)

find_package(catkin REQUIRED COMPONENTS
  rospy
  geometry_msgs
)

catkin_python_setup()

catkin_package(
  CATKIN_DEPENDS rospy geometry_msgs
)
catkin_install_python(PROGRAMS
  nodes/covid_bot_teleop_key
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
