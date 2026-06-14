# DryFire-Trainer

A real-time computer vision dry fire training system built with **Python** and **OpenCV**. DryFire-Trainer turns any webcam into a laser shot tracking platform by detecting laser impacts and marking them directly on a captured target image.

Unlike expensive commercial dry fire systems, this project is lightweight, open source, and uses HSV color masking to detect laser hits with high accuracy.

## Features

* Real-time laser shot detection using a webcam
* Automatic shot marking on a target image
* Live camera feed and target display
* Optional debug mode for mask visualization
* Save and update target images at any time
* Simple setup with Python and OpenCV

---

## How It Works

1. Place a high-contrast target on a wall.
2. Position your webcam so the entire target is visible and centered in the camera frame.
3. Launch the application.
4. Capture a screenshot of your target by pressing **S**.
5. Aim your laser training device at the target.
6. Each detected laser hit is automatically marked with a red dot on the saved target image.
7. Continue shooting to build a shot group.
8. Press **Q** to quit and save your final results.

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/iordjn/DryFire-Trainer.git
cd DryFire-Trainer
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install opencv-python numpy
```

---

## Running the Application

Start the program:

```bash
python main.py
```

When prompted:

```text
would you like to see debug frame? (y for yes, otherwise click any other button):
```

Enter:

* `y` to display the detection mask used for laser tracking.
* Any other key to run normally.

---

## Controls

| Key   | Action                                                                                                                       |
| ----- | ---------------------------------------------------------------------------------------------------------------------------- |
| **S** | Capture and save a new target screenshot from the current camera view. This becomes the image where future shots are marked. |
| **Q** | Quit the application and save the final shot group.                                                                          |

---

## Target Image Behavior

When the application starts:

* If `targetImage.png` already exists, it is loaded automatically.
* If no target image exists, the first webcam frame is saved as `targetImage.png`.

Pressing **S** at any time:

1. Takes a screenshot of the current webcam frame.
2. Replaces the existing target image.
3. Saves it as `targetImage.png`.
4. Clears previous shot markings by creating a fresh target image.

---

## Shot Detection

The system detects laser impacts using a combination of:

* Red HSV color masking
* Bright white core detection

This dual-mask approach helps improve reliability compared to simple red color filtering alone.

When a laser hit is detected:

* The impact location is calculated.
* A marker is drawn on the live feed.
* A red dot is permanently added to `targetImage.png`.
* The updated target image is automatically saved.

---

## Troubleshooting

### Laser Not Being Detected?

Try the following:

* Reduce glare from overhead lighting.
* Avoid direct sunlight on the target.
* Ensure the laser is clearly visible to the webcam.
* Increase contrast between the target and background.
* Run with debug mode enabled (`y`) to view the detection mask.

### Webcam Not Opening?

Make sure:

* No other application is using the webcam.
* Your webcam permissions are enabled.
* The correct camera is connected and recognized by your operating system.

---

## Requirements

* Python 3.8+
* OpenCV
* NumPy
* Webcam
* Laser training device

---

## Future Improvements

* Adjustable detection sensitivity
* Multiple target support
* Shot statistics and scoring
* Session recording
* Automatic target calibration

## License

Open source and free to modify for personal and educational use.
