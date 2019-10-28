import numpy
from PIL import Image

im = Image.open('lena.jpg')
pixelMap = im.load()
# I = numpy.asarray(Image.open('lena.jpg'))
# print(I)
img = Image.new(im.mode, im.size)
pixelNew = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        if 0 <= pixelMap[i, j] <= 31:
            pixelNew[i, j] = 0
        elif 32 <= pixelMap[i, j] <= 63:
            pixelNew[i, j] = 1
        elif 64 <= pixelMap[i, j] <= 95:
            pixelNew[i, j] = 2
        elif 96 <= pixelMap[i, j] <= 127:
            pixelNew[i, j] = 3
        elif 128 <= pixelMap[i, j] <= 159:
            pixelNew[i, j] = 4
        elif 160 <= pixelMap[i, j] <= 191:
            pixelNew[i, j] = 5
        elif 192 <= pixelMap[i, j] <= 223:
            pixelNew[i, j] = 6
        elif 224 <= pixelMap[i, j] <= 255:
            pixelNew[i, j] = 7
img.save('lena_compressed.jpg')
# J = numpy.asarray(Image.open('lena_compressed.jpg'))
#   print(J)
