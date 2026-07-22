import time

students = {}


def update(student_id):

    now = time.time()

    if student_id not in students:

        students[student_id] = {

            "last_seen": now,

            "direction": "FRONT",

            "history": [],

            "look_count": 0,

            "hand_count": 0,

            "talk_count": 0,

            "stand_count": 0,

            "phone_count": 0

        }

    students[student_id]["last_seen"] = now

    return students[student_id]


def get_absent_students():

    now = time.time()

    absent = []

    for sid, data in students.items():

        if now - data["last_seen"] > 3:

            absent.append(sid)

    return absent