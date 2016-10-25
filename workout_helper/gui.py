import sys

from PyQt5.QtWidgets import (QMainWindow, QAction, QApplication, QGridLayout,
                             QPushButton, QWidget, QSizePolicy, QSpacerItem,
                             QStackedWidget, QStyleOptionButton, QStyle)
from PyQt5.QtGui import QIcon, QPainter
from PyQt5.QtCore import QSize

import modele
from settings import *

class MainWindow(QMainWindow):
    """
    MainWindow is the principal window of the application, it holds all the menu
    and toolbar layout that will be used inside the application.
    """
    def __init__(self, parent=None):
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
        self.startAction = QAction(QIcon('images/start.png'),
                                   'Start working out!', self)
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
        self.breadcrumb = []
        self.central_widget = QStackedWidget()
        main_central_widget = CentralWidgetMain(self)
        # add the main central widget to the stacked widget
        self.breadcrumb.append(
            self.central_widget.addWidget(main_central_widget))
        # assign the stacked widget as main window central widget.
        self.setCentralWidget(self.central_widget)
        # define the default properties of the main window
        self.setGeometry(MAIN_WINDOW_POSITION_X,
                         MAIN_WINDOW_POSITION_Y,
                         MAIN_WINDOW_LENGTH,
                         MAIN_WINDOW_WIDTH
                         )
        self.setWindowTitle('Workout Helper')

    # slots
    # change the central widget according to clicked button
    def change_central_widget(self):
        sender = self.sender()
        if sender.text() == "Workout List":
            workout_list_widget = CentralWidgetWorkoutList(self)
            self.breadcrumb.append(
                self.central_widget.addWidget(workout_list_widget))
            self.central_widget.setCurrentWidget(workout_list_widget)
        elif sender.text() == "Back":
            self.breadcrumb.pop()
            self.central_widget.setCurrentIndex(self.breadcrumb.pop())
            self.breadcrumb.append(self.central_widget.currentIndex())
        else:
            self.statusBar().showMessage(sender.text() + ' was pressed')

class CentralWidgetMain(QWidget):
    """
    This is the central widget of the application,
    this will be used to create all the different views used in the
    application
    """

    def __init__(self, parent=None):

        # Call to QWidget __init__()
        super(CentralWidgetMain, self).__init__(parent)

        # creating the grid layout
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.grid.setSpacing(SPACING)

        #create widgets to fill the layout
        self.w_history = QPushButton('History')
        self.w_history.setSizePolicy(QSizePolicy.Expanding,
                                     QSizePolicy.Expanding)

        self.w_workout_list = QPushButton('Workout List')
        self.w_workout_list.setSizePolicy(QSizePolicy.Expanding,
                                          QSizePolicy.Expanding)

        self.w_create_exercise = QPushButton('Create exercise')
        self.w_create_exercise.setSizePolicy(QSizePolicy.Expanding,
                                             QSizePolicy.Expanding)

        self.w_create_workout = QPushButton('Create a Workout')
        self.w_create_workout.setSizePolicy(QSizePolicy.Expanding,
                                            QSizePolicy.Expanding)

        # populate layout
        self.grid.addWidget(self.w_history, 4, 1, 2, 4)
        self.grid.addWidget(self.w_workout_list, 0, 1, 2, 4)
        self.grid.addWidget(self.w_create_workout, 2, 1, 2, 2)
        self.grid.addWidget(self.w_create_exercise, 2, 3, 2, 2)
        # Temporary spacer to create the desired display
        self.grid.addItem(QSpacerItem(100, 100), 0, 0, 5, 1)
        # Define the signals
        self.w_workout_list.clicked.connect(self.parent().change_central_widget)

class CentralWidgetWorkoutList(QWidget):
    """
    This is the workout list central widget,
    this is where the user can see all the available workouts
    it's based on a grid, each workout is displayed in a cell
    of the grid, each workout is a QPushButton and will lead
    to the same Workout Overview.
    """

    def __init__(self, parent=None):

        # Call to QWidget __init__()
        super(CentralWidgetWorkoutList, self).__init__(parent)

        # creating the grid layout
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.grid.setSpacing(SPACING)

        # TESTING ONLY
        workouts = []
        a = modele.Workout('Workout A')
        workouts.append(a)
        b = modele.Workout('Workout B')
        workouts.append(b)
        c = modele.Workout('Workout C')
        workouts.append(c)
        d = modele.Workout('Workout D')
        workouts.append(d)
        e = modele.Workout('Workout E')
        workouts.append(e)
        f = modele.Workout('Workout F')
        workouts.append(f)
        # END OF TESTING CODE

        self.w_workout_list = []
        #create widgets for the layout
        for workout in workouts:
            #creating the button
            temp = MyPushButton(workout.name)
            temp.setSizePolicy(QSizePolicy.Expanding,
                               QSizePolicy.Expanding)
            temp.setIcon(QIcon(workout.icon_path))
            # Define the signals
            temp.clicked.connect(self.parent().change_central_widget)
            self.w_workout_list.append(temp)

        self.back_button = QPushButton('Back')
        self.back_button.clicked.connect(self.parent().change_central_widget)



        # populate layout
        i = 0
        j = 0
        for button in self.w_workout_list:
            self.grid.addWidget(button, i, j, WORKOUT_BUTTON_WIDTH_CELL,
                                WORKOUT_BUTTON_LENGTH_CELL)
            j += WORKOUT_BUTTON_LENGTH_CELL
            if j >= WORKOUT_PER_LINE * WORKOUT_BUTTON_LENGTH_CELL :
                i += WORKOUT_BUTTON_WIDTH_CELL
                j = 0
        self.grid.addWidget(self.back_button, i+WORKOUT_BUTTON_WIDTH_CELL+1,
                            WORKOUT_PER_LINE*WORKOUT_BUTTON_LENGTH_CELL-1)

        # Temporary spacer to create the desired display
        # self.grid.addItem(QSpacerItem(100,100),0,0,5,1)

class MyPushButton(QPushButton):
    def __init__(self, label=None, parent=None):
        super(MyPushButton, self).__init__(label, parent)

        self.pad = 4     # padding between the icon and the button frame
        self.minSize = 8 # minimum size of the icon

        sizePolicy = QSizePolicy(QSizePolicy.Expanding,
                                 QSizePolicy.Expanding)
        self.setSizePolicy(sizePolicy)

    def paintEvent(self, event):

        qp = QPainter()
        qp.begin(self)

        #---- get default style ----
        opt = QStyleOptionButton()
        self.initStyleOption(opt)

        #---- scale icon to button size ----
        Rect = opt.rect
        h = Rect.height()
        w = Rect.width()
        iconSize = max(min(h, w) - 2 * self.pad, self.minSize)
        opt.iconSize = QSize(iconSize, iconSize)

        #---- draw button ----
        self.style().drawControl(QStyle.CE_PushButton, opt, qp, self)
        qp.end()
