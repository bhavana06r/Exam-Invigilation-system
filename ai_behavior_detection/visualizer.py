import cv2


def draw_student(frame, student):

    x1, y1, x2, y2 = student["box"]

    risk = student["risk"]

    # -----------------------
    # Box Color Based on Risk
    # -----------------------

    if risk == "NORMAL":
        color = (0, 255, 0)          # Green

    elif risk == "LOW":
        color = (0, 255, 255)        # Yellow

    elif risk == "MEDIUM":
        color = (0, 165, 255)        # Orange

    elif risk == "HIGH":
        color = (0, 0, 255)          # Red

    elif risk == "CHEATING":
        color = (0, 0, 150)          # Dark Red

    else:
        color = (0, 255, 0)

    # -----------------------
    # Draw Bounding Box
    # -----------------------

    cv2.rectangle(
        frame,
        (x1, y1),
        (x2, y2),
        color,
        2
    )

    # -----------------------
    # Student ID
    # -----------------------

    cv2.putText(
        frame,
        f"ID : {student['id']}",
        (x1, y1 - 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        color,
        2
    )

    # -----------------------
    # Risk
    # -----------------------

    cv2.putText(
        frame,
        f"Risk : {risk}",
        (x1, y1 - 75),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        color,
        2
    )

    # -----------------------
    # Score
    # -----------------------

    cv2.putText(
        frame,
        f"Score : {student['score']}",
        (x1, y1 - 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        color,
        2
    )

    # -----------------------
    # Behavior
    # -----------------------

    behavior = ", ".join(student["behavior"])

    cv2.putText(
        frame,
        behavior,
        (x1, y1 - 25),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        color,
        2
    )