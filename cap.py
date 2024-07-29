import cv2
cap = cv2.VideoCapture(0)
ret, frame=cap.read()
cv2.imwrite('captured_image.jpg',frame)
cap.release()
cv2.destroyAllWindows()
print("image saved as 'captured_image.jpg'")