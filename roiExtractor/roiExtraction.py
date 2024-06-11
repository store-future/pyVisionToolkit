import cv2
import numpy as np


def capture_and_process_video(address_of_camera):
    # Initialize the camera
    cap = cv2.VideoCapture(address_of_camera)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Camera could not be opened.")
        return

    try:
        # Run indefinitely until 'q' is pressed
        while True:
            ret, frame = cap.read()
            print(ret)
            # Check if frame is captured successfully
            if not ret:
                print("Error: No frame captured.")
                break

            # Resize and flip the frame
            frame = cv2.resize(frame, (720, 540))
            frame = cv2.flip(frame, 1)

            # Define the coordinates and dimensions for the ROI
            x_cord, y_cord, width, height = 300, 200, 200, 150

            # Extract the ROI
            roi = frame[y_cord:y_cord+height, x_cord:x_cord+width].copy()
            print("ROI Shape : ", roi.shape)

            # Draw a rectangle around the ROI
            cv2.rectangle(frame, (x_cord, y_cord), (x_cord + width, y_cord + height), (0, 0, 0), 5)

            # Display the original image and the ROI
            cv2.imshow('Processed Image', frame)
            cv2.imshow('Extracted ROI Image', roi)

            # Break the loop when 'q' is pressed
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Release the camera and close all OpenCV windows
        cap.release()
        cv2.destroyAllWindows()


address_of_camera = 0               # enter the address of camera object            
# Call the function to start the process
capture_and_process_video(address_of_camera)
