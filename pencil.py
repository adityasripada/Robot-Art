#Detects Face, Converts to Pencil Drawing, Writes Pixels to file
import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
c= cv2.VideoCapture(1)
ramp_frames = 30

def get_image():
 # read is the easiest way to get a full image out of a VideoCapture object.
	retval, im = c.read()
	return im

def dodgeV2(image, mask):
  return cv2.divide(image, 255-mask, scale=256)

while True:
	_,cap = c.read()
	cv2.imshow('hey',cap)
	k = cv2.waitKey(25)
	if k == ord('q'):
		print("Taking image...")
		cv2.imwrite("hello.jpg",cap)
		print("Image Saved!!")
		break;

im = cv2.imread('hello.jpg')
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Gray',gray)
inv = 255 - gray
#cv2.imshow('Inv',inv)
blur = cv2.GaussianBlur(inv, ksize=(21, 21),sigmaX=0, sigmaY=0)
#cv2.imshow('Blur',blur)
blend = dodgeV2(gray, blur)
cv2.imshow("pencil sketch", blend)
ret,th = cv2.threshold(blend,127,255,cv2.THRESH_BINARY)
cv2.imshow("Thresh", th)
cv2.imwrite('blend.jpg',blend)
'''
canny = cv2.Canny(th, 600, 700)
cv2.imshow('canny',canny)


im2,contours,hierarchy = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#print contours
cv2.imshow('contours',im2)
'''
xvalues = []
yvalues = []

for i in range(len(th)):
	for j in range(len(th[i])):
		if th[i][j]==0:
			xvalues.append(str(j))
			yvalues.append(str(i))

#for i in range(len(contours)):
	#xvalues.extend([str(x[0][0]) for x in contours[i]])
    	#yvalues.extend([str(x[0][1]) for x in contours[i]])

f = open('xf.txt','w')
f.write(' '.join(xvalues))
f.close()
f = open('yf.txt','w')
f.write(' '.join(yvalues))
f.close()

cv2.waitKey(0)
cv2.destroyAllWindows()

