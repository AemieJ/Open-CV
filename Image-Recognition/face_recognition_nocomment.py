
import cv2 

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 
eye_cascade =  cv2.CascadeClassifier("haarcascade_eye.xml")  

def detect(gray,frame) : 
      faces = face_cascade.detectMultiScale(gray,1.3,5) 
      for (x,y,w,h) in faces : 
          cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2) 
          roi_gray = gray[y:y+h,x:x+w] 
          roi_color = frame[y:y+h,x:x+w] 
          eyes = eye_cascade.detectMultiScale(roi_gray,1.1,3) 
          for(ex,ey,ew,eh) in eyes : 
              cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
      return frame

def main(): 
    cam = cv2.VideoCapture(0) #1 if you are using an external webcam connected to your computer
    while True : 
        _,frame = cam.read() 
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
        canvas = detect(gray,frame) 
        cv2.imshow("Video",canvas) 
        k = cv2.waitKey(1) & 0xff
        if k == 27: #press esc to escape
            break       
    cam.release()   
    cv2.destroyAllWindows()
    
main() 

