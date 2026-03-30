# Real-Time Face Blurring

A lightweight Python script that performs real-time face detection and anonymization (blurring) using your computer's webcam.

This project uses OpenCV for image processing and `cvzone` (powered by MediaPipe) for highly accurate, fast face detection.

## Features

- **Real-Time Detection:** Captures live video feed from the default webcam.
- **High-Confidence Tracking:** Uses a 75% minimum confidence threshold to ensure accurate face bounding boxes and minimize false positives.
- **Dynamic Blurring:** Automatically calculates the face bounding box, crops the region, applies a heavy box blur (`35x35` kernel), and merges it back into the live video feed.
- **Edge-Case Handling:** Includes boundary checks to prevent crashes when a face moves partially off-screen.
- **Graceful Exit:** Safely closes the application and releases camera resources with a simple keystroke.

## Prerequisites

Before running the script, ensure Python is installed on your system. You also need the following libraries:

### Required Libraries

- `opencv-python` (`cv2`)
- `cvzone`
- `mediapipe` (backend required by `cvzone`'s `FaceDetectionModule`)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. Install dependencies:
   ```bash
   pip install opencv-python cvzone mediapipe
   ```

## Usage

Run the script from your terminal:

```bash
python main.py
```

> Replace `main.py` with the actual name of your Python file.

A window named **Face Blur** will open and display your webcam feed with detected faces blurred out.

To exit the application, press **`q`** while the video window is active. The script will safely release the webcam and close all OpenCV windows.

## How It Works

1. **Initialization:** Starts the webcam with `cv.VideoCapture(0)` and initializes the `FaceDetector`.
2. **Frame Extraction:** Reads the video feed frame by frame.
3. **Face Localization:** `detector.findFaces` locates faces and returns bounding box coordinates (`x, y, w, h`).
4. **Anonymization:**
   - Extracts the face region of interest (ROI).
   - Applies `cv.blur` to the cropped face.
   - Pastes the blurred ROI back into the original frame at the same coordinates.
5. **Display & Exit:** Shows the modified frame continuously and checks for `q` key press to break the loop, release `cap`, and destroy OpenCV windows.
