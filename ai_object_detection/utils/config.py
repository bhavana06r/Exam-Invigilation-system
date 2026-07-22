import os

# Base Folder
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Model Path
MODEL_PATH = os.path.join(BASE_DIR, "models", "yolov8n.pt")

# Video Path
VIDEO_PATH = os.path.join(
    BASE_DIR,
    "..",
    "sample_videos",
    "exam.mp4"
)

# Output JSON
OUTPUT_JSON = os.path.join(
    BASE_DIR,
    "output",
    "object_output.json"
)

# Confidence Threshold
CONFIDENCE = 0.45

# Allowed Objects
TARGET_CLASSES = [
    "person",
    "cell phone",
    "laptop",
    "book",
    "backpack"
]