#!/usr/bin/env python

import rospy
from std_msgs.msg import String

import sys
from PyQt4 import QtGui

import sys
from PyQt4.QtCore import *
from PyQt4.Qt import *

import PyQt4.Qwt5 as Qwt

# import pyqtgraph as pg

# global variables

TOPIC_NAME = "plotdata"

# class Plot(QtGui.QWidget):

#     def __init__(self):

#         import os

#         os.system("rqt_plot " + TOPIC_NAME)

class Plot(QtGui.QWidget):
    
    def __init__(self):
        super(Plot, self).__init__()
        self.counter = 0
        self.prev = [0, 0]
        self.initUI()
        self.listener()        
        
    def initUI(self):

        # print "XInitThreads says :- ", x11.XInitThreads()

        # xlib.XInitThreads()

        # initialising the window
        
        QtGui.QWidget.__init__(self)

        # # self.setGeometry(300, 300, 160, 1000)
        # # self.setWindowTitle('Visualizer')

        # # main layout

        self.layout = QtGui.QVBoxLayout(self)

        g = QGraphicsView(self)

        self.scene = QGraphicsScene(0, 0, 500, 500, g)
        # self.scene.setBackgroundBrush(Qt.red)

        # scene.addLine(10, 10, 50, 50)

        g.setScene(self.scene)
        g.show()

        self.layout.addWidget(g)

        # # Creating the elements in this widget

        # a = QtGui.QLabel("Navigation", self)

        # a.setStyleSheet("QLabel{ background-color: white; color: black; font-size: 25px; }")

        # pw = pg.PlotWidget()
        # pw.setLabel('left', 'Value', units='V')
        # pw.setLabel('bottom', 'Time', units='s')
        # pw.setXRange(0, 20)
        # pw.setYRange(0, 100)

        # self.plot = Qwt.QwtPlot(self)
        # self.plot.setCanvasBackground(Qt.white)
        # self.plot.setAxisTitle(Qwt.QwtPlot.xBottom, 'Time')
        # self.plot.setAxisScale(Qwt.QwtPlot.xBottom, 0, 50, 1)
        # self.plot.setAxisTitle(Qwt.QwtPlot.yLeft, 'Temperature')
        # self.plot.setAxisScale(Qwt.QwtPlot.yLeft, 0, 250, 40)
        # self.plot.replot()
        
        # self.curve = Qwt.QwtPlotCurve('')
        # self.curve.setRenderHint(Qwt.QwtPlotItem.RenderAntialiased)
        # pen = QPen(QColor('limegreen'))
        # pen.setWidth(2)
        # self.curve.setPen(pen)
        # self.curve.attach(self.plot)

        # self.layout.addWidget(a)
        # self.layout.addWidget(pw)

    def listener(self):       

        rospy.init_node('listener', anonymous=True)

        rospy.Subscriber(TOPIC_NAME, String, self.callback)

    def callback(self, data):

        dataY = int(str(data.data))

        dataX = self.counter

        self.counter += 30

        now = [dataX, dataY]

        print now

        self.scene.addLine(self.prev[0], self.prev[1], now[0], now[1])

        self.prev = [dataX, dataY]

        # self.xData.append(self.counter + 1)
        # self.yData.append(int(str(data.data)))
        # self.counter += 1

        # self.curve.setData(self.xData, self.yData)
        # self.plot.replot()

        # m = Qwt.QwtPlotMarker()
        # m.setSymbol( Qwt.QwtSymbol.Diamond )
        # m.setValue(QPointF(self.counter, int(str(data.data))))
        # m.attach(self.plot)

        # QwtPlotMarker* m = new QwtPlotMarker();
        # m->setSymbol( QwtSymbol( QwtSymbol::Diamond, Qt::red, Qt::NoPen, QSize( 10, 10 ) ) );
        # m->setValue( QPointF( 1.5, 2.2 ) );
        # m->attach( plot );

# def main():
    
#     app = QtGui.QApplication(sys.argv)
#     test = Plot()
#     test.show()
#     app.exec_()


# if __name__ == '__main__':
#     main()                