#!/usr/bin/env python
# license removed for brevity
import rospy
import time
from std_msgs.msg import String
import random

ch = random.choice
h = range(2, 239, 1)

TOPIC_NAME = raw_input("Enter the topic name to publish to :- ")

def talker():
    pub = rospy.Publisher(TOPIC_NAME, String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    r = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        time.sleep(1.1)
        g = ch(h)
        string = str(g)
        rospy.loginfo(string)
        pub.publish(string)
        r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
