from train import train
from predict import predict
import cv2
import face_recognition
import pickle
from face_recognition.face_recognition_cli import image_files_in_folder
from Attendance import attendance


if __name__ == "__main__":
    print("Training KNN classifier...")
    classifier = train("image_knn/train", model_save_path="trained_knn_model.clf", n_neighbors=2)
    print("Training complete!")

    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Find all people in the image using a trained classifier model
        # Note: You can pass in either a classifier file name or a classifier model instance
        predictions = predict(X_img_path=rgb_frame, model_path="trained_knn_model.clf")

        for name, (top, right, bottom, left) in predictions:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            if(name != "unknown"):
                attendance(name)
            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        # Display the resulting image
        cv2.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()