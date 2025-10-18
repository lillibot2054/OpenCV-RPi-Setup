import cv2

print("OpenCV version:", cv2.__version__)

# Test reading an image
img = cv2.imread('FILE.NAME')
if img is None:
    print("OpenCV is working. No test image found.")
else:
    cv2.imshow('Test Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
