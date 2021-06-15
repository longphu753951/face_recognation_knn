import face_recognition
import pickle
from face_recognition.face_recognition_cli import image_files_in_folder

def predict(X_img_path, knn_clf=None, model_path=None, distance_threshold=0.6):
    # if not os.path.isfile(X_img_path) or os.path.splitext(X_img_path)[1][1:] not in ALLOWED_EXTENSIONS:
        # raise Exception("Invalid image path: {}".format(X_img_path))

    if knn_clf is None and model_path is None:
        raise Exception("Must supply knn classifier either thourgh knn_clf or model_path")

    #Khởi động file train các model KNN
    if knn_clf is None:
        with open(model_path, 'rb') as f:
            knn_clf = pickle.load(f)

    # Tìm vị trí gương mặt từ ảnh cắt từ webcam
    X_face_locations = face_recognition.face_locations(X_img_path)

    # Không thấy gương mặt nào thì sẽ trả lại kết quả rỗng
    if len(X_face_locations) == 0:
        return []

    # Mã hóa các gương mặt ở trong ảnh đã được cắt từ webcam 
    faces_encodings = face_recognition.face_encodings(X_img_path, known_face_locations=X_face_locations)

    # Dùng KNN model để tìm gương mặt phù hợp nhất với gương mặt trong Camera
    closest_distances = knn_clf.kneighbors(faces_encodings, n_neighbors=1)
    are_matches = [closest_distances[0][i][0] <= distance_threshold for i in range(len(X_face_locations))]

    # Predict classes and remove classifications that aren't within the threshold
    return [(pred, loc) if rec else ("unknown", loc) for pred, loc, rec in zip(knn_clf.predict(faces_encodings), X_face_locations, are_matches)]


