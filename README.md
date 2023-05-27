### Project Objective:

<img src="https://github.com/meryemsakin/helmet-detection/blob/main/allresults.jpeg" width="500" height="300">

The project involved creating a script for detecting helmets in images and videos using the YOLOv8 object detection algorithm. The script was designed to take a folder path as input and detect helmets in all the images and videos contained within that folder. The script then saved the annotated images and a CSV file containing information about the detections in a separate output folder.

```
python main.py <folder-path-containing-images>
```

### Tools Used:

1. Python Programming Language
2. OpenCV (Open Source Computer Vision Library) - to work with images and videos
3. YOLOv8 (You Only Look Once) Model - to detect objects in images and videos
4. Supervision (Python Package) - to visualize object detection and annotations
5. Ultralytics (Python Package) - to use the YOLO model

### Project Workflow:

1. Load the YOLO model that has been trained to detect helmets.
2. Read the input video or images and resize the frames to the required size.
3. Pass the resized frames through the YOLO model to get the detected objects and their positions.
4. Use the Supervision package to visualize the detections on the image.
5. Store the resulting images with the annotations in a folder.
6. Extract the labels of the detections from the YOLO results.
7. Check whether each person in the image is wearing a helmet or not, and store the results in a CSV file.
8. Store the CSV file in a folder along with the images.


### Limitations and Potential Improvements:

1. The model may not be accurate in all situations, and there may be false positives and false negatives. One way to improve the accuracy is to fine-tune the model on a larger and more diverse dataset.
2. The current implementation only detects helmets, but it could be extended to detect other safety equipment such as safety glasses or gloves.
3. The current implementation only works with images and videos, but it could be extended to work with live camera feeds.
    
    

### Conclusion:

In conclusion, your project involved detecting helmets in images and videos using a YOLO model. You used Python, OpenCV, YOLO, Supervision, and Ultralytics to implement the solution. The project workflow involved loading the YOLO model, reading the input images or video frames, passing them through the model, visualizing the detections, checking whether each person is wearing a helmet or not, and storing the results in a CSV file. There are potential improvements that could be made to the project, but overall it provides a good foundation for detecting safety equipment in images and videos.# helmet-detection


## Results

<img src="https://github.com/meryemsakin/helmet-detection/blob/main/Result/floor_1/images/hard_hat_workers42.png" width="500" height="500">

<img src="https://github.com/meryemsakin/helmet-detection/blob/main/Result/floor_1/images/image_6.jpg" width="500" height="500">
