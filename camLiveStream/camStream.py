import cv2

def capture_and_process_video():
    # Initialize the camera
    cap = cv2.VideoCapture(0)       # change indexing according to hardware

    # Set frame width and height
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

    if not cap.isOpened():
        print("Error: Camera could not be opened.")
        return

    try:
        while True:
            ret, frame = cap.read()

            if not ret:
                print("Error: No frame captured.")
                break


            # Flip the frame horizontally
            frame = cv2.flip(frame, 1)

            # Show the frame
            cv2.imshow('frame', frame)


            # Break the loop if 'q' is pressed
            if cv2.waitKey(200) & 0xFF == ord('q'):
                break
    finally:
        # Release the camera and close all windows
        cap.release()
        cv2.destroyAllWindows()

# Call the function to start the process
capture_and_process_video()
