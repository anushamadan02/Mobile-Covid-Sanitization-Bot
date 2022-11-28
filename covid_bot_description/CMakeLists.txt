cmake_minimum_required(VERSION 3.0.2)
project(covid_bot_description)

find_package(catkin REQUIRED COMPONENTS
  urdf
  xacro
)
catkin_package(
  LIBRARIES covid_bot_description
  CATKIN_DEPENDS urdf xacro
)

include_directories( ${catkin_INCLUDE_DIRS} )

install(DIRECTORY meshes rviz urdf
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
