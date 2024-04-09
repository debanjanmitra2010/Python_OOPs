import numpy as np
import self as self
from PIL import Image  # Pillow Library


class Canvas:
    """Object where all shapes are going to be drawn"""

    def __init__(self, width, height, color):
        self.width = width
        self.color = color
        self.height = height

    # Create 3D numpy array of zeros,
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
    # then replace zeros (black pixels) with mentioned pxls
        self.data[:] = self.color # 5- Horizontally, 4- Vertically, 3- Depth

    def make(self, imagepath):
        """Converts the current array into an image file"""
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)

class Rectangle:

    def __init__(self, x, y, width, height, color):
        self.color = color
        self.height = height
        self.width = width
        self.y = y
        self.x = x

    def draw(self, canvas):
        """Draws itself into the canvas"""
        # Changes a slice of the array with new values
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color


class Square:
    """A Square shape that can be drawn on a Canvas object"""
    def __init__(self, x, y, side, color):
        self.color = color
        self.side = side
        self.y = y
        self.x = x

    def draw(self, canvas):
        """Draws itself into the canvas"""
        # Changes a slice of the array with new values
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color


canvas = Canvas(height=20, width=30, color=(255, 255, 255))
r1 = Rectangle(x=1, y=6, height=7, width=10, color=(100, 200, 125))
r1.draw(canvas)
s1 = Square(x=1, y=3, side=3, color=(0, 100, 222))
s1.draw(canvas)
canvas.make('canvas.png')
