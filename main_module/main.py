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

import sensors, control_panel, depth, plot

# global variables

TOPIC_NAME = ["yaw", "pitch", "roll"]

class MainWidget(QtGui.QWidget):
    
    def __init__(self):
        super(MainWidget, self).__init__()
        self.initUI()
        self.listener()        
        
    def initUI(self):
        
        QtGui.QWidget.__init__(self)

        self.setGeometry(300, 300, 320, 320)
        self.setWindowTitle('Visualizer')

        self.layout = QtGui.QHBoxLayout(self)

        # self.connect(self.testButton, QtCore.SIGNAL("released()"), self.test)

        a = sensors.Sensors()
        b = depth.Depth()
        c = control_panel.ControlPanel()
        d = plot.Plot()

        # c = QtGui.QLabel("Visualizer", self)

        self.vlayout = QtGui.QVBoxLayout(self)

        self.vlayout.addWidget(a)
        self.vlayout.addWidget(d)

        self.layout.addLayout(self.vlayout)
        self.layout.addWidget(b)
        self.layout.addWidget(c)


    def listener(self):       

        rospy.init_node('listener', anonymous=True)

    def buildSubscribeCallback(self, topic_index):

        def callback(data=None):

            self.listwidget[topic_index].insertItem(0, str(data.data)) 

            # self.listwidget[topic_index].setText(str(data.data))

        return callback
            
def main():
    
    app = QtGui.QApplication(sys.argv)
    test = MainWidget()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()