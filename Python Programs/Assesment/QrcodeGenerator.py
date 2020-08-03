import qrcode
import matplotlib.pyplot as plt

data = '''Anything You want in a Qr code
'''

img = qrcode.make(data)
img.save('sample.jpg')
