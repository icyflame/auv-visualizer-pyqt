# Multiple Topic listener
#
# Add the topics that you want to listen to in the TOPIC_NAME list that is present
# at the top of this file. Once added, the widgets will be placed horizontally.
#
# The placing of the widgets can be changed dynamically depending on the requirements
# of the user and the number of topics being shown.

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

        self.layout = QtGui.QHBoxLayout(self)

        # self.connect(self.testButton, QtCore.SIGNAL("released()"), self.test)

        self.listwidget = []

        for i in TOPIC_NAME:

            self.listwidget.append(QtGui.QListWidget(self))

        # self.listwidget = QtGui.QListWidget(self)
        # self.listwidget2 = QtGui.QListWidget(self)
        # # self.button1 = QtGui.QPushButton("Change Topic", self)
        # self.edit1 = QtGui.QLineEdit(self)

        for i, j in enumerate(self.listwidget):

            label = QtGui.QLabel(TOPIC_NAME[i], self)

            self.layout.addWidget(label)

            self.layout.addWidget(j)


        # self.layout.addWidget(self.edit1)
        # self.layout.addWidget(self.button1)

    def listener(self):       

        rospy.init_node('listener', anonymous=True)

        for i, j in enumerate(TOPIC_NAME):

            rospy.Subscriber(TOPIC_NAME[i], String, self.buildCallback(i))        

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