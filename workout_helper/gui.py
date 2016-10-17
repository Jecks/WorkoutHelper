import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        exitAction = QAction(QIcon('images/logo.png'), 'Quit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Workout Helper')
        exitAction.triggered.connect(self.close)

        startAction = QAction(QIcon('images/start.png'),'Start',self)
        startAction.setShortcut('Ctrl+S')
        startAction.setStatusTip('Start a Workout')
        startAction.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar('Start')
        toolbar.addAction(startAction)

        self.setGeometry(300,300,350,250)
        self.setWindowTitle('Workout Helper')
        self.show()
