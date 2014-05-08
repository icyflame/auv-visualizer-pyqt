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

TOPIC_NAME = "depth"

class Depth(QtGui.QWidget):
    
    def __init__(self):
        super(Depth, self).__init__()
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

        a = QtGui.QLabel("Depth", self)

        a.setStyleSheet("QLabel{ background-color: white; color: black; font-size: 25px; }")

        self.thermo = Qwt.QwtThermo(self)
        self.thermo.setFixedSize(60, 400)
        self.thermo.setRange(0, 100)
        self.thermo.setAlarmLevel(90)
        self.thermo.setAlarmEnabled(True)
        self.thermo.setFillColor(Qt.green)
        self.thermo.setAlarmColor(Qt.red)
        self.thermo.setOrientation(Qt.Vertical, Qwt.QwtThermo.RightScale)
        self.thermo.setValue(50)

        self.layout.addWidget(a)
        self.layout.addWidget(self.thermo)

    def listener(self):       

        rospy.init_node('listener', anonymous=True)

        # for i, j in enumerate(TOPIC_NAME):

        #     rospy.Subscriber(TOPIC_NAME[i], String, self.buildSubscribeCallback(i))

        rospy.Subscriber(TOPIC_NAME, String, self.callback)

    def callback(self, data=None):

        num = int(str(data.data))

        self.thermo.setValue(num)

# def main():
    
#     app = QtGui.QApplication(sys.argv)
#     test = Depth()
#     test.show()
#     app.exec_()


# if __name__ == '__main__':
#     main()        