# Face Presence Detection

## Project Description

Face Presence Detection is a monitoring system designed to detect whether a candidate remains present in the camera frame during an interview session. The system continuously analyzes video frames, identifies face presence, and calculates the duration for which the candidate is absent.

This project was developed as part of an internship assignment focused on interview monitoring and candidate engagement tracking.

---

## Objective

The main objectives of this project are:

- Detect the presence of a candidate's face in video frames.
- Monitor continuous face visibility.
- Identify periods when the candidate is absent from the frame.
- Calculate absence duration.
- Generate structured JSON output for further processing.

---

## Features

- Face detection using OpenCV.
- Continuous frame-by-frame monitoring.
- Presence/absence status tracking.
- Absence duration calculation.
- JSON-based output generation.
- Video sample testing support.
- Simple and lightweight implementation.

---

## Technology Stack

| Technology | Purpose |
|------------|----------|
| Python | Core Programming Language |
| OpenCV | Face Detection & Video Processing |
| JSON | Structured Output Format |

---

## Project Structure

```text
FacePresenceDetection/
│
├── main.py
├── output.json
├── test_video.mp4
├── README.md
└── requirements.txt
```

---

## Workflow

1. Load video input.
2. Read frames continuously.
3. Detect face presence in each frame.
4. Update presence status.
5. Calculate absence duration when no face is detected.
6. Store and display output in JSON format.

---

## Sample Output

```json
{
    "face_present": false,
    "duration_absent_sec": 4
}
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/24mca12-wq/FacePresenceDetection.git
```

### Install Dependencies

```bash
pip install opencv-python
```

---

## Running the Project

Place the video file inside the project directory and run:

```bash
python main.py
```

---

## Testing

The system was tested using recorded video samples containing:

- Face present in frame
- Face absent from frame
- Multiple transitions between present and absent states

---

## Edge Cases Considered

- Partial face visibility
- Temporary face absence
- Poor lighting conditions
- Camera blur and detection limitations

---

## Acceptance Criteria Covered

✔ Face Presence Detection

✔ Absence Monitoring

✔ Absence Duration Calculation

✔ JSON Output Generation

✔ Video Sample Testing

✔ Configurable Detection Parameters

---

## Future Improvements

- Real-time webcam integration
- MediaPipe-based face detection
- API integration using FastAPI
- Timestamp logging for each absence event
- Performance optimization for low-light conditions

---

## Author

**Kajal Kumari**

MCA Student

Internship Assignment Submission
