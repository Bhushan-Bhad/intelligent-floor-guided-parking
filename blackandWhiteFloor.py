import cv2
import numpy as np

def convert_video_floor_to_bw(input_video_path, output_video_path):
    # Open the video file
    cap = cv2.VideoCapture(input_video_path)

    # Get the video's frames per second (fps) and frame dimensions
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    center_width=frame_width/2
    center_height=frame_height/2

    # Create VideoWriter object to save the processed video
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

    while True:
        # Read a frame from the video
        ret, frame = cap.read()

        # If the frame is not read, break the loop
        if not ret:
            break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply thresholding to convert the frame to black and white
        _, binary_frame = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

        # Invert the binary frame to make the floor white
        inverted_frame = cv2.bitwise_not(binary_frame)

        # Convert the original frame to a binary mask where the floor is black
        floor_mask = cv2.bitwise_not(binary_frame)

        # Keep the original color of the lines where the floor is black
        result_frame = cv2.bitwise_and(frame, frame, mask=floor_mask)

        # Combine the original color lines with the white floor
        result_frame = cv2.bitwise_or(result_frame, cv2.cvtColor(inverted_frame, cv2.COLOR_GRAY2BGR))

        edges = cv2.Canny(result_frame, 50, 150)

        # Use Hough Line Transform to detect lines in the image
        lines = cv2.HoughLines(edges, 1, np.pi / 180, threshold=100)

        # Draw lines on the original image
        if lines is not None:
            for line in lines:
                rho, theta = line[0]
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a * rho
                y0 = b * rho
                x1 = int(x0 + 1000 * (-b))
                y1 = int(y0 + 1000 * (a))
                x2 = int(x0 - 1000 * (-b))
                y2 = int(y0 - 1000 * (a))
                cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

        # Write the processed frame to the output video
        out.write(result_frame)

        # Display the processed frame
        cv2.imshow('Original Color Lines with Black and White Floor', result_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the VideoCapture and VideoWriter objects
    cap.release()
    out.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()


# Function to process each frame of the video
def process_frame(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise and help in edge detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Use Canny edge detector to find edges in the image
    edges = cv2.Canny(blurred, 50, 150)

    # Use Hough Line Transform to detect lines in the image
    lines = cv2.HoughLines(edges, 1, np.pi / 180, threshold=100)

    # Draw lines on the original image
    if lines is not None:
        for line in lines:
            rho, theta = line[0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))
            cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

    return frame
# Replace 'input_video.mp4' and 'output_video.avi' with your video file paths
convert_video_floor_to_bw('C:\\Users\\Bhushan Bhad\\Desktop\\SofDcar\\red-light-green-light\\video.mp4', 'output_video.avi')
