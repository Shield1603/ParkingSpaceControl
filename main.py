import cv2
import pickle


width,height = 107,48
poslist=[]

def mouseclick(events,x,y,flags,params):
    if events == cv2.EVENT_LBUTTONDOWN:
        poslist.append((x,y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i,pos in enumerate(poslist):
            x1,y1 = pos
            if x1<x<x1+width and y1<y<y1+height:
                poslist.pop(i)




while True:
    #cv2.rectangle(img,(50,192),(157,240),(255,0,255),2)
    img = cv2.imread('carParkImg.png')
    for pos in poslist:
        cv2.rectangle(img,pos,(pos[0]+width,pos[1]+height),(255,0,255),2)

    cv2.imshow("image",img)
    cv2.setMouseCallback("image",mouseclick)
    cv2.waitKey(1)

