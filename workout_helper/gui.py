import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    """
    MainWindow is the principal window of the application, it holds all the menu
    and toolbar layout that will be used inside the application.
    """
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        initUI: used to create the basic layout of the main window

        """
        # Action definition to be used by Menu and Toolbar

        # to close the application
        exitAction = QAction(QIcon('images/logo.png'), 'Quit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit Workout Helper')
        exitAction.triggered.connect(self.close)
        # to start a workout
        startAction = QAction(QIcon('images/start.png'),'Start',self)
        startAction.setShortcut('Ctrl+S')
        startAction.setStatusTip('Start a Workout')
        startAction.triggered.connect(self.close)

        # initialize the status bar on the bottom
        self.statusBar()

        # create a menu bar and populate it
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        # create a tool bar and populate it
        toolbar = self.addToolBar('Start')
        toolbar.addAction(startAction)

        # define the default properties of the main window
        self.setGeometry(300,300,350,250)
        self.setWindowTitle('Workout Helper')

        #draw the window
        self.show()
