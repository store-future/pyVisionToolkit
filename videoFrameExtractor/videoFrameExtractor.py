import cv2
import numpy as np
import matplotlib.pyplot as plt


def extract_and_display_frame(video_path, frame_number):
    """
    Extract and display a specific frame from a video file.

    Parameters:
    video_path (str): Path to the video file.
    frame_number (int): Frame number to extract (0-based index).
    """
    
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if the video was successfully opened
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Get the total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Total number of frames in the video: {total_frames}")
    print(f"Extracted frame No from this video: {frame_number}")

    # Ensure the frame number is within the valid range
    if frame_number >= total_frames or frame_number < 0:
        print("Error: Frame number out of range.")
        return

    # Set the video position to the desired frame
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    
    # Read the frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        return

    # Resize the frame for display
    frame = cv2.resize(frame, (700, 400), interpolation=cv2.INTER_LINEAR)

    # Display the frame
    cv2.imshow('Frame', frame)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Release the video capture object
    cap.release()

# Example usage:
video_path = 'C:/Users/DELL/Desktop/projects/machine_learning/lanDetection/road.mp4'
frame_number = 200  # Change this to the frame you want to extract
extract_and_display_frame(video_path, frame_number)
