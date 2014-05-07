#!/usr/bin/env python

import rospy
from std_msgs.msg import String

import sys
from PyQt4 import QtGui

import thread

# global variables

TOPIC_NAME = "chatter"

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()
        self.listener()        
        
    def initUI(self):
        
        QtGui.QWidget.__init__(self)

        self.setGeometry(300, 300, 1000, 1000)
        self.setWindowTitle('threads')

        self.layout = QtGui.QVBoxLayout(self)

        self.listwidget = QtGui.QListWidget(self)

        self.layout.addWidget(self.listwidget)

    def listener(self):
        
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber(TOPIC_NAME, String, self.callback)

    def callback(self, data=None):

        self.listwidget.insertItem(0, str(data.data)) 
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    test = Example()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()

# def callback(data):
#     rospy.loginfo(rospy.get_caller_id()+"I heard %s",data.data)
    
# def listener():

#     # in ROS, nodes are unique named. If two nodes with the same
#     # node are launched, the previous one is kicked off. The 
#     # anonymous=True flag means that rospy will choose a unique
#     # name for our 'listener' node so that multiple listeners can
#     # run simultaenously.
#     rospy.init_node('listener', anonymous=True)

#     rospy.Subscriber("chatter", String, callback)

#     # spin() simply keeps python from exiting until this node is stopped
#     rospy.spin()
        
# if __name__ == '__main__':
#     listener()
