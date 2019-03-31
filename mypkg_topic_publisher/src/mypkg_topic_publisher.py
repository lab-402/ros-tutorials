#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('move_cmder')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
rate = rospy.Rate(2)
count = Twist()  # need to change to match the described type
count.linear.x = 0
count.angular.z = 0

while not rospy.is_shutdown():
    pub.publish(count)
    count.linear.x = 0.5
    count.angular.z = 0.5
    rate.sleep()
