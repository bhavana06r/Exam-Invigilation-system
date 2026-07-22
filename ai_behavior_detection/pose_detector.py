from ultralytics import YOLO

model = YOLO("yolo11n-pose.pt")


def detect_pose(frame):

    results = model.track(
        frame,
        persist=True,
        tracker="botsort.yaml",
        verbose=False
    )

    students = []

    if len(results) == 0:
        return students

    result = results[0]

    if result.boxes is None or result.keypoints is None:
        return students

    boxes = result.boxes
    keypoints = result.keypoints.xy.cpu().numpy()

    # NEW
    confidences = result.keypoints.conf.cpu().numpy()

    if boxes.id is not None:
        ids = boxes.id.cpu().numpy().astype(int)
    else:
        ids = [-1] * len(keypoints)

    for box, person, conf, sid in zip(boxes, keypoints, confidences, ids):

        x1, y1, x2, y2 = map(int, box.xyxy[0])

        students.append({
            "id": int(sid),
            "box": [x1, y1, x2, y2],
            "keypoints": person,
            "confidence": conf      # NEW
        })

    return students