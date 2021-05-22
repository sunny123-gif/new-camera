import cv2

cap = cv2.VideoCapture(0)
tracker = cv2.TrackerKCF_create()
succes,img = cap.read()
box = cv2.selectROI("tracking",img,False)
tracker.init(img,box)
def drawbox(img,box):
    x,y,w,h = int(box[0]),int(box[1]),int(box[2]),int(box[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)
    cv2.putText(img,"tracking",(75,75),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,255),2,cv2.LINE_AA)
while True:
    succes,img = cap.read()
    succes,box = tracker.update(img)
    if succes:
        drawbox(img,box)
    else:
        print("lost")
    cv2.imshow("tracking",img)
    key = cv2.waitKey(1)
