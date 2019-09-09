import tkinter as tk
from tkinter.filedialog import askopenfilename
import cv2
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import sys


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


root = tk.Tk()
root.withdraw()

filename = askopenfilename()
try:
    Image.open(filename).verify()
except Exception:
    sys.exit("Invalid image")

img = cv2.imread(filename)
h, w, _ = img.shape

boxes = pytesseract.image_to_boxes(img)

# draw the bounding boxes on the image
for b in boxes.splitlines():
    b = b.split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

# show annotated image and wait for keypress
cv2.imshow(filename, img)
cv2.waitKey(0)


cv2.waitKey(0)



cv2.destroyAllWindows()


