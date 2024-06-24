import cv2
import os

# Directory where the captured images will be saved
output_dir = 'C:/Users/DELL/Desktop/trainingImagesGenerator/resource'
# Name of the hand pose (used to name the output folder and files)
pose_name = 'stop'
# Number of images to capture
num_images = 50

def generate_training_images(output_dir, pose_name, num_images):
    """
    Captures images from the webcam and saves them in a specified directory.

    Args:
    output_dir (str): Directory where the images will be saved.
    pose_name (str): Name of the hand pose for the folder and filenames.
    num_images (int): Number of images to capture.
    """
    
    # Create the full output directory path
    full_output_dir = os.path.join(output_dir, pose_name)
    os.makedirs(full_output_dir, exist_ok=True)  # Ensure the output directory exists

    cap = cv2.VideoCapture(0)  # Open the primary camera
    
    if not cap.isOpened():
        print("Error: Camera could not be opened.")
        return

    count = 0
    while count < num_images:
        ret, frame = cap.read()  # Capture frame-by-frame
        if not ret:
            print("Error: Frame could not be captured.")
            break

        cv2.imshow('Capture Hand Poses', frame)  # Display the resulting frame
        key = cv2.waitKey(1)  # Wait 1ms for a key event

        if key == ord('s'):  # Press 's' to save the image
            img_name = os.path.join(full_output_dir, f"{pose_name}_{count}.jpg")       # if want to use zero padding use this = "{pose_name}_{count:04d}.jpg"

            cv2.imwrite(img_name, frame)  # Save the captured image
            print(f"Image saved: {img_name}")
            count += 1
        elif key == ord('q'):  # Press 'q' to quit the capture
            break

    cap.release()  # When everything done, release the capture
    cv2.destroyAllWindows()  # Close all OpenCV windows

# Uncomment the line below to run the function with specified parameters
generate_training_images(output_dir, pose_name, num_images)
