import sys

class Workout():
    """
    this class represents a workout and all associated methods.
    a workout is identified by its name and contain a list of exercises.
    a workout compute its duration from the list of exercises.
    a workout can have an icon that will be used by the gui to represent it.
    a workout has a description.
    """
    
    def __init__(self,
                 name,
                 description='',
                 exercises=[],
                 icon_path='images/start.png'
                 ):
        self.name = name
        self.description = description
        self.exercises = exercises
        self.icon_path = icon_path
