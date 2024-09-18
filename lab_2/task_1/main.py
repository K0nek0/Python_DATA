from PIL import Image

filename = 'puppy.jpg'
with Image.open(filename) as img:
    img.load()

red, green, blue = img.split()

zeroed_band = red.point(lambda _: 0)

red_merge = Image.merge('RGB', (red, zeroed_band, zeroed_band))
green_merge = Image.merge('RGB', (zeroed_band, green, zeroed_band))
blue_merge = Image.merge('RGB', (zeroed_band, zeroed_band, blue))

img.show()
red_merge.show()
green_merge.show()
blue_merge.show()

red_merge.save('red_puppy.jpg')
green_merge.save('green_puppy.jpg')
blue_merge.save('blue_puppy.jpg')
