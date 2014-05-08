# Depth Needle

# Depending on the data that is coming in the needle will be set to the
# depth.

#!/usr/bin/env python

import rospy
from std_msgs.msg import String

import sys
from PyQt4.QtCore import *
from PyQt4.Qt import QColor, QPalette
import PyQt4.QtGui as QtGui
import PyQt4.Qwt5 as Qwt

TOPIC_NAME = "chatter"

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
        self.listener()        
        
    def initUI(self):

        QtGui.QWidget.__init__(self)

        self.setGeometry(300, 300, 1000, 1000)
        self.setWindowTitle('threads')

        self.layout = QtGui.QHBoxLayout(self)

        # dial

        self.dial = Qwt.QwtDial()
        self.dial.setReadOnly(True)

        self.dial.setWrapping(False)

        # understanding the setscale function.

        # setScale(maxMajInt, maxMinInt, step)

        # maximum major intervals
        # maximum minor intervals
        # step

        # The first argument :- I don't get it

        # The third argument :- Step. This is the spacing between two major ticks

        # The second argument :- The number of intervals in between two major ticks.

        self.dial.setScale(-1, 2, 20)



        self.dial.setRange(0.0, 240.0)
        self.dial.setOrigin(135.0)
        self.dial.setScaleArc(0.0, 270.0)
        

        self.dial.setValue(120.0)

        self.dial.setNeedle(Qwt.QwtDialSimpleNeedle(
            Qwt.QwtDialSimpleNeedle.Arrow,
            True,
            QColor(Qt.red),
            QColor(Qt.gray)))

        self.layout.addWidget(self.dial)

    def listener(self):       

        rospy.init_node('listener', anonymous=True)

        rospy.Subscriber(TOPIC_NAME, String, self.callback)

    def callback(self, data=None):

        num = int(str(data.data))

        print num

        self.dial.setValue(num)

def main():
    
    app = QtGui.QApplication(sys.argv)
    test = Example()
    test.show()
    app.exec_()


if __name__ == '__main__':
    main()