#!/usr/bin/env python

import roslib
import rospy
from sensor_msgs.msg import LaserScan

class LaserFixer(object):
	'''
	A node that listens to scan messages from LMS200 and republishes it with some fixes in the header
        See: Navigation Guide
        and https://github.com/smichaud/lidar-snowfall/issues/1
	'''

	def __init__(self):

		rospy.init_node('lms200fix')

		rospy.loginfo("Starting laser fixer node")
		# subscriptions
		rospy.Subscriber("/bad_scan", LaserScan, self._HandleScanMessage)
		self._ScanPublisher = rospy.Publisher("/good_scan", LaserScan, queue_size=5)

	def _HandleScanMessage(self, msg):
	
		#msg.angle_min= -1.57079637051
                #msg.angle_max= 1.57079637051
                msg.angle_increment= 0.0174532923847
                msg.time_increment= 3.70370362361e-05
                msg.scan_time= 0.0133333336562
                msg.range_min= 0.0
                msg.range_max= 81.0
		
		self._ScanPublisher.publish(msg)


if __name__ == '__main__':
	laserFixer = LaserFixer()
	rospy.spin()

