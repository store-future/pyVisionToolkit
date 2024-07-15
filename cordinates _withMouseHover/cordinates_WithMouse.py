import cv2

# Global variables to store mouse coordinates
current_x, current_y = 0, 0

def mouse_event_handler(event, x, y, flags, param):
    """
    Callback function to handle mouse events.

    Args:
    event (int): The type of mouse event.
    x (int): The x-coordinate of the mouse pointer.
    y (int): The y-coordinate of the mouse pointer.
    flags (int): Any relevant flags passed by OpenCV.
    param (Any): Any extra parameters supplied by OpenCV.
    """
    global current_x, current_y
    if event == cv2.EVENT_MOUSEMOVE:
        current_x, current_y = x, y

def display_frame_with_mouse_events():
    """
    Function to capture video from the webcam and display mouse coordinates.
    """
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video capture.")
        return

    # Create a named window before setting the mouse callback
    cv2.namedWindow("Frame")
    cv2.setMouseCallback("Frame", mouse_event_handler)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Display the coordinates on the frame
        cv2.putText(frame, f"Coordinates: ({current_x}, {current_y})", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        # Display the frame
        cv2.imshow("Frame", frame)

        # Break the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Run the function to display the frame with coordinates
display_frame_with_mouse_events()
