#!/bin/bash

rqt &
roslaunch beginner_tutorials turtlemimic.launch &
rostopic pub /turtlesim1/turtle1/cmd_vel geometry_msgs/Twist -r 1 -- '[2.0, 0.0, 0.0]' '[0.0, 0.0, -1.8]' &