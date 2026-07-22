from tracker import update


def analyze(student):

    kp = student["keypoints"]

    box = student["box"]
    sid = student["id"]

    state = update(sid)
    history = state["history"]

    behavior = []

    # -----------------------
    # Keypoints
    # -----------------------

    nose = kp[0]

    left_eye = kp[1]
    right_eye = kp[2]

    left_ear = kp[3]
    right_ear = kp[4]

    left_shoulder = kp[5]
    right_shoulder = kp[6]

    left_wrist = kp[9]
    right_wrist = kp[10]

    # -----------------------
    # Head Direction Detection
    # -----------------------

    shoulder_center = (left_shoulder[0] + right_shoulder[0]) / 2
    shoulder_width = abs(right_shoulder[0] - left_shoulder[0])

    offset = nose[0] - shoulder_center

    threshold = shoulder_width * 0.12

    eye_distance = abs(left_eye[0] - right_eye[0])
    ear_distance = abs(left_ear[0] - right_ear[0])

    direction = "FRONT"

    # Nose shifted
    if offset > threshold:
        direction = "RIGHT"

    elif offset < -threshold:
        direction = "LEFT"

    # Eyes become closer
    elif eye_distance < shoulder_width * 0.18:

        if nose[0] > shoulder_center:
            direction = "RIGHT"
        else:
            direction = "LEFT"

    # One ear disappears
    elif ear_distance < shoulder_width * 0.10:

        if nose[0] > shoulder_center:
            direction = "RIGHT"
        else:
            direction = "LEFT"

    # -----------------------
    # Looking Detection
    # -----------------------

    if direction != "FRONT":

        state["look_count"] += 1

        if state["look_count"] > 10:
            behavior.append(f"Looking {direction}")

    else:

        state["look_count"] = max(0, state["look_count"] - 1)

    # -----------------------
    # Direction History
    # -----------------------

    history.append(direction)

    if len(history) > 30:
        history.pop(0)

    # -----------------------
    # Talking Detection
    # -----------------------

    changes = 0
    previous = None

    for d in history:

        if d == "FRONT":
            continue

        if previous is None:
            previous = d
            continue

        if previous != d:
            changes += 1
            previous = d

    if changes >= 5:

        state["talk_count"] += 1

        if "Possible Talking" not in behavior:
            behavior.append("Possible Talking")

    else:

        state["talk_count"] = max(0, state["talk_count"] - 1)

    # -----------------------
    # Hand Raised
    # -----------------------

    handRaised = False

    if left_wrist[1] < left_shoulder[1]:
        handRaised = True

    if right_wrist[1] < right_shoulder[1]:
        handRaised = True

    if handRaised:

        state["hand_count"] += 1

        if "Hand Raised" not in behavior:
            behavior.append("Hand Raised")

    else:

        state["hand_count"] = max(0, state["hand_count"] - 1)

    # -----------------------
    # Standing Detection
    # -----------------------

    x1, y1, x2, y2 = box

    height = y2 - y1
    width = x2 - x1

    if height > width * 2.2:

        state["stand_count"] += 1

        if "Standing" not in behavior:
            behavior.append("Standing")

    else:

        state["stand_count"] = max(0, state["stand_count"] - 1)

    # -----------------------
    # Score Calculation
    # -----------------------

    look_score = min(int(state["look_count"] * 0.5), 30)
    talk_score = min(int(state["talk_count"] * 1.0), 30)
    hand_score = min(int(state["hand_count"] * 0.5), 20)
    stand_score = min(int(state["stand_count"] * 0.5), 20)

    score = look_score + talk_score + hand_score + stand_score

    score = min(score, 100)

    # -----------------------
    # Default Behaviour
    # -----------------------

    if len(behavior) == 0:
        behavior.append("Normal")

    # -----------------------
    # Risk Level
    # -----------------------

    if score >= 90:
        risk = "HIGH"

    elif score >= 60:
        risk = "MEDIUM"

    elif score >= 25:
        risk = "LOW"

    else:
        risk = "NORMAL"

    # -----------------------
    # Debug (Optional)
    # -----------------------

    # Uncomment these lines for debugging
    #
    # print(
    #     f"ID:{sid} | Dir:{direction} | "
    #     f"Look:{state['look_count']} | "
    #     f"Talk:{state['talk_count']} | "
    #     f"Score:{score}"
    # )

    # -----------------------
    # Return
    # -----------------------

    return {

        "id": sid,
        "box": box,
        "behavior": behavior,
        "direction": direction,
        "score": score,
        "risk": risk

    }