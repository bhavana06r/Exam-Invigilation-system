import cv2
from pathlib import Path

from tracker import get_absent_students
from pose_detector import detect_pose
from behavior_engine import analyze
from visualizer import draw_student


def main():

    project_root = Path(__file__).parent.parent

    video_path = project_root / "sample_videos" / "exam.mp4"

    cap = cv2.VideoCapture(str(video_path))

    if not cap.isOpened():
        print("Unable to open video.")
        return

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        # -------------------------
        # Detect Students
        # -------------------------

        students = detect_pose(frame)

        final_students = []

        for student in students:

            result = analyze(student)

            final_students.append(result)

        # -------------------------
        # Draw Student Information
        # -------------------------

        for student in final_students:

            draw_student(frame, student)

        # -------------------------
        # Show Absent Students
        # -------------------------

        absent_students = get_absent_students()

        y = 30

        for sid in absent_students:

            cv2.putText(
                frame,
                f"Student {sid} Left Seat",
                (20, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 255),
                2
            )

            y += 30

        # -------------------------
        # Display
        # -------------------------

        cv2.imshow("AI Exam Invigilation", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()