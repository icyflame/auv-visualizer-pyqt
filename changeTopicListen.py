# Topic Listener

# A Line Edit at the top of the window, list item forming the main part of the
# window. In case the user needs to change the topic, then he/she can enter the
# topic in the line edit and then press change "topic". A confirmation dialog will pop up.


#!/usr/bin/env python

import rospy
from std_msgs.msg import String

import sys
from PyQt4 import QtGui

import thread

# global variables

TOPIC_NAME = ["chatter", "chatter1"]

active_topic = 0

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()

        # thread.start_new_thread(self.initUI, ())

        # try:
        #     thread.start_new_thread(self.initUI, (self)) #, ("Thread-1", 2, ) )
        #     # thread.start_new_thread(self.listener)
        # except:
        #     print "Error: unable to start thread"
        self.initUI()
        self.listener()        
        
    def initUI(self):
        
        QtGui.QWidget.__init__(self)

        self.setGeometry(300, 300, 1000, 1000)
        self.setWindowTitle('threads')

        self.layout = QtGui.QVBoxLayout(self)

        # self.connect(self.testButton, QtCore.SIGNAL("released()"), self.test)
        self.listwidget = QtGui.QListWidget(self)
        self.button1 = QtGui.QPushButton("Change Topic", self)
        self.edit1 = QtGui.QLineEdit(self)

        self.button1.clicked.connect(self.on_click)

        self.layout.addWidget(self.edit1)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.listwidget)

    def listener(self):       

        rospy.init_node('listener', anonymous=True)
        print self.buildCallback(0)
        rospy.Subscriber(TOPIC_NAME[0], String, self.buildCallback(0))
        rospy.Subscriber(TOPIC_NAME[1], String, self.buildCallback(1))
        # ros.spin()

        # spin() simply keeps python from exiting until this node is stopped

    def buildCallback(self, topic_index):

        def callback(data=None):

            self.listwidget.insertItem(0, str(data.data)) 

        return callback
            
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
