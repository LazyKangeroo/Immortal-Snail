import math

from enum import Enum

from PyQt6.QtGui import QCursor

class Directions(Enum):
    RIGHT = ['sprites/cat/right_1.png', 'sprites/cat/right_2.png', 'sprites/cat/right_3.png', 'sprites/cat/right_4.png']
    LEFT = ['sprites/cat/left_1.png', 'sprites/cat/left_2.png','sprites/cat/left_3.png', 'sprites/cat/left_4.png']
    FORWARD = ['sprites/cat/forward_1.png','sprites/cat/forward_2.png','sprites/cat/forward_3.png','sprites/cat/forward_4.png']
    BACKWARD = ['sprites/cat/back_1.png','sprites/cat/back_2.png','sprites/cat/back_3.png','sprites/cat/back_4.png']

class Cat:
        def __init__(self, win):
            # Snail attributes
            self.sprite = 0
            self.count = 0

            #? Window object
            self.win = win

        def sprite_handle(self):
            self.count += 1

            if self.count >= 3:
                self.count = 0
                if self.sprite < 3:
                     self.sprite += 1
                else:
                    self.sprite = 0

            return self.sprite

        def update(self):
            ## Follow mouse
            mouse_pos = QCursor.pos()

            #? Get direction/distance of mouse
            self.geo = self.win.geometry() # This gets pos and size

            #* Calculate distance
            self.distanceX = mouse_pos.x() - self.geo.x() # if positive then move right, if negative then left
            self.distanceY = mouse_pos.y() - self.geo.y() # if positve then move down, if negative then move up
            distance = math.hypot(self.distanceX,self.distanceY)

            # since there are 4 different directional views I need to get an angle and see if the sprite is in a set angle range before changing directional sprite.
            # range between like 45-135 for up and down and the rest is left and right

            if self.distanceX < 0:
                 direction = Directions.LEFT
            else:
                 direction = Directions.RIGHT

            idle = False
            if distance < 5:
                idle = True
            else:
                speed = 10
                #  direction vector
                velocoityX = (self.distanceX / distance) * speed
                velocoityY = (self.distanceY / distance) * speed

                new_x = self.geo.x() + velocoityX
                new_y = self.geo.y() + velocoityY

            return {
                 'direction' : direction,
                 'x' : self.geo.x() if idle else new_x, # type: ignore
                 'y' : self.geo.y() if idle else new_y,  # type: ignore
                 'idle' : idle
            }