#! /usr/bin/env python

import rospy
from nav_msgs.msg import Odometry


def callback(msg):
    print msg.pose
    print msg.twist


rospy.init_node('odometry_printer')
sub = rospy.Subscriber('/odom', Odometry, callback)
rospy.spin()
