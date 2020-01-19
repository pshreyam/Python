import pyqtgraph as pg
import pyqtgraph.exporters
import numpy as np

# define the data
theTitle = "pyqtgraph plot"
y = [2,4,6,8,10,12,14,16,18,20]
y2 = [0,1,2,4,12,14,16,17,14,22]
x = range(0,10)

# create plot
plt = pg.plot()
plt.showGrid(x=True,y=True)
plt.addLegend()

# set properties
plt.setLabel('left', 'Value', units='V')
plt.setLabel('bottom', 'Time', units='s')
plt.setXRange(0,10)
plt.setYRange(0,20)
plt.setWindowTitle('pyqtgraph plot')

# plot
c1 = plt.plot(x, y, pen='b', symbol='x', symbolPen='b', symbolBrush=0.2, name='red')
c2 = plt.plot(x, y2, pen='r', symbol='o', symbolPen='r', symbolBrush=0.2, name='blue')

## Start Qt event loop.
if __name__ == '__main__':
    import sys
    if sys.flags.interactive != 1 or not hasattr(pg.QtCore, 'PYQT_VERSION'):
        pg.QtGui.QApplication.exec_()