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

TOPIC_NAME_DIAL = "dialtopic"

class ControlPanel(QtGui.QWidget):
    
    def __init__(self):
        super(ControlPanel, self).__init__()
        self.initUI()
        # self.listener()        
        
    def initUI(self):

        # initialise the widget
        
        QtGui.QWidget.__init__(self)

        # self.setGeometry(300, 300, 160, 800)
        # self.setWindowTitle('Visualizer')

        # Initialising all the layouts

        self.layout = QtGui.QVBoxLayout(self)
        v1 = QtGui.QVBoxLayout(self)
        v2 = QtGui.QVBoxLayout(self)
        hl1 = QtGui.QHBoxLayout(self)
        hl2 = QtGui.QHBoxLayout(self)
        hl3 = QtGui.QHBoxLayout(self)
        hl4 = QtGui.QHBoxLayout(self)
        hl5 = QtGui.QHBoxLayout(self)

        ################################

        ######## HEADING ###############

        ################################


        a = QtGui.QLabel("Control Panel", self)
        a.setStyleSheet("QLabel{ background-color: black; color: white; font-size: 25px; }")
        a.setFixedSize(180, 30)

        b = QtGui.QLabel("Heading", self)
        b.setStyleSheet("QLabel{ background-color: black; color: white; font-size: 20px; }")
        b.setFixedSize(180, 25)

        Kp = QtGui.QLabel("Kp", self)
        Kp.setStyleSheet("QLabel{ background-color: white; color: black; font-size: 15px; }")

        Ki = QtGui.QLabel("Ki", self)
        Ki.setStyleSheet("QLabel{ background-color: white; color: black; font-size: 15px; }")

        Kd = QtGui.QLabel("Kd", self)
        Kd.setStyleSheet("QLabel{ background-color: white; color: black; font-size: 15px; }")

        setpt = QtGui.QLabel("Setpoint", self)
        setpt.setStyleSheet("QLabel{ background-color: white; color: black; font-size: 15px; }")

        error = QtGui.QLabel("Error", self)
        error.setStyleSheet("QLabel{ background-color: white; color: black; font-size: 15px; }")

        self.heading_Kple = QtGui.QLineEdit("0.0", self)
        self.heading_Kile = QtGui.QLineEdit("0.0", self)
        self.heading_Kdle = QtGui.QLineEdit("0.0", self)
        self.heading_setptle = QtGui.QLineEdit("0.0", self)
        self.heading_errorle = QtGui.QLineEdit("0.0", self)

        staticLabels = []

        staticLabels.append(Kp)
        staticLabels.append(Ki)
        staticLabels.append(Kd)
        staticLabels.append(setpt)
        staticLabels.append(error)

        for i in staticLabels:

            i.setFixedSize(60, 20)

        dynamicLabels = []

        dynamicLabels.append(self.heading_Kple)
        dynamicLabels.append(self.heading_Kile)
        dynamicLabels.append(self.heading_Kdle)
        dynamicLabels.append(self.heading_setptle)
        dynamicLabels.append(self.heading_errorle)

        for i in dynamicLabels:

            i.setFixedSize(60, 20)

        submitHeading = QtGui.QPushButton("Submit", self)
        submitHeading.setFixedSize(180, 25)
        submitHeading.clicked.connect(self.on_click_heading)

        hl1.addWidget(Kp)
        hl1.addWidget(self.heading_Kple)
        hl2.addWidget(Ki)
        hl2.addWidget(self.heading_Kile)
        hl3.addWidget(Kd)
        hl3.addWidget(self.heading_Kdle)
        hl4.addWidget(setpt)
        hl4.addWidget(self.heading_setptle)
        hl5.addWidget(error)
        hl5.addWidget(self.heading_errorle)

        v1.addWidget(a)
        v1.addWidget(b)
        v1.addLayout(hl1)
        v1.addLayout(hl2)
        v1.addLayout(hl3)
        v1.addLayout(hl4)
        v1.addLayout(hl5)
        v1.addWidget(submitHeading)

        ###############################

        ########## DEPTH ##############

        ###############################


        b = QtGui.QLabel("Depth", self)
        b.setStyleSheet("QLabel{ background-color: black; color: white; font-size: 20px; }")
        b.setFixedSize(180, 25)

        Kp = QtGui.QLabel("Kp", self)
        Kp.setStyleSheet("QLabel{ background-color: white; color: black; font-size: 15px; }")

        Ki = QtGui.QLabel("Ki", self)
        Ki.setStyleSheet("QLabel{ background-color: white; color: black; font-size: 15px; }")

        Kd = QtGui.QLabel("Kd", self)
        Kd.setStyleSheet("QLabel{ background-color: white; color: black; font-size: 15px; }")

        setpt = QtGui.QLabel("Setpoint", self)
        setpt.setStyleSheet("QLabel{ background-color: white; color: black; font-size: 15px; }")

        error = QtGui.QLabel("Error", self)
        error.setStyleSheet("QLabel{ background-color: white; color: black; font-size: 15px; }")

        self.depth_Kple = QtGui.QLineEdit("0.0", self)
        self.depth_Kile = QtGui.QLineEdit("0.0", self)
        self.depth_Kdle = QtGui.QLineEdit("0.0", self)
        self.depth_setptle = QtGui.QLineEdit("0.0", self)
        self.depth_errorle = QtGui.QLineEdit("0.0", self)

        staticLabels = []

        staticLabels.append(Kp)
        staticLabels.append(Ki)
        staticLabels.append(Kd)
        staticLabels.append(setpt)
        staticLabels.append(error)

        for i in staticLabels:

            i.setFixedSize(60, 20)

        dynamicLabels = []

        dynamicLabels.append(self.depth_Kple)  
        dynamicLabels.append(self.depth_Kile)  
        dynamicLabels.append(self.depth_Kdle)  
        dynamicLabels.append(self.depth_setptle)
        dynamicLabels.append(self.depth_errorle)

        for i in dynamicLabels:

            i.setFixedSize(60, 20)

        submitDepth = QtGui.QPushButton("Submit", self)
        submitDepth.setFixedSize(180, 25)
        submitDepth.clicked.connect(self.on_click_depth)

        hl1 = QtGui.QHBoxLayout(self)
        hl2 = QtGui.QHBoxLayout(self)
        hl3 = QtGui.QHBoxLayout(self)
        hl4 = QtGui.QHBoxLayout(self)
        hl5 = QtGui.QHBoxLayout(self)

        hl1.addWidget(Kp)
        hl1.addWidget(self.depth_Kple)
        hl2.addWidget(Ki)
        hl2.addWidget(self.depth_Kile)
        hl3.addWidget(Kd)
        hl3.addWidget(self.depth_Kdle)
        hl4.addWidget(setpt)
        hl4.addWidget(self.depth_setptle)
        hl5.addWidget(error)
        hl5.addWidget(self.depth_errorle)

        v2.addWidget(b)
        v2.addLayout(hl1)
        v2.addLayout(hl2)
        v2.addLayout(hl3)
        v2.addLayout(hl4)
        v2.addLayout(hl5)
        v2.addWidget(submitDepth)

        self.layout.addLayout(v1)
        self.layout.addLayout(v2)

    def listener(self):       

        rospy.init_node('listener', anonymous=True)

        # for i, j in enumerate(TOPIC_NAME):

        #     rospy.Subscriber(TOPIC_NAME[i], String, self.buildSubscribeCallback(i)) 

        # rospy.Subscriber(TOPIC_NAME_DIAL, String, self.callbackForDial) 

    def on_click_heading(self):

        dataEntered = [self.heading_Kple.text(),self.heading_Kile.text(),self.heading_Kdle.text(),self.heading_setptle.text(),self.heading_errorle.text()]

    def on_click_depth(self):

        dataEntered = [self.depth_Kple,self.depth_Kile,self.depth_Kdle,self.depth_setptle,self.depth_errorle,]

    def buildSubscribeCallback(self, topic_index):

        def callback(data=None):

            self.listwidget[topic_index].insertItem(0, str(data.data)) 

            # self.listwidget[topic_index].setText(str(data.data))

        return callback
            
# def main():
    
#     app = QtGui.QApplication(sys.argv)
#     test = ControlPanel()
#     test.show()
#     app.exec_()


# if __name__ == '__main__':
#     main()