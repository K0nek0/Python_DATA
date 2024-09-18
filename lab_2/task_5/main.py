import os
from PIL import Image
from sys import argv


def create_thumbnails(directory, extension):
    for filename in os.listdir(directory):
        if filename.lower().endswith(extension.lower()):
            file_path = os.path.join(directory, filename)

            with Image.open(file_path) as img:
                img = img.resize((50, 50))
                img.show()
                img.save(f'mini_{extension}')


if __name__ == "__main__":
    if len(argv) != 2:
        print('Usage: python main.py <file.extension>')
    else:
        file_extension = argv[1]
        create_thumbnails('.', file_extension)
