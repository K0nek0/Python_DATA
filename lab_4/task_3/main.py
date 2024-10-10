import cv2
from argparse import ArgumentParser


def play_video_with_info(video_path):
    video = cv2.VideoCapture(video_path)
    fps = video.get(cv2.CAP_PROP_FPS)
    video_name = video_path.split('/')[-1]

    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break

        text = f"Name: {video_name}, FPS: {fps:.2f}"
        cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow('Video', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'): # Немного костыльное значение для waitKey(). Есть вариант с использованием time.
            break

    video.release()
    cv2.destroyAllWindows()


def main():
    parser = ArgumentParser()
    parser.add_argument('video_path')
    
    args = parser.parse_args()
    
    play_video_with_info(args.video_path)


if __name__ == '__main__':
    main()
