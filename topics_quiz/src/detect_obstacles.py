#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist


def callback(msg):
    print msg.ranges
    count.linear.x = 0.5
    count.angular.z = 0.5
    pub.publish(count)
    rate.sleep()


rospy.init_node('topics_quiz_node')
sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(2)
count = Twist()  # need to change to match the described type
count.linear.x = 0
count.angular.z = 0
rospy.spin()

# while not rospy.is_shutdown():
