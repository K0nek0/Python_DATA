from PIL import Image
from sys import argv

filename = argv[1]
with Image.open(filename) as img:
    img.load()

pixels = img.getdata()
red_val = green_val = blue_val = 0

for pixel in pixels:
    r, g, b = pixel[:3]
    red_val += r
    green_val += g
    blue_val += b

if red_val > green_val and red_val > blue_val:
    dominant_color = 'Red'
elif green_val > red_val and green_val > blue_val:
    dominant_color = 'Green'
else:
    dominant_color = 'Blue'

print(f"Преобладающий цвет: {dominant_color}")
