# Dynamic listener

# All the topics will have a single push button associated with them.

# When the push button is pressed, that topic will be shown. When the push button 
# is pressed again then the topic will be hidden.

#!/usr/bin/env python

import rospy
from std_msgs.msg import String

import sys
from PyQt4 import QtGui

import thread

# global variables

TOPIC_NAME = ["chatter", "chatter1", "depth", "images"]

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
        self.pb = []
        self.activeTabs = []

        for i in TOPIC_NAME:

            self.listwidget.append(QtGui.QListWidget(self))

            self.pb.append(QtGui.QPushButton(i, self))

            self.activeTabs.append(0)

        # self.listwidget = QtGui.QListWidget(self)
        # self.listwidget2 = QtGui.QListWidget(self)
        # # self.button1 = QtGui.QPushButton("Change Topic", self)
        # self.edit1 = QtGui.QLineEdit(self)

        for i, j in enumerate(self.listwidget):

            pb = self.pb[i]

            self.layout.addWidget(pb)

            self.layout.addWidget(j)

            j.hide()

        for num, item in enumerate(self.pb):

            item.clicked.connect(self.buildOnClickSlots(num))


        # self.layout.addWidget(self.edit1)
        # self.layout.addWidget(self.button1)

    def listener(self):       

        rospy.init_node('listener', anonymous=True)

        for i, j in enumerate(TOPIC_NAME):

            rospy.Subscriber(TOPIC_NAME[i], String, self.buildSubscribeCallback(i))        

    def buildSubscribeCallback(self, topic_index):

        def callback(data=None):

            self.listwidget[topic_index].insertItem(0, str(data.data)) 

        return callback

    def buildOnClickSlots(self, button_index):

        def on_click():

            if(self.activeTabs[button_index]):

                self.listwidget[button_index].hide()
                self.activeTabs[button_index] = 0

            else:

                self.listwidget[button_index].show()
                self.activeTabs[button_index] = 1

        return on_click
            
def main():
    
    app = QtGui.QApplication(sys.argv)
    test = Example()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()