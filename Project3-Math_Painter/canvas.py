import numpy as np
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