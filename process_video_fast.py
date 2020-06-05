import youtube_dl
import cv2
import face_recognition
import sklearn
from sklearn.datasets import fetch_lfw_people

from faced import FaceDetector
from faced.utils import annotate_image

lfw_people = fetch_lfw_people()

face_detector = FaceDetector()

def process_video(vidfile):
    # start processing video
    input_movie = cv2.VideoCapture(vidfile)
    length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))
    # Write the resulting image to the output video file
    codec = int(input_movie.get(cv2.CAP_PROP_FOURCC))
    fps = int(input_movie.get(cv2.CAP_PROP_FPS))
    frame_width = int(input_movie.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(input_movie.get(cv2.CAP_PROP_FRAME_HEIGHT))
    output_movie = cv2.VideoWriter('output.mp4', codec, fps, (frame_width,frame_height))
    frame_num=0

    while frame_num < length:
        ret, frame = input_movie.read()
        frame_num += 1
        if not ret:
            continue
        # bgr to rgb
        # rgb_img = frame[:, :, ::-1]
        rgb_img = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2RGB)

        # Receives RGB numpy image (HxWxC) and
        # returns (x_center, y_center, width, height, prob) tuples.
        bboxes = face_detector.predict(rgb_img, 0.7)

        # Use this utils function to annotate the image.
        frame = annotate_image(frame, bboxes)

        print("Writing frame {} / {}".format(frame_num, length))
        output_movie.write(frame)

    # Show the image
    input_movie.release()
    output_movie.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    print('process_video_fast.py')
    process_video("yeold.mp4")
