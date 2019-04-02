#! /usr/bin/env python

import rospy
import numpy as np
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

check_range_length = 0

# avoid obstacle
# state
# forward
# avoid
# right


def callback(msg):
    range_front = msg.ranges[350:370]
    range_right = msg.ranges[0:10]
    range_left = msg.ranges[709:719]
    d_left = np.average(range_left)
    d_front = np.average(range_front)
    d_right = np.average(range_right)
    print "Dists at {0}: left-{1} front-{2} right-{3}".format(
        msg.header.stamp, d_left, d_front, d_right)
    if(d_front < 1):
        print "EMERGENCY STOP ENGAGED"
        move.linear.x = 0.1
        move.angular.z = 5
    else:
        if(d_front == d_left == d_right == np.inf):
            move.linear.x = 0.1
            move.angular.z = -5
        else:
            move.linear.x = 0.5
            move.angular.z = 0
    pub.publish(move)


rospy.init_node('topics_quiz_node')
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(1)
move = Twist()  # need to change to match the described type
move.linear.x = 0
move.angular.z = 0
rospy.spin()

# while not rospy.is_shutdown():
