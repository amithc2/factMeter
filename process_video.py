import youtube_dl
import cv2
import face_recognition
import sklearn
from sklearn.datasets import fetch_lfw_people
lfw_people = fetch_lfw_people()

def process_video(vidfile):
    face_localizations = []
    face_encodings = []
    face_ids = []
    frame_num = 0

    # start processing video
    input_movie = cv2.VideoCapture(vidfile)
    length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))
    while True:
        ret, frame = input_movie.read()
        frame_num += 1
        if not ret:
            continue
        # bgr to rgb
        rgb_frame = frame[:, :, ::-1]

        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_frame, model="hog")
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        if face_encodings:
            face_encodings = face_encodings[0]
        face_ids = []
        # for face_encoding in face_encodings:
            # See if the face is a match for the faces in the dataset
        #     match = face_recognition.compare_faces(lfw_people.data, face_encoding, tolerance=0.50)
        #     name = None
        #     for i in range(len(match)):
        #         if match[i]:
        #             name = lfw_people.target_names[i]
        #             break
        #
        #     face_ids.append(name)

        # Label the results
        for (top, right, bottom, left), name in zip(face_locations, face_ids):
            isEmpty = (top, right, bottom, left)
            if not name:
                name = 'unknown'

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

        # Write the resulting image to the output video file
        codec = int(input_movie.get(cv2.CAP_PROP_FOURCC))
        fps = int(input_movie.get(cv2.CAP_PROP_FPS))
        frame_width = int(input_movie.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(input_movie.get(cv2.CAP_PROP_FRAME_HEIGHT))
        output_movie = cv2.VideoWriter('output.mp4', codec, fps, (frame_width,frame_height))
        print("Writing frame {} / {}".format(frame_num, length))
        output_movie.write(frame)

    # All done!
    input_movie.release()
    output_movie.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    print('process_video.py')
    process_video("yeold.mp4")
