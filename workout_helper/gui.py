import sys
from PyQt5.QtWidgets import (QMainWindow, QAction, QApplication, QGridLayout,
                            QPushButton, QWidget, QSizePolicy, QSpacerItem,
                            QStackedWidget)
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):
    """
    MainWindow is the principal window of the application, it holds all the menu
    and toolbar layout that will be used inside the application.
    """
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        """
        initUI: used to create the basic layout of the main window

        """
    # Action definition to be used by Menu and Toolbar

        # to close the application
        self.exitAction = QAction(QIcon('images/logo.png'), 'Quit', self)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.setStatusTip('Exit Workout Helper')
        self.exitAction.triggered.connect(self.close)
        # to start a workout
        self.startAction = QAction(QIcon('images/start.png'),'Start working out!',self)
        self.startAction.setShortcut('Ctrl+S')
        self.startAction.setStatusTip('Start a Workout')
        self.startAction.triggered.connect(self.close)

    # UI  elements creation

        # initialize the status bar on the bottom
        self.statusBar()

        # create a menu bar and populate it
        self.menubar = self.menuBar()
        self.fileMenu = self.menubar.addMenu('&File')
        self.fileMenu.addAction(self.exitAction)

        # create a tool bar and populate it
        self.toolbar = self.addToolBar('Start')
        self.toolbar.addAction(self.startAction)

    # Define the default central space layout
        self.central_widget = QStackedWidget()
        main_central_widget = CentralWidgetMain(self)
        # add the main central widget to the stacked widget
        self.central_widget.addWidget(main_central_widget)
        # assign the stacked widget as main window central widget.
        self.setCentralWidget(self.central_widget)

        # define the default properties of the main window
        self.setGeometry(300,300,350,250)
        self.setWindowTitle('Workout Helper')

# slots
    # change the central widget according to clicked button
    def change_central_widget(self):
        sender = self.sender()
        if sender.text() == "Workout List":
            workout_list_widget = CentralWidgetWorkoutList(self)
            self.central_widget.addWidget(workout_list_widget)
            self.central_widget.setCurrentWidget(workout_list_widget)
        else:
            self.statusBar().showMessage(sender.text() + 'was pressed')


class CentralWidgetMain(QWidget):
    """
    This is the central widget of the application,
    this will be used to create all the different views used in the
    application
    """

    def __init__(self, parent = None):

        # Call to QWidget __init__()
        super(CentralWidgetMain, self).__init__(parent)

        # creating the grid layout
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.grid.setSpacing(0)

        #create widgets to fill the layout
        self.history = QPushButton('History')
        self.history.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.workout_list = QPushButton('Workout List')
        self.workout_list.setSizePolicy(QSizePolicy.Expanding,
            QSizePolicy.Expanding)

        self.create_exercise = QPushButton('Create exercise')
        self.create_exercise.setSizePolicy(QSizePolicy.Expanding,
            QSizePolicy.Expanding)

        self.create_workout = QPushButton('Create a Workout')
        self.create_workout.setSizePolicy(QSizePolicy.Expanding,
            QSizePolicy.Expanding)

        # populate layout
        self.grid.addWidget(self.history,4,1,2,4)
        self.grid.addWidget(self.workout_list, 0,1,2,4)
        self.grid.addWidget(self.create_workout,2,1,2,2)
        self.grid.addWidget(self.create_exercise,2,3,2,2)
        # Temporary spacer to create the desired display
        self.grid.addItem(QSpacerItem(100,100),0,0,5,1)
        # Define the signals
        self.workout_list.clicked.connect(self.parent().change_central_widget)

class CentralWidgetWorkoutList(QWidget):
    """
    This is the workout list central widget,
    this is where the user can see all the available workouts
    """

    def __init__(self, parent = None):

        # Call to QWidget __init__()
        super(CentralWidgetWorkoutList, self).__init__(parent)

        # creating the grid layout
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.grid.setSpacing(0)

        #create widgets for the layout
        self.history = QPushButton('History')
        self.history.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.workout_list = QPushButton('Workout List')
        self.workout_list.setSizePolicy(QSizePolicy.Expanding,
            QSizePolicy.Expanding)

        self.create_exercise = QPushButton('Create exercise')
        self.create_exercise.setSizePolicy(QSizePolicy.Expanding,
            QSizePolicy.Expanding)

        self.create_workout = QPushButton('Create a Workout')
        self.create_workout.setSizePolicy(QSizePolicy.Expanding,
            QSizePolicy.Expanding)

        # populate layout
        self.grid.addWidget(self.history,4,1,2,4)
        self.grid.addWidget(self.workout_list, 0,1,2,4)
        self.grid.addWidget(self.create_workout,2,1,2,2)
        self.grid.addWidget(self.create_exercise,2,3,2,2)
        # Temporary spacer to create the desired display
        # self.grid.addItem(QSpacerItem(100,100),0,0,5,1)
