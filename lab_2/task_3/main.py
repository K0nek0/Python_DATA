from PIL import Image, ImageFilter

puppy = 'puppy.jpg'
logo = 'python_symbol.jpg'
with Image.open(puppy) as img, Image.open(logo) as img_logo:
    img.load()
    img_logo.load()

img_logo = img_logo.convert("L")

threshold = 50
img_logo = img_logo.point(lambda x: 255 if x > threshold else 0)
img_logo = img_logo.resize(
    (img_logo.width // 5, img_logo.height // 5)
)

img_logo = img_logo.filter(ImageFilter.CONTOUR)
img_logo = img_logo.point(lambda x: 0 if x == 255 else 255)

position = (
    (img.width - img_logo.width) // 2,
    (img.height - img_logo.height) // 2
)
img.paste(img_logo, position, img_logo)
img.show()
img.save('puppy_with_watermark.jpg')
