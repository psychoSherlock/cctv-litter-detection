import cv2
import numpy as np
from ultralytics import YOLO

# FILEPATH: /home/psychosherlock/Desktop/MITS/IEDC/wasteProject/predit.py
# Load the trained model
model = YOLO('litter.pt')

# ask the image from the user
image_path = input("Enter the image path: ")
# Perform inference on an image
results = model.predict(image_path, device='cpu')  # CPU is faster in my case

img = cv2.imread(image_path)

for result in results:
    boxes = result.boxes
    conf_scores = boxes.conf.cpu().numpy()  # Convert tensor to numpy array

    for i in range(len(boxes)):
        x1, y1, x2, y2 = boxes.xyxy[i].int().tolist()
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)  # Change color to red
        cv2.putText(img, f'Confidence: {conf_scores[i]:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)  # Change color to red

# cv2.imshow('Image with Boxes', img)
cv2.imwrite("output_" + image_path, img)
