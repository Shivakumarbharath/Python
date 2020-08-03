from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open('E:\Bharath\Python\PYTHONprograms\Tkinter\Viewer\destination_1.jpg')
num = np.array(im)
print(num, num.mean(axis=2))
# to make it in white and black
plt.imshow(num.mean(axis=2), cmap='gray')
plt.show()
