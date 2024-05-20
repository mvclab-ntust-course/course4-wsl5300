from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO("yolov8n-seg.pt")

# Define path to the image file
source = "/Users/wsl/work/mvc/week4/argoverse.mp4"

# Run inference on the source
results = model(source, save=True, classes=2) # list of Results objects
