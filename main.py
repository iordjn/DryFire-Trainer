import cv2 as cv
import numpy as np


# Enable a debug window that shows the detection mask
debug_mode = input("would you like to see debug frame? (y for yes, othewise click any other button): ")

# Open the default webcam (camera index 0)
cam = cv.VideoCapture(0)

# Capture an initial frame to verify the camera works
ret, frame = cam.read()
if not ret:
    print("Failed to capture initial frame.")
    cam.release()
    cv.destroyAllWindows()
    raise SystemExit(1)

# HSV COLOR RANGES -------------------------------------------------------
lower_red = np.array([160, 100, 100])
upper_red = np.array([180, 255, 255])

lower_white = np.array([0, 0, 240])
upper_white = np.array([180, 50, 255])

# LOAD OR CREATE TARGET IMAGE --------------------------------------------
target_img = cv.imread("targetImage.png")
if target_img is None:
    # Use the first camera frame as the base target image.
    target_img = frame.copy()
    cv.imwrite("targetImage.png", target_img)

print("Press 's' to update target image, 'q' to quit.")

# MAIN LOOP --------------------------------------------------------------
while True:
    ret, frame = cam.read()
    if ret:

        red_dot = None
        laser_radius = 0
        
        # convert frame from Blue, Green, Red to Hue, Saturation, and Value
        hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        # CREATE COLOR MASKS -------------------------------------------
        mask_red = cv.inRange(hsv_frame, lower_red, upper_red)
        mask_white = cv.inRange(hsv_frame, lower_white, upper_white)
        
        full_mask = cv.bitwise_or(mask_red, mask_white)

        # FIND LASER CONTOURS--------------------------------------------
        contours, _ = cv.findContours(full_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        if contours:
            # Use the largest contour as the most likely laser
            c = max(contours, key=cv.contourArea)
            # Create a circle that encloses the contour
            ((x, y), radius) = cv.minEnclosingCircle(c)
            # Calculate contour moments for center position
            M = cv.moments(c)

             # Calculate contour moments for center position
            if M["m00"] != 0:
                # Compute contour center
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])

                red_dot = (cX, cY)

                 # 5. Draw it on your color frame
                cv.circle(frame, (cX, cY), 5, (0, 255, 0), -1) # Green dot at center
                print(f"Shot detected at: {cX}, {cY}")

        #MARKS WHERE LASER HIT--------------------------------------------
        if red_dot is not None:
            #Automatically mark each detected red dot onto the target image.
            cv.circle(target_img, red_dot, max(laser_radius, 5), (0, 0, 255), -1)
            cv.imwrite("targetImage.png", target_img)
            red_dot = None

        # DISPLAY WINDOWS-------------------------------------------------
        # Optional debug window showing the mask used for laser detection
        if debug_mode == 'y':
            cv.imshow("debug video", full_mask)
        cv.imshow("LIVE VIDEO", frame)
        cv.imshow("TARGET", target_img)
        
        # KEYBOARD CONTROLS-----------------------------------------------
        key = cv.waitKey(1)
        
        # Quit application
        if key == ord("q"):
            break
        # Capture a new target image
        elif key == ord("s"):
            # Refresh the base target image from the latest frame.
            target_img = frame.copy()
            # Save image as targetImage.png
            cv.imwrite("targetImage.png", target_img)
            print("Target image updated from current frame.")     

    else:
        print("Failed to capture image.")

# CLEANUP / END PROGRAM ---------------------------------------------------
# Release webcam resources 
cam.release() 
# Close all OpenCV windows 
cv.destroyAllWindows()
