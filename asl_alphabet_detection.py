import cv2
import dlib
from scipy.spatial import distance
import os

# Calculate Eye Aspect Ratio
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

# Thresholds (tuned for better accuracy)
EAR_THRESHOLD = 0.21  # Lowered for more sensitivity
CONSEC_FRAMES = 30    # Increased for more robust detection
counter = 0

# Model path
MODEL_PATH = r"C:\Users\Shruti Singh\OneDrive\Desktop\ComputerVision\shape_predictor_68_face_landmarks.dat"

# Check if model file exists
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")

# Load dlib's detector and landmark predictor
try:
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(MODEL_PATH)
except Exception as e:
    print(f"Error loading dlib models: {e}")
    exit(1)

# Eye landmark points
LEFT_EYE = list(range(42, 48))
RIGHT_EYE = list(range(36, 42))

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit(1)

while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        print("Error: Could not access the webcam or capture a frame.")
        break
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)
    if len(faces) == 0:
        cv2.putText(frame, "No face detected", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    for face in faces:
        shape = predictor(gray, face)
        landmarks = [(shape.part(i).x, shape.part(i).y) for i in range(68)]

        left_eye = [landmarks[i] for i in LEFT_EYE]
        right_eye = [landmarks[i] for i in RIGHT_EYE]

        left_ear = eye_aspect_ratio(left_eye)
        right_ear = eye_aspect_ratio(right_eye)
        avg_ear = (left_ear + right_ear) / 2.0

        if avg_ear < EAR_THRESHOLD:
            counter += 1
            if counter >= CONSEC_FRAMES:
                cv2.putText(frame, "DROWSINESS ALERT!", (20, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 4)
        else:
            counter = 0

        cv2.putText(frame, f"EAR: {avg_ear:.2f}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

    cv2.imshow("Drowsiness Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
