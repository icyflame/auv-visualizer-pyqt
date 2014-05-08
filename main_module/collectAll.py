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

import sensors, control_panel, depth

# global variables

TOPIC_NAME = ["yaw", "pitch", "roll"]

TOPIC_NAME_DIAL = "dialtopic"

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

        # c = QtGui.QLabel("Visualizer", self)

        self.layout.addWidget(a)
        self.layout.addWidget(b)
        self.layout.addWidget(c)

        # for i in TOPIC_NAME:

        #     # self.listwidget.append(QtGui.QLineEdit(self))

        #     self.listwidget.append(QtGui.QListWidget(self))

        #     self.pb.append(QtGui.QPushButton(i, self))

        #     self.activeTabs.append(0)

        # self.create_dial()

        # hl1 = QtGui.QHBoxLayout(self)
        # hl2 = QtGui.QHBoxLayout(self)

        # vl1 = QtGui.QVBoxLayout(self)
        # vl2 = QtGui.QVBoxLayout(self)

        # vl1.addWidget(self.pb[0])
        # vl1.addWidget(self.listwidget[0])
        # vl1.addWidget(self.pb[1])
        # vl1.addWidget(self.listwidget[1])

        # vl2.addWidget(self.pb[2])
        # vl2.addWidget(self.listwidget[2])
        # vl2.addWidget(self.pb[3])
        # vl2.addWidget(self.listwidget[3])

        # hl1.addLayout(vl1)
        # hl1.addLayout(vl2)

        # hl1.addWidget(self.dial)

        # self.layout.addLayout(hl1)

        # for i, j in enumerate(self.listwidget):

        #     pb = self.pb[i]

        #     self.layout.addWidget(pb)

        #     self.layout.addWidget(j)

        #     j.hide()

        # for num, item in enumerate(self.pb):

        #     item.clicked.connect(self.buildOnClickSlots(num))

    def listener(self):       

        rospy.init_node('listener', anonymous=True)

        # for i, j in enumerate(TOPIC_NAME):

        #     rospy.Subscriber(TOPIC_NAME[i], String, self.buildSubscribeCallback(i)) 

        # rospy.Subscriber(TOPIC_NAME_DIAL, String, self.callbackForDial) 

    # def create_dial(self):

    #     self.dial = Qwt.QwtDial()
    #     self.dial.setReadOnly(True)

    #     self.dial.setWrapping(False)

    #     # understanding the setscale function.

    #     # setScale(maxMajInt, maxMinInt, step)

    #     # maximum major intervals
    #     # maximum minor intervals
    #     # step

    #     # The first argument :- I don't get it

    #     # The third argument :- Step. This is the spacing between two major ticks

    #     # The second argument :- The number of intervals in between two major ticks.

    #     self.dial.setScale(-1, 2, 20)

    #     self.dial.setRange(0.0, 240.0)
    #     self.dial.setOrigin(135.0)
    #     self.dial.setScaleArc(0.0, 270.0)
        

    #     self.dial.setValue(120.0)

    #     self.dial.setNeedle(Qwt.QwtDialSimpleNeedle(
    #         Qwt.QwtDialSimpleNeedle.Arrow,
    #         True,
    #         QColor(Qt.red),
    #         QColor(Qt.gray))) 

    # def callbackForDial(self, data=None):

    #     num = int(str(data.data))

    #     self.dial.setValue(num)

    def buildSubscribeCallback(self, topic_index):

        def callback(data=None):

            self.listwidget[topic_index].insertItem(0, str(data.data)) 

            # self.listwidget[topic_index].setText(str(data.data))

        return callback

    # def buildOnClickSlots(self, button_index):

    #     def on_click():

    #         if(self.activeTabs[button_index]):

    #             self.listwidget[button_index].hide()
    #             self.activeTabs[button_index] = 0

    #         else:

    #             self.listwidget[button_index].show()
    #             self.activeTabs[button_index] = 1

    #     return on_click
            
def main():
    
    app = QtGui.QApplication(sys.argv)
    test = MainWidget()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()