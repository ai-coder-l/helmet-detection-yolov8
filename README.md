## Helmet-Detection

This project aims to detect helmets in images and videos using the YOLOv8 object detection algorithm. It provides a script that takes a folder path as input, detects helmets in all the images and videos within that folder, and saves annotated images and a CSV file with detection information in an output folder.

<img src="https://github.com/meryemsakin/helmet-detection/blob/main/allresults.jpeg" width="900" height="500">

## Project Objective:

The objective of this project is to detect helmets in images and videos using the YOLOv8 object detection algorithm. The project workflow involves loading the pre-trained YOLOv8 model, resizing input frames, passing them through the model for object detection, visualizing the detections, and storing the results in annotated images and a CSV file.

```
python main.py <folder-path-containing-images>
```

## Tools Used:

1. Python Programming Language
2. OpenCV (Open Source Computer Vision Library) - to work with images and videos
3. YOLOv8 (You Only Look Once) Model - to detect objects in images and videos
4. Supervision (Python Package) - to visualize object detection and annotations
5. Ultralytics (Python Package) - to use the YOLO model

## Project Workflow:

1. Load the pre-trained YOLOv8 model for helmet detection.
2. Read input images or videos and resize the frames to the required size.
3. Pass the resized frames through the YOLOv8 model to obtain the detected objects and their positions.
4. Use the Supervision package to visualize the detections on the images.
5. Store the resulting annotated images in a separate folder.
6. Extract the labels of the detections from the YOLOv8 results.
7. Evaluate the detections and generate a confusion matrix.
8. Calculate accuracy and loss metrics and plot them using graphs.
9. Store the generated graphs, along with the CSV file containing detection information, in the output folder.

## Metrics

![Accuracy](https://github.com/meryemsakin/helmet-detection/blob/main/graph.png)

## Confusion Matrix
The confusion matrix provides a comprehensive evaluation of the model's performance. Here is the confusion matrix for the helmet detection model:

![cm](https://github.com/meryemsakin/helmet-detection/blob/main/cmatrix.png)

## Limitations and Potential Improvements:

1. The model may not be accurate in all situations, and there may be false positives and false negatives. One way to improve the accuracy is to fine-tune the model on a larger and more diverse dataset.
2. The current implementation only detects helmets, but it could be extended to detect other safety equipment such as safety glasses or gloves.
3. The current implementation only works with images and videos, but it could be extended to work with live camera feeds.
    
    

## Conclusion:

In conclusion, your project involved detecting helmets in images and videos using a YOLO model. You used Python, OpenCV, YOLO, Supervision, and Ultralytics to implement the solution. The project workflow involved loading the YOLO model, reading the input images or video frames, passing them through the model, visualizing the detections, checking whether each person is wearing a helmet or not, and storing the results in a CSV file. There are potential improvements that could be made to the project, but overall it provides a good foundation for detecting safety equipment in images and videos.# helmet-detection


## Results

<img src="https://github.com/meryemsakin/helmet-detection/blob/main/Result/floor_1/images/hard_hat_workers42.png" width="500" height="500">

<img src="https://github.com/meryemsakin/helmet-detection/blob/main/Result/floor_1/images/image_6.jpg" width="500" height="500">
