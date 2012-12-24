#! /usr/bin/env python3
# Filename: smarty

from PIL import Image

img = Image.open('oxygen.png')

# left-low corner to right-up corner
box = (0, 43, 608, 52)

belt = img.crop(box)

pixels = belt.getdata()

print ('mode: %s' %img.mode)
print ('pixel: %d' %len(pixels))
print (pixels[0])

low_belt = belt.convert('L')
low_pixels = low_belt.getdata()

sentence = ''
for i in range(0, 608, 7):
    sentence += chr(low_pixels[i])
print (sentence)

ans = [105, 110, 116, 101, 103, 114, 105, 116, 121]
next_level = ''.join([chr(i) for i in ans])
print (next_level)
