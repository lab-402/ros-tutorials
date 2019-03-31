#! /usr/bin/env python

import rospy
from age_publisher.msg import Age

rospy.init_node('node_getting_older')
print 'init node'
pub = rospy.Publisher('/age_info', Age, queue_size=1)
rate = rospy.Rate(2)
print 'init publisher'
age = Age()  # need to change to match the described type
age.years = 5  # Fill the values of the message
age.months = 10  # Fill the values of the message
age.days = 0
print 'init age'

while not rospy.is_shutdown():
    pub.publish(age)
    print 'publising msg: {0}'.format(age)
    rate.sleep()
