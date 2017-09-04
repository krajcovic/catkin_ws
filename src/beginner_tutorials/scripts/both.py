#!/usr/bin/env python
# Tohle je blbost, lepsi je to mit oddelene, ten studentik co to psal v tom stejne mel chybu.
import rospy
from std_msgs.msg import String 
msg = String()

def talker():
	pub = rospy.Publisher('chatter_both', String, queue_size=10) 
	r = rospy.Rate(1)
	
	while not rospy.is_shutdown():
		rospy.loginfo(msg)
		pub.publish(msg)
		r.sleep()

def callback(data):
	rospy.loginfo(rospy.get_caller_id()+"I heard %s",data.data)
	global msg
	msg = data

def listener():
	rospy.init_node('listener_talker', anonymous=True)
	rospy.Subscriber("chatter_both", String, callback)
	talker()
	
	rospy.spin()


if __name__ == '__main__':
	listener()
