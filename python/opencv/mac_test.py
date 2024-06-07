import cv2
import time
import os

# This is for mac build-in camera

# Specify the directory to store the image
folder_path = 'cap_img'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Initialize the camera
cap = cv2.VideoCapture(1)  # 0 is usually the built-in camera on a Mac

if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Total countdown duration in seconds
countdown = 3

# Show live camera feed and countdown
start_time = time.time()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Calculate remaining time
    elapsed_time = time.time() - start_time
    remaining_time = countdown - int(elapsed_time)
    if remaining_time < 0:
        break

    # Display countdown on the frame
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, f'Capturing in {remaining_time}...', (50, 50), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Determine the dimensions of the video feed
    height, width = frame.shape[:2]

    # Draw a centered rectangle (suggestion square), now 500x500 pixels
    rectangle_size = 200  # Half of 500 pixels
    top_left = (width // 2 - rectangle_size, height // 2 - rectangle_size)
    bottom_right = (width // 2 + rectangle_size, height // 2 + rectangle_size)
    cv2.rectangle(frame, top_left, bottom_right, (255, 0, 0), 3)

    cv2.imshow('Camera Feed', frame)

    # Check if the user has pressed the 'q' key to exit earlier
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Capture the final frame for saving
ret, frame = cap.read()
if ret:
    # Define the full path for the image
    image_path = os.path.join(folder_path, 'captured_image.jpg')
    # Save the captured image
    cv2.imwrite(image_path, frame)
    print(f"Image saved to {image_path}")
else:
    print("Failed to capture image")

# Release the capture and close any open windows
cap.release()
cv2.destroyAllWindows()