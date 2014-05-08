#!/usr/bin/env python

import rospy
from std_msgs.msg import String

import sys
from PyQt4 import QtGui

import thread

# global variables

TOPIC_NAME_1 = "chatter"
TOPIC_NAME_2 = "chatter1"

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
        self.listwidget1 = QtGui.QListWidget(self)
        self.listwidget2 = QtGui.QListWidget(self)

        self.layout.addWidget(self.listwidget1)
        self.layout.addWidget(self.listwidget2)

    def listener(self):
        # in ROS, nodes are unique named. If two nodes with the same
        # node are launched, the previous one is kicked off. The 
        # anonymous=True flag means that rospy will choose a unique
        # name for our 'listener' node so that multiple listeners can
        # run simultaenously.
        
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber(TOPIC_NAME_1, String, self.callback1)
        rospy.Subscriber(TOPIC_NAME_2, String, self.callback2)
        # ros.spin()

        # spin() simply keeps python from exiting until this node is stopped

    def on_click(self):

        new_topic = self.edit1.text()

        self.listwidget.addItem(new_topic)

        global TOPIC_NAME

        query = "Do you want to change the topic from " + TOPIC_NAME + " to " + new_topic + " ?"

        QtGui.QMessageBox.question(self, 'Message', query,  QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        TOPIC_NAME = self.edit1.text()



    def callback1(self, data=None):

        # self.lbl1.setText("Heya!")

        self.listwidget1.insertItem(0, str(data.data)) 

    def callback2(self, data=None):

        # self.lbl1.setText("Heya!")

        self.listwidget2.insertItem(0, str(data.data)) 
        
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
