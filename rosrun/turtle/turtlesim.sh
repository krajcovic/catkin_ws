#!/bin/bash

rosparam load param_last.yamp last

rosrun rqt_console rqt_console &
rosrun rqt_logger_level rqt_logger_level &
rosrun rqt_graph rqt_graph &
rosrun rqt_plot rqt_plot &

rosrun turtlesim turtlesim_node __name:=turtle_sim_1 &
x-terminal-emulator -e rosrun turtlesim turtle_teleop_key __name:=turtle_control &

#x-terminal-emulator -e rostopic echo /turtle1/cmd_vel &
# provede pouze jednou
#rostopic pub -1 /turtle1/cmd_vel geometry_msgs/Twist -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, 1.8]'

# provadi opakovane s frekvenci 1 khz
rostopic pub /turtle1/cmd_vel geometry_msgs/Twist -r 1 -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, 1.8]'
rosservice call /spawn 2 2 0.2 ""