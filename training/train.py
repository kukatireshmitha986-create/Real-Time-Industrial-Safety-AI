from ultralytics import YOLO

print("Loading YOLO model...")

model = YOLO("yolo11n.pt")

print("Starting training...")

results = model.train(
    data="dataset/data.yaml",
    epochs=20,
    imgsz=640,
    batch=8,
    name="industrial_safety_helmet",
    project="models",
    workers=2,
    patience=5
)

print("\nTraining completed successfully!")
print("Best model:")
print("models/industrial_safety_helmet/weights/best.pt")