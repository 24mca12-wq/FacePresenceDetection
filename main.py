import cv2
import json
import time

cap = cv2.VideoCapture("test_video.mp4")

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

absence_start = None

while True:

    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )

    if len(faces) > 0:

        absence_start = None

        output = {
            "face_present": True,
            "duration_absent_sec": 0
        }

        print(output)

    else:

        if absence_start is None:
            absence_start = time.time()

        duration = round(
            time.time() - absence_start,
            2
        )

        output = {
            "face_present": False,
            "duration_absent_sec": duration
        }

        print(output)

    with open(
        "output.json",
        "w"
    ) as f:

        json.dump(
            output,
            f,
            indent=4
        )

cap.release()

print("FINISHED")
