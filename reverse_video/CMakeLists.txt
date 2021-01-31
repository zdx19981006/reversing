cmake_minimum_required(VERSION 3.0.2)
project(reverse_video)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)

## Generate messages in the 'msg' folder
add_message_files(
   FILES
   control_message.msg
 )

generate_messages(
   DEPENDENCIES
   std_msgs
)

catkin_package(
    CATKIN_DEPENDS message_runtime
)

catkin_install_python(
	PROGRAMS scripts/user.py
	scripts/main.py
	scripts/Reverse.py
	scripts/Straight.py
	DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

