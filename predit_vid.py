import cv2
import numpy as np
from ultralytics import YOLO
from tqdm import tqdm

# Load the trained model
model = YOLO('litter.pt')

# Open the video file
video_path = './test1.mp4'
cap = cv2.VideoCapture(video_path)

# Get the video's frame rate, dimensions, and total frame count
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Create a VideoWriter object to save the annotated video
output_path = 'output_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# Create a tqdm progress bar
pbar = tqdm(total=total_frames)

while True:
    # Read a frame from the video
    ret, frame = cap.read()
    if not ret:
        break

    # Perform inference on the frame
    results = model.predict(frame, device='cpu', conf=0.5)

    for result in results:
        boxes = result.boxes
        conf_scores = boxes.conf.cpu().numpy()  # Convert tensor to numpy array

        for i in range(len(boxes)):
            x1, y1, x2, y2 = boxes.xyxy[i].int().tolist()
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)  # Change color to red
            cv2.putText(frame, f'Confidence: {conf_scores[i]:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)  # Change color to red

    # Write the annotated frame to the output video
    out.write(frame)

    # Update the progress bar
    pbar.update(1)

# Close the progress bar
pbar.close()

# Release the video capture and writer objects
cap.release()
out.release()
print('Done')