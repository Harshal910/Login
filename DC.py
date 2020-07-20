import cv2
import numpy as np
import sqlite3
faceDetect = cv2.CascadeClassifier('C:\\Users\\harsh\\anaconda3\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
def InsertOrUpdate(ID,Name):
    conn=sqlite3.connect("Record.db")
    cmd="SELECT * FROM std WHERE ID="+str(ID)
    cursor=conn.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd="UPDATE std SET Name="+str(Name)+" WHERE ID="+str(ID)
    else:
        cmd="INSERT INTO std(ID,Name) Values("+str(ID)+","+str(Name)+")"
    conn.execute(cmd)
    conn.commit()
    conn.close()
id=input("enter user id")
name=input("enter your name")
InsertOrUpdate(id,name)



sampleNum=0
while(True):
    ret,img=cam.read()
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        sampleNum=sampleNum+1
        cv2.imwrite("dataSet/User."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(100)
    cv2.imshow("Face",img)
    cv2.waitKey(1)
    if(sampleNum>20):
        break
cam.release()
cv2.destroyAllWindows()