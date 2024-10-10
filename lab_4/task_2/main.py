from argparse import ArgumentParser
from moviepy.editor import VideoFileClip
from PIL import Image
from shutil import rmtree
import os


def extract_frames(input_file, start_time, end_time, output_path, step=10):
    if not output_path:
        output_path = 'frames_output'
    if os.path.exists(output_path):
        rmtree(output_path)
    os.makedirs(output_path, exist_ok=True)
    
    with VideoFileClip(input_file) as video:
        clip = video.subclip(start_time, end_time)
        
        frame_number = 0
        
        for time in range(0, int(clip.duration), step):
            frame = clip.get_frame(time)

            frame_image = Image.fromarray(frame)
            frame_image.thumbnail((250, frame_image.height))
            frame_image.save(os.path.join(output_path, f"{frame_number}.png"))

            frame_number += 1


def main():
    parser = ArgumentParser()
    parser.add_argument('input_file')
    parser.add_argument('start_time')
    parser.add_argument('end_time')
    parser.add_argument('--output_path', default=None)
    parser.add_argument('--step', type=int, default=10)

    args = parser.parse_args()

    extract_frames(args.input_file, args.start_time, args.end_time, args.output_path, args.step)
    print(f"Frames successfully saved in '{args.output_path or 'frames_output'}'")


if __name__ == '__main__':
    main()
