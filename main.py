import cv2
import supervision as sv
import os
from datetime import datetime
import sys

from utils.helperFunctions import *
from ultralytics import YOLO


# source = "../RESOURCES\helmet.mp4"
# Custom trained Model we are using for helmet detection
model = YOLO("/Users/meryem/Downloads/Safety-Helmet-Detection-yoloV8-main/models/hemletYoloV8_100epochs.pt")

# frame width and height
frame_wid = 640
frame_hyt = 480


def processImages(image_path_list, image_name_list, image_storage_folder):
    """
    Process images in the given list, detect helmets using a pre-trained YOLOv5 model,
    and store the annotated images and detection results in the output folder.

    Args:
        - image_path_list: A list of image paths to be processed.
        - image_name_list: A list of image names corresponding to the images in image_path_list.
        - image_storage_folder: The path to the output folder where annotated images and detection results are to be stored.

    Returns:
        - csv_result_msg_final: A list of messages containing the detection results for each image in the input list.
    """

    box_annotator = sv.BoxAnnotator(thickness=2, text_thickness=1, text_scale=1)

    csv_result_msg_final = []

    for i in range(len(image_path_list)):
        frame = cv2.imread(image_path_list[i])

        # print("Before Compression")
        # show_file_size(image_path_list[i])

        # Resize the image to a fixed size
        image = cv2.resize(frame, (frame_wid, frame_hyt))

        # Use the pre-trained YOLOv5 model to detect helmets
        results = model(image)[0]
        detections = sv.Detections.from_yolov8(results)
        labels = [f"{model.model.names[class_id]}" for _, _, class_id, _ in detections]

        # Annotate the image with bounding boxes around the detected helmets
        image = box_annotator.annotate(
            scene=image,
            detections=detections
            # labels=labels
        )

        # Check if the detected helmets are properly worn, and add the detection result to the output list
        csv_result_msg_final = checkHeads(
            labels,
            image_name_list,
            image_path_list,
            image,
            csv_result_msg_final,
            i,
            image_storage_folder,
        )

        # Show the annotated image
        # cv2.imshow("Helmet Detection", image)
        # if cv2.waitKey(1) == 27:
        #     break

    return csv_result_msg_final


if __name__ == "__main__":
    """
    Main function for the helmet detection program. Parses command line arguments to determine
    the input folder containing images to be processed, and the output folder where annotated
    images and detection results are to be stored. Calls the processImages function to perform
    helmet detection on the input images.
    """

    try:
        # Parse command line arguments to determine input and output folders
        # It wont matter if your path has spaces, this will handle that
        inter_path = sys.argv[1:]
        real_path = ""
        for path in inter_path:
            real_path = real_path+path+" "

        folder_path = real_path.strip()
        # folder_path = str(sys.argv[1])
        split_list = folder_path.split("\\")
        output_folder_name = os.path.join("Result", split_list[-1])
        os.makedirs(output_folder_name)

        image_storage_folder = os.path.join(output_folder_name, "images")
        os.makedirs(image_storage_folder)

    except Exception as error:
        print("[!] folder already exists [!]")

    try:
        # Load images from input folder and perform helmet detection
        image_path_list, image_name_list = imageLoader(folder_path)
        result = processImages(image_path_list, image_name_list, image_storage_folder)

        # Save detection results to a CSV file
        saveResultCSV(result, output_folder_name, csv_file_name=split_list[-1])

        print(
            f"Images saved to '{image_storage_folder}' \nCSV file generate saved to '{output_folder_name}'"
        )

    except Exception as error:
        # Clean up output folder if an error occurs
        print("[!] Some error occured during processing [!]")
        os.rmdir(image_storage_folder)
        os.rmdir(output_folder_name)
