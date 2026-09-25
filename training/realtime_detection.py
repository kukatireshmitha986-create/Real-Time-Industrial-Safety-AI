import cv2
from ultralytics import YOLO
from datetime import datetime
import os
import time

from database import create_database, log_violation


# ============================================================
# AI-POWERED REAL-TIME INDUSTRIAL SAFETY MONITORING SYSTEM
# ============================================================

MODEL_PATH = r"runs\detect\models\industrial_safety_helmet\weights\best.pt"


# ============================================================
# CREATE REQUIRED FOLDERS
# ============================================================

os.makedirs("screenshots", exist_ok=True)
os.makedirs("detections", exist_ok=True)


# ============================================================
# INITIALIZE SQLITE DATABASE
# ============================================================

create_database()


# ============================================================
# LOAD TRAINED YOLO MODEL
# ============================================================

print()
print("Loading trained YOLO model...")

model = YOLO(MODEL_PATH)

print("Model loaded successfully.")
print("Class 0 = Head")
print("Class 1 = Helmet")


# ============================================================
# OPEN WEBCAM
# ============================================================

cap = cv2.VideoCapture(0)

if not cap.isOpened():

    print()
    print("ERROR: Could not open webcam.")
    print("Please check your camera.")

    exit()


print()
print("Webcam started successfully.")
print("Press Q to quit.")


# ============================================================
# SCREENSHOT CONTROL
# ============================================================

last_screenshot_time = 0

screenshot_delay = 5


# ============================================================
# CONFIDENCE THRESHOLD
# ============================================================

CONFIDENCE = 0.40


# ============================================================
# FUNCTION: CALCULATE IOU
# ============================================================

def calculate_iou(box1, box2):

    """
    Calculate Intersection over Union
    between two bounding boxes.
    """

    # Intersection coordinates

    x1 = max(
        box1[0],
        box2[0]
    )

    y1 = max(
        box1[1],
        box2[1]
    )

    x2 = min(
        box1[2],
        box2[2]
    )

    y2 = min(
        box1[3],
        box2[3]
    )


    # Intersection dimensions

    intersection_width = max(
        0,
        x2 - x1
    )

    intersection_height = max(
        0,
        y2 - y1
    )


    # Intersection area

    intersection_area = (
        intersection_width *
        intersection_height
    )


    if intersection_area == 0:

        return 0


    # Area of first box

    area1 = (
        (box1[2] - box1[0]) *
        (box1[3] - box1[1])
    )


    # Area of second box

    area2 = (
        (box2[2] - box2[0]) *
        (box2[3] - box2[1])
    )


    # Union area

    union_area = (
        area1 +
        area2 -
        intersection_area
    )


    if union_area == 0:

        return 0


    # IoU

    return intersection_area / union_area


# ============================================================
# REAL-TIME DETECTION LOOP
# ============================================================

