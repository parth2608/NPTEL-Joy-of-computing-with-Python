from PIL import Image

img = Image.open('obtained.png')

transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)

transposed_img.save('corrected.png')

print('Done Flipping!')
