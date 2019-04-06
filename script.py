import cv2

face_cascade = cv2.CascadeClassifier( "haarcascade_frontalface_default.xml")

img = cv2.imread('photo.jpg')
grey_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(grey_img,minNeighbors=5,
scaleFactor=1.05)
for x,y,w,h in faces:
		img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)


cv2.imshow('rec_img',img)
cv2.waitKey(5000)
cv2.destroyAllWindows()