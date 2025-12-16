from ultralytics import YOLO
import cv2

# Load model YOLO
model = YOLO("yolov8n.pt")

# Load image
img = cv2.imread("eee.jpg") #ganti dengan gambar image.png

# Deteksi objek
results = model(img)

count = 0

for r in results:
    for box in r.boxes:
        cls = int(box.cls[0])
        if model.names[cls] == "person":
            count += 1
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)

cv2.putText(
    img,
    f"Jumlah Orang: {count}",
    (20,40),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0,0,255),
    2
)

cv2.imshow("People Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()