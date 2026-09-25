import cv2
import os

IMAGE_PATH = r"dataset\test\images\test3_jpg.rf.2910fbdc32f43243d537aab6d0cf9be1.jpg"
LABEL_PATH = r"dataset\test\labels\test3_jpg.rf.2910fbdc32f43243d537aab6d0cf9be1.txt"

image = cv2.imread(IMAGE_PATH)

if image is None:
    print("ERROR: Image could not be loaded.")
    exit()

height, width = image.shape[:2]

with open(LABEL_PATH, "r") as file:
    lines = file.readlines()

for line in lines:

    parts = line.strip().split()

    if len(parts) != 5:
        continue

    class_id = int(parts[0])

    x_center = float(parts[1]) * width
    y_center = float(parts[2]) * height
    box_width = float(parts[3]) * width
    box_height = float(parts[4]) * height

    x1 = int(x_center - box_width / 2)
    y1 = int(y_center - box_height / 2)
    x2 = int(x_center + box_width / 2)
    y2 = int(y_center + box_height / 2)

    if class_id == 0:
        label = "CLASS 0"
        color = (255, 0, 0)
    else:
        label = "CLASS 1"
        color = (0, 0, 255)

    cv2.rectangle(
        image,
        (x1, y1),
        (x2, y2),
        color,
        3
    )

    cv2.putText(
        image,
        label,
        (x1, max(y1 - 10, 20)),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        color,
        2
    )

output = r"screenshots\class_inspection.jpg"

cv2.imwrite(output, image)

print("Inspection image created:")
print(output)

cv2.imshow("Class Inspection", image)

print("Press any key to close.")
cv2.waitKey(0)
cv2.destroyAllWindows()