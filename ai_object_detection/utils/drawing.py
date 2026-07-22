import cv2


def draw_box(frame, x1, y1, x2, y2, label, color):
    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)

    cv2.putText(
        frame,
        label,
        (x1, y1 - 8),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        color,
        2
    )


def draw_dashboard(frame, counts, status, fps):

    cv2.rectangle(frame, (0, 0), (420, 190), (40, 40, 40), -1)

    cv2.putText(frame, f"Students : {counts['person']}", (20, 35),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.putText(frame, f"Phones : {counts['cell phone']}", (20, 65),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    cv2.putText(frame, f"Laptops : {counts['laptop']}", (20, 95),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

    cv2.putText(frame, f"Books : {counts['book']}", (20, 125),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 200, 255), 2)

    cv2.putText(frame, f"Status : {status}", (20, 155),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    cv2.putText(frame, f"FPS : {fps}", (20, 185),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)