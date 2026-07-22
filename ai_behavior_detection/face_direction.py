import cv2
import mediapipe as mp

mp_face_mesh = mp.solutions.face_mesh

face_mesh = mp_face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)


def get_face_direction(face_crop):

    rgb = cv2.cvtColor(face_crop, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb)

    if not results.multi_face_landmarks:
        return "UNKNOWN"

    face = results.multi_face_landmarks[0]

    nose = face.landmark[1]
    left_cheek = face.landmark[234]
    right_cheek = face.landmark[454]

    center = (left_cheek.x + right_cheek.x) / 2

    diff = nose.x - center

    if diff > 0.03:
        return "RIGHT"

    elif diff < -0.03:
        return "LEFT"

    return "FRONT"