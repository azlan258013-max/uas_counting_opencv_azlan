# uas_counting_opencv_azlan


Anda bilang:
Jelaskan tiap fungsi kodenya 
from ultralytics import YOLO
import cv2

# Load model YOLO
model = YOLO("yolov8n.pt")

# Load image
img = cv2.imread("image.png")

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
ChatGPT bilang:
Berikut penjelasan tiap baris / fungsi kode secara runtut dan bahasa sederhana 👇

1. Import library
from ultralytics import YOLO
import cv2
YOLO → library Ultralytics YOLOv8 untuk deteksi objek.

cv2 → OpenCV, dipakai untuk membaca gambar, menggambar kotak, dan menampilkan hasil.

2. Load model YOLO
model = YOLO("yolov8n.pt")
Memuat model YOLOv8 nano (yolov8n.pt)

Model ini:

Sudah pre-trained

Bisa mendeteksi banyak objek (person, car, motor, dll)

model.names berisi nama kelas objek (COCO dataset)

3. Load gambar
img = cv2.imread("image.png")
Membaca file gambar image.png

Hasilnya disimpan dalam variabel img

Format: array (numpy) berisi pixel gambar

4. Deteksi objek
results = model(img)
Menjalankan YOLO pada gambar

Menghasilkan hasil deteksi

results berisi:

bounding box

confidence

class label

5. Variabel penghitung orang
count = 0
Menyimpan jumlah orang yang terdeteksi

6. Loop hasil deteksi
for r in results:
r → hasil deteksi untuk satu gambar

Karena YOLO bisa memproses banyak gambar sekaligus

7. Loop bounding box
for box in r.boxes:
r.boxes → semua kotak deteksi

Setiap box berisi:

koordinat

kelas

confidence

8. Ambil kelas objek
cls = int(box.cls[0])
box.cls → ID kelas objek

Contoh:

0 = person

2 = car

Diubah ke int supaya bisa dipakai indexing

9. Cek apakah objek adalah orang
if model.names[cls] == "person":
model.names[cls] → nama kelas

Hanya menghitung objek "person"

Objek lain diabaikan

10. Tambah jumlah orang
count += 1
Setiap ada orang terdeteksi → tambah 1

11. Ambil koordinat bounding box
x1, y1, x2, y2 = map(int, box.xyxy[0])
box.xyxy → koordinat kotak:

(x1, y1) → pojok kiri atas

(x2, y2) → pojok kanan bawah

map(int, ...) → ubah ke integer (OpenCV butuh integer)

12. Gambar kotak deteksi
cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)
Menggambar kotak hijau di sekitar orang

(0,255,0) → warna hijau

2 → ketebalan garis

13. Tampilkan jumlah orang
cv2.putText(
    img,
    f"Jumlah Orang: {count}",
    (20,40),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0,0,255),
    2
)
Menampilkan teks di gambar

Isi teks → jumlah orang

Posisi → (20, 40)

Warna merah (0,0,255)

Ketebalan teks 2

14. Tampilkan hasil ke layar
cv2.imshow("People Detection", img)
Menampilkan window berisi hasil deteksi

15. Menunggu input keyboard
cv2.waitKey(0)
Program menunggu tombol ditekan

0 → tunggu tanpa batas

16. Tutup semua window
cv2.destroyAllWindows()
Menutup semua jendela OpenCV

Membersihkan resource

🔍 Ringkasan Fungsi Program
✔ Membaca gambar
✔ Mendeteksi objek menggunakan YOLOv8
✔ Menghitung jumlah orang
✔ Menggambar bounding box
✔ Menampilkan hasil ke layar

