from argparse import ArgumentParser
from moviepy.editor import VideoFileClip


def extract_clip(input_file, start_time, end_time, output_file):
    with VideoFileClip(input_file) as video:
        clip = video.subclip(start_time, end_time)
        clip.write_videofile(output_file, codec='libx264')


def main():
    parser = ArgumentParser()
    parser.add_argument('input_file')
    parser.add_argument('start_time')
    parser.add_argument('end_time')
    parser.add_argument('output_file')

    args = parser.parse_args()

    extract_clip(args.input_file, args.start_time, args.end_time, args.output_file)


if __name__ == '__main__':
    main()
