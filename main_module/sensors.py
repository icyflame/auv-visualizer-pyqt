#!/usr/bin/env python

import rospy
from std_msgs.msg import String

import sys
from PyQt4 import QtGui

import sys
from PyQt4.QtCore import *
from PyQt4.Qt import QColor, QPalette
import PyQt4.QtGui as QtGui
import PyQt4.Qwt5 as Qwt

# global variables

TOPIC_NAME = ["yaw", "pitch", "roll"]

class Sensors(QtGui.QWidget):
    
    def __init__(self):
        super(Sensors, self).__init__()
        self.initUI()
        self.listener()        
        
    def initUI(self):

        # initialising the window
        
        QtGui.QWidget.__init__(self)

        # self.setGeometry(300, 300, 160, 1000)
        # self.setWindowTitle('Visualizer')

        # main layout

        self.layout = QtGui.QVBoxLayout(self)

        # Creating the elements in this widget

        a = QtGui.QLabel("Sensor", self)

        a.setStyleSheet("QLabel{ background-color: white; color: black; font-size: 25px; }")

        y = QtGui.QLabel("Yaw", self)

        p = QtGui.QLabel("Pitch", self)

        r = QtGui.QLabel("Roll", self)

        self.yawLabel = QtGui.QLabel("0.0", self)

        self.pitchLabel = QtGui.QLabel("0.0", self)

        self.rollLabel = QtGui.QLabel("0.0", self)

        # grouping the elements together

        self.staticLabels = []
        self.dynamicLabels = []

        self.staticLabels.append(y)
        self.staticLabels.append(p)
        self.staticLabels.append(r)

        self.dynamicLabels.append(self.yawLabel)
        self.dynamicLabels.append(self.pitchLabel)
        self.dynamicLabels.append(self.rollLabel)

        # setting the style sheet of all the elements

        a.setFixedSize(160, 35)

        for i in self.staticLabels:

            i.setStyleSheet("QLabel{ background-color: black; color: white; font-size: 20px; padding-left: 15px; }")
            i.setFixedSize(90, 20)

        for i in self.dynamicLabels:

            i.setStyleSheet("QLabel{ background-color: black; color: white; font-size: 20px; margin-left: 20px; padding-left: 15px }")
            i.setFixedSize(90, 20)

        # adding the elements to the widget

        self.layout.addWidget(a)


        hl1 = QtGui.QHBoxLayout(self)
        hl1.addWidget(y)
        hl1.addWidget(self.yawLabel)

        hl2 = QtGui.QHBoxLayout(self)
        hl2.addWidget(p)
        hl2.addWidget(self.pitchLabel)

        hl3 = QtGui.QHBoxLayout(self)
        hl3.addWidget(r)
        hl3.addWidget(self.rollLabel)

        self.layout.addLayout(hl1)
        self.layout.addLayout(hl2)
        self.layout.addLayout(hl3)

    def listener(self):       

        rospy.init_node('listener', anonymous=True)

        for i, j in enumerate(TOPIC_NAME):

            rospy.Subscriber(TOPIC_NAME[i], String, self.buildSubscribeCallback(i))

    def buildSubscribeCallback(self, topic_index):

        def callback(data=None):

            self.dynamicLabels[topic_index].setText(str(data.data))

        return callback

def main():
    
    app = QtGui.QApplication(sys.argv)
    test = Sensors()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()                