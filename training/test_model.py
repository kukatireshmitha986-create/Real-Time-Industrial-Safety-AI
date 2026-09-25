from ultralytics import YOLO

print("Loading trained model...")

model = YOLO(
    r"runs\detect\models\industrial_safety_helmet\weights\best.pt"
)

print("Running predictions on test images...")

results = model.predict(
    source=r"dataset\test\images",
    conf=0.5,
    save=True
)

print("\nPrediction completed successfully!")
print("Check the generated prediction images inside the runs folder.")