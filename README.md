# DryFire-Trainer
 real time computer vision system built with Python and OpenCV that transforms any webcam into a dry fire training platform. It utilizes high precision HSV masking to track laser impacts with pixel accuracy. A lightweight, open-source alternative to commercial laser dry fire trainers

1. Prepare your Target: Tape a high-contrast target to a wall.
2. Position your Webcam: Align the camera so the target is clearly visible and centered in the frame.
3. Run the tracker:
   python main.py
4. Ensure your room lighting is consistent.
5. Upload Target: Once ready press s to capture target image.
6. Every time the laser hits the target, a red dot will be drawn and saved to targetImage.png
7. Exit: Press q to quit the application and save your final shot group.

Note for Users: If the laser isn't being detected, check your lighting. Intense overhead glare can sometimes "wash out" the laser's red signature. The system uses a dual masking approach to find the saturated white core of the laser, making it more robust than simple color filters.

git clone https://github.com/yourusername/DryFire-Shot-Tracker.git
    cd DryFire-Shot-Tracker
    ```
  
  
    This isolates the project dependencies.
    ```bash
    python -m venv venv
    ```
  
  
    * **Windows:** `venv\Scripts\activate`
    * **Mac/Linux:** `source venv/bin/activate`
  
  
    Install the core computer vision libraries:
    ```bash
    pip install opencv-python numpy
    ```
