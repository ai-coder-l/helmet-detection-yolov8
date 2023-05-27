import cv2
import os
import csv


def show_file_size(file):
    """
    This function takes a file path as input and prints its size in megabytes.

    Args:
        - file (str): The path of the file whose size is to be calculated.

    Returns:
        None
    """

    # Get the size of the file in bytes
    file_size = os.path.getsize(file)
    # Convert the size to megabytes and round to two decimal places
    file_size_mb = round(file_size / 1024, 2)

    # Print the file size in megabytes
    print("File size is " + str(file_size_mb) + "MB")


def imageLoader(folder_path):
    """
    This function takes a folder path as input and returns a list of all image paths within the folder,
    along with their names.

    Args:
        - folder_path (str): The path of the folder containing the images.

    Returns:
        Tuple: A tuple containing two lists:
            1. A list of all image paths in the folder.
            2. A list of all image names in the folder.
    """
    # Get a list of all items in the folder
    items = os.listdir(folder_path)
    print(f"[!] Found {len(items)} images [!]")

    images_path_list = []
    # Loop through each item in the folder
    for image in items:
        # Get the path of the item
        item_path = os.path.join(folder_path, image)
        images_path_list.append(item_path)

    # Return a tuple containing the list of image paths and the list of image names
    return (images_path_list, items)


def saveResultCSV(result, output_folder_name, csv_file_name):
    """
    This function takes a list of results, an output folder name and a CSV file name as input, and saves the
    results to a CSV file in the specified output folder.

    Args:
        - result (list): A list of lists, with each inner list containing the image name, image location, and status.
        - output_folder_name (str): The name of the folder where the CSV file will be saved.
        - csv_file_name (str): The name of the CSV file.

    Returns:
        None
    """

    # Combine the output folder name and CSV file name to form the full path to the CSV file
    csv_path = os.path.join(output_folder_name, csv_file_name + ".csv")
    with open(csv_path, "w") as f1:
        writer = csv.writer(f1, delimiter=",")  # lineterminator='\n',
        writer.writerow(["Image Name", "Image Location", "Status"])
        # Loop over the results and write each row to the CSV file
        for i in range(len(result)):
            row = result[i]
            writer.writerow(row)


def checkHeads(
    labels,
    image_name_list,
    image_path_list,
    image,
    csv_result_msg_final,
    i,
    image_storage_folder,
):
    """
    This function checks if the given list of labels contains the word "head". If it does, the function saves the
    corresponding image to disk and adds a row to the result list indicating that no helmet was detected.

    Args:
        - labels (list): A list of labels detected in the image.
        - image_name_list (list): A list of all image names in the folder.
        - image_path_list (list): A list of all image paths in the folder.
        - image (numpy.ndarray): The image array.
        - csv_result_msg_final (list): A list containing the results.
        - i (int): The index of the current image.
        - image_storage_folder (str): The path of the folder where the images will be saved.

    Returns:
        list: A list containing the updated results.
    """

    # Looping through the results of detections
    if "head" in labels:
        print("head found")
        # Getting the image name and location
        image_name = f"{image_name_list[i]}"
        image_loc = os.path.join(f"{image_storage_folder}/", image_name)
        # cv2.imwrite(image_loc, image, [cv2.IMWRITE_JPEG_QUALITY, 1])
        cv2.imwrite(image_loc, image)

        # print("After Compression")
        # show_file_size(image_loc)

        img_loc = image_path_list[i]
        message = "No Helmet"

        # Generating the message to store in csv file
        csv_result_msg_final.append([image_name, img_loc, message])

    return csv_result_msg_final
