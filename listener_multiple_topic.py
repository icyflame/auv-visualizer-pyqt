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

TOPIC_NAME = ["chatter", "chatter1", "depth"]

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

        self.listwidget = []

        for i in TOPIC_NAME:

            self.listwidget.append(QtGui.QListWidget(self))

        # self.listwidget = QtGui.QListWidget(self)
        # self.listwidget2 = QtGui.QListWidget(self)
        # # self.button1 = QtGui.QPushButton("Change Topic", self)
        # self.edit1 = QtGui.QLineEdit(self)

        for i in self.listwidget:

            self.layout.addWidget(i)

        # self.layout.addWidget(self.edit1)
        # self.layout.addWidget(self.button1)

    def listener(self):       

        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber(TOPIC_NAME[0], String, self.buildCallback(0))
        rospy.Subscriber(TOPIC_NAME[1], String, self.buildCallback(1))
        

    def buildCallback(self, topic_index):

        def callback(data=None):

            self.listwidget[topic_index].insertItem(0, str(data.data)) 

        return callback
            
def main():
    
    app = QtGui.QApplication(sys.argv)
    test = Example()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()