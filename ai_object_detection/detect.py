import cv2
import time
from ultralytics import YOLO

from utils.config import *
from utils.drawing import draw_box, draw_dashboard
from utils.json_writer import save_output

# -----------------------------
# Load YOLO Model
# -----------------------------
model = YOLO("yolov8m.pt")   # Better than yolov8n for phone detection

# -----------------------------
# Open Video
# -----------------------------
cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    print("❌ Cannot open video!")
    exit()

prev_time = time.time()

# Colors
COLORS = {
    "person": (0, 255, 0),
    "cell phone": (0, 0, 255),
    "laptop": (255, 255, 0),
    "book": (255, 0, 255),
    "backpack": (255, 165, 0)
}

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Run YOLO
    results = model(frame, verbose=False)

    counts = {
        "person": 0,
        "cell phone": 0,
        "laptop": 0,
        "book": 0,
        "backpack": 0
    }

    for result in results:

        for box in result.boxes:

            cls = int(box.cls[0])
            conf = float(box.conf[0])

            if conf < CONFIDENCE:
                continue

            label = model.names[cls]

            if label not in TARGET_CLASSES:
                continue

            counts[label] += 1

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            draw_box(
                frame,
                x1,
                y1,
                x2,
                y2,
                label,
                COLORS[label]
            )

    # -----------------------------
    # Status
    # -----------------------------
    if counts["cell phone"] > 0:
        status = "PHONE DETECTED"

    elif counts["book"] > 0:
        status = "BOOK DETECTED"

    elif counts["backpack"] > 0:
        status = "BACKPACK DETECTED"

    else:
        status = "NORMAL"

    # -----------------------------
    # FPS
    # -----------------------------
    current = time.time()
    fps = max(1, int(1 / (current - prev_time)))
    prev_time = current

    # -----------------------------
    # Dashboard
    # -----------------------------
    draw_dashboard(
        frame,
        counts,
        status,
        fps
    )

    # -----------------------------
    # Save JSON
    # -----------------------------
    output = {
        "students": counts["person"],
        "phones": counts["cell phone"],
        "laptops": counts["laptop"],
        "books": counts["book"],
        "backpacks": counts["backpack"],
        "status": status
    }

    save_output(OUTPUT_JSON, output)

    cv2.imshow("AI Exam Invigilation", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()