#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def talker():
	pub = rospy.Publisher('chatter', String, queue_size=10)
	
	rospy.init_node('talker', anonymous=True)
	
	r = rospy.Rate(10)
	
	while not rospy.is_shutdown():
		str = "Publisher timestamp: %s" % rospy.get_time() 
		rospy.loginfo(str)
		pub.publish(String(str))
		r.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException: pass