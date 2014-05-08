# Dynamic listener

# All the topics will have a single push button associated with them.

# When the push button is pressed, that topic will be shown. When the push button 
# is pressed again then the topic will be hidden.

#!/usr/bin/env python

import rospy
from std_msgs.msg import String

# import sys
# from PyQt4 import QtGui
# from PyQt4.Qt import QColor, QPalette
# from PyQt4.Qwt5 import Qwt

# import thread

import sys

from PyQt4.QtCore import *
from PyQt4.Qt import QColor, QPalette
import PyQt4.QtGui as QtGui
import PyQt4.Qwt5 as Qwt

# global variables

# TOPIC_NAME = ["chatter", "chatter1", "depth", "images"]

TOPIC_NAME = "chatter"

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        self.listener()        
        
    def initUI(self):

        # dial

        dial = Qwt.QwtDial()
        dial.setReadOnly(True)

        dial.setWrapping(False)
        

        dial.setOrigin(135.0)
        dial.setScaleArc(0.0, 270.0)
        dial.setRange(0.0, 240.0)

        dial.setValue(120.0)

        dial.setNeedle(Qwt.QwtDialSimpleNeedle(
            Qwt.QwtDialSimpleNeedle.Arrow,
            True,
            QColor(Qt.red),
            QColor(Qt.gray)))

        self.dial = dial


        # compass

        compass = Qwt.QwtCompass()
        compass.setLineWidth(4)
        # if pos < 3:
        # compass.setFrameShadow(Qwt.QwtCompass.Sunken)
        # else:
        compass.setFrameShadow(Qwt.QwtCompass.Raised)

        compass.setMode(Qwt.QwtCompass.RotateScale)
        rose = Qwt.QwtSimpleCompassRose(1, -1)
        rose.setWidth(0.15)
        compass.setReadOnly(True)
        compass.setRose(rose)

        self.comp = compass

        # knob

        knob = Qwt.QwtKnob(self)
        knob.setRange(0, 20, 0, 1)
        knob.setScaleMaxMajor(10)
        knob.setKnobWidth(50)
        knob.setValue(10)

        self.knob = knob
        
        QtGui.QWidget.__init__(self)

        self.setGeometry(300, 300, 1000, 1000)
        self.setWindowTitle('threads')

        self.layout = QtGui.QHBoxLayout(self)

        self.layout.addWidget(self.knob)
        self.layout.addWidget(self.comp)
        self.layout.addWidget(self.dial)

        # self.connect(self.testButton, QtCore.SIGNAL("released()"), self.test)

        # self.listwidget = []
        # self.pb = []
        # self.activeTabs = []

        # for i in TOPIC_NAME:

        #     self.listwidget.append(QtGui.QListWidget(self))

        #     self.pb.append(QtGui.QPushButton(i, self))

        #     self.activeTabs.append(0)

        # for i, j in enumerate(self.listwidget):

        #     pb = self.pb[i]

        #     self.layout.addWidget(pb)

        #     self.layout.addWidget(j)

        #     j.hide()

        # for num, item in enumerate(self.pb):

        #     item.clicked.connect(self.buildOnClickSlots(num))

    def listener(self):       

        rospy.init_node('listener', anonymous=True)

        rospy.Subscriber(TOPIC_NAME, String, self.callback)

        # for i, j in enumerate(TOPIC_NAME):

        #     rospy.Subscriber(TOPIC_NAME[i], String, self.buildSubscribeCallback(i)) 

    def callback(self, data=None):

        num = int(str(data.data))

        print num

        self.dial.setValue(num)

    # def buildSubscribeCallback(self, topic_index):

    #     def callback(data=None):

    #         self.listwidget[topic_index].insertItem(0, str(data.data)) 

    #     return callback

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
    test = Example()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()