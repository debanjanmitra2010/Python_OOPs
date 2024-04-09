import numpy as np
from PIL import Image  # Pillow Library

# Create 3D numpy array of zeros, then replace zeros (black pixels) with yellow pxls
data = np.zeros((5, 4, 3), dtype=np.uint8)  # 5- Horizontally, 4- Vertically, 3- Depth
data[:] = [255, 255, 0]  # Replacing with the Data values
print(data)

data[0:3, 0:2] = [255, 200, 255]  # Row and Column
data[3:4, 1:4] = [24, 89, 120]  # Row and Column

img = Image.fromarray(data, 'RGB')
img.save('canvas.png')