while True:

    # --------------------------------------------------------
    # Read webcam frame
    # --------------------------------------------------------

    ret, frame = cap.read()


    if not ret:

        print(
            "ERROR: Could not read webcam frame."
        )

        break


    # --------------------------------------------------------
    # Run YOLO detection
    # --------------------------------------------------------

    results = model.predict(
        source=frame,
        conf=CONFIDENCE,
        verbose=False
    )


    # --------------------------------------------------------
    # Detection lists
    # --------------------------------------------------------

    heads = []

    helmets = []


    # ========================================================
    # PROCESS YOLO DETECTIONS
    # ========================================================

    for result in results:

        for box in result.boxes:

            class_id = int(
                box.cls[0]
            )

            confidence = float(
                box.conf[0]
            )


            # Bounding box

            x1, y1, x2, y2 = map(
                int,
                box.xyxy[0]
            )


            detection_box = (
                x1,
                y1,
                x2,
                y2
            )


            # ------------------------------------------------
            # CLASS 0 = HEAD
            # ------------------------------------------------

            if class_id == 0:

                heads.append({

                    "box": detection_box,

                    "confidence": confidence

                })


            # ------------------------------------------------
            # CLASS 1 = HELMET
            # ------------------------------------------------

            elif class_id == 1:

                helmets.append({

                    "box": detection_box,

                    "confidence": confidence

                })


    # ========================================================
    # CHECK HEADS FOR HELMET
    # ========================================================

    violation_detected = False


    for head in heads:

        head_box = head["box"]

        helmet_found = False


        # ----------------------------------------------------
        # Compare head with every helmet
        # ----------------------------------------------------

        for helmet in helmets:

            helmet_box = helmet["box"]


            iou = calculate_iou(
                head_box,
                helmet_box
            )


            # Helmet overlaps head

            if iou > 0.05:

                helmet_found = True

                break


        # ====================================================
        # HEAD WITH HELMET
        # ====================================================

        if helmet_found:

            color = (
                0,
                255,
                0
            )

            label = (
                f"HEAD - HELMET OK "
                f"{head['confidence']:.2f}"
            )


        # ====================================================
        # HEAD WITHOUT HELMET
        # ====================================================

        else:

            color = (
                0,
                0,
                255
            )

            label = (
                f"HEAD - NO HELMET "
                f"{head['confidence']:.2f}"
            )

            violation_detected = True


        # ----------------------------------------------------
        # Draw head bounding box
        # ----------------------------------------------------

        cv2.rectangle(
            frame,
            (
                head_box[0],
                head_box[1]
            ),
            (
                head_box[2],
                head_box[3]
            ),
            color,
            2
        )


        # ----------------------------------------------------
        # Draw head label
        # ----------------------------------------------------

        cv2.putText(
            frame,
            label,
            (
                head_box[0],
                max(
                    head_box[1] - 10,
                    20
                )
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            color,
            2
        )


    # ========================================================
    # DRAW HELMET DETECTIONS
    # ========================================================

    for helmet in helmets:

        helmet_box = helmet["box"]


        cv2.rectangle(
            frame,
            (
                helmet_box[0],
                helmet_box[1]
            ),
            (
                helmet_box[2],
                helmet_box[3]
            ),
            (
                0,
                255,
                255
            ),
            2
        )


        cv2.putText(
            frame,
            f"HELMET {helmet['confidence']:.2f}",
            (
                helmet_box[0],
                max(
                    helmet_box[1] - 10,
                    20
                )
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.55,
            (
                0,
                255,
                255
            ),
            2
        )


    # ========================================================
    # SYSTEM INFORMATION
    # ========================================================

    cv2.putText(
        frame,
        "AI INDUSTRIAL SAFETY MONITORING",
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.70,
        (
            255,
            255,
            255
        ),
        2
    )


    cv2.putText(
        frame,
        f"Heads: {len(heads)}",
        (20, 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.60,
        (
            255,
            255,
            255
        ),
        2
    )


    cv2.putText(
        frame,
        f"Helmets: {len(helmets)}",
        (20, 95),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.60,
        (
            255,
            255,
            255
        ),
        2
    )


    # ========================================================
    # SAFETY STATUS
    # ========================================================

    if violation_detected:

        cv2.putText(
            frame,
            "SAFETY VIOLATION DETECTED",
            (20, 135),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            (
                0,
                0,
                255
            ),
            3
        )


        # ----------------------------------------------------
        # Current time
        # ----------------------------------------------------

        current_time = time.time()


        # ----------------------------------------------------
        # Save screenshot every 5 seconds
        # ----------------------------------------------------

        if (
            current_time -
            last_screenshot_time
            >= screenshot_delay
        ):


            timestamp = datetime.now().strftime(
                "%Y%m%d_%H%M%S"
            )


            filename = (
                f"screenshots/"
                f"violation_{timestamp}.jpg"
            )


            # Save image

            cv2.imwrite(
                filename,
                frame
            )


            print()
            print(
                "[ALERT] SAFETY VIOLATION DETECTED"
            )


            print(
                f"[SCREENSHOT] Saved: {filename}"
            )


            # =================================================
            # SAVE EVENT TO SQLITE
            # =================================================

            if heads:

                highest_confidence = max(
                    head["confidence"]
                    for head in heads
                )

            else:

                highest_confidence = 0.0


            event_id = log_violation(

                violation_type="No Helmet",

                confidence=highest_confidence,

                screenshot_path=filename

            )


            print(
                f"[EVENT ID] {event_id}"
            )


            # Update screenshot timer

            last_screenshot_time = current_time


    # ========================================================
    # SAFE STATUS
    # ========================================================

    elif len(heads) > 0:

        cv2.putText(
            frame,
            "STATUS: ALL WORKERS SAFE",
            (20, 135),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.70,
            (
                0,
                255,
                0
            ),
            2
        )


    # ========================================================
    # NO PERSON
    # ========================================================

    else:

        cv2.putText(
            frame,
            "STATUS: NO PERSON DETECTED",
            (20, 135),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (
                255,
                255,
                255
            ),
            2
        )


    # ========================================================
    # DISPLAY WEBCAM
    # ========================================================

    cv2.imshow(
        "Industrial Safety AI",
        frame
    )


    # ========================================================
    # PRESS Q TO QUIT
    # ========================================================

    if cv2.waitKey(1) & 0xFF == ord("q"):

        break


# ============================================================
# CLEANUP
# ============================================================

cap.release()

cv2.destroyAllWindows()


print()
print("Real-time monitoring stopped.")