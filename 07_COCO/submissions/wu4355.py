import json

import cv2
import numpy as np
from pycocotools import mask as mask
from skimage import measure

index = 1

with open("annotations.txt", "r") as f:
    line = f.readline()
    line = f.readline()
    images = []
    anns = []
    temp_data = temp_data1 = {}
    json_data = {
        "images": [],
    }
    while line:

        line_array = line.split(",")
        line_array[-1] = line_array[-1].strip()
        file_name = line_array[0]
        file_id = int(file_name[3:-4])
        image_id = line_array[1]
        category_id = int(line_array[2])
        mask_name = line_array[3]
        image = cv2.imread(file_name, 0)
        mk = cv2.imread(mask_name, cv2.IMREAD_GRAYSCALE)
        mk = mk.clip(max=1)
        ground_truth_binary_mask = np.array(mk, dtype=np.uint8)

        fortran_mask = np.asfortranarray(ground_truth_binary_mask)
        encoded_ground_truth = mask.encode(fortran_mask)
        ground_truth_area = mask.area(encoded_ground_truth)
        ground_truth_bounding_box = mask.toBbox(encoded_ground_truth)
        contours = measure.find_contours(ground_truth_binary_mask, 0.5)
        annotation = {
            "segmentation": [],
            "area": float(ground_truth_area.tolist()),
            "iscrowd": 0,
            "image_id": file_id,
            "bbox": ground_truth_bounding_box.tolist(),
            "category_id": category_id,
            "id": index,
        }

        image = {
            "file_name": file_name,
            "height": image.shape[0],
            "width": image.shape[1],
            "id": file_id,
        }
        if image not in images:
            images.append(image)
        # get segmentation
        polygons = []
        for contour in contours:

            contour = np.flip(contour, axis=1)
            segmentation = contour.ravel().tolist()
            annotation["segmentation"].append(segmentation)

        anns.append(annotation)

        line = f.readline()
        index += 1
    json_data = {"images": images, "annotations": anns}
    with open("instances_val2017.json", "r") as f:
        temp_data = json.load(f)
        category = {"categories": temp_data["categories"]}
        json_data.update(category)
    json_data = json.dumps(json_data, indent=4, sort_keys=True)
with open("wu4355.json", "w") as outfile:
    outfile.write(json_data)
