cmake_minimum_required(VERSION 2.8.3)
project(flatland_demo)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  flatland_msgs
  flatland_server
  flatland_plugins
  message_generation
  pluginlib
  std_msgs
)


catkin_package(
  INCLUDE_DIRS include
  # LIBRARIES flatland_lib
  CATKIN_DEPENDS pluginlib roscpp flatland_server
)

include_directories(
  include
  ${catkin_INCLUDE_DIRS}
  ${YAML_CPP_INCLUDE_DIRS}
)

# add_library(flatland_lib
# )

# add_dependencies(flatland_lib ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS} flatland_plugins)
# target_link_libraries(flatland_lib
#   ${catkin_LIBRARIES}
#   yaml-cpp
# )


# Mark executables and/or libraries for installation
# install(TARGETS flatland_lib
#   ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#   LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#   RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

# Mark cpp header files for installation
install(DIRECTORY include/${PROJECT_NAME}/
  DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
  FILES_MATCHING PATTERN "*.hpp"
)

# Install plugins file
install(FILES flatland_plugins.xml
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
