from ultralytics import YOLO
import  cv2
import cvzone
import math
import pyttsx3
from multiprocessing import Process
import requests 
import numpy as np 
import imutils 


#run camera and detection+speech as seperate loops. 
# Replace the below URL with your own. Make sure to add "/shot.jpg" at last. 
url = "http://10.241.190.149:8080/shot.jpg" #use the url from IP webcam

def speech(text):
        engine = pyttsx3.init()
        engine.setProperty('rate', 220)
        engine.setProperty('volume', 0.9)
        voices = engine.getProperty('voices')
        engine.setProperty('voice' , voices[0].id)

        engine.say(text) 
    #engine.save_to_file(opencv_response ,'audio.mp3' ) - saves opencv response as a file
        engine.runAndWait()  
#def loop_a():       # While loop to continuously fetching data from the Url 
    #while True: 
        # img_resp = requests.get(url) 
        # img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8) 
        # img = cv2.imdecode(img_arr, -1) 
        # img = imutils.resize(img, width=1000, height=1800) 
        # cv2.imshow("Android_cam", img)

    

    #spelling word option, get word definition from internet option - allows using of tool for learning

    #tracking code checks detected changes, if there is a change then the variables are read aloud.
    # A = j#tracker data
    # B = j#tracker data

    # engine.say(str(A + B))
    # engine.runAndWait()

# cap = cv2.VideoCapture(0)
# cap.set(3, 1280) # use as mid points
# cap.set(4, 720)  # use as mid points
def loop_b():
    img_resp = requests.get(url) 
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8) 
    img = cv2.imdecode(img_arr, -1) 
    img = imutils.resize(img, width=1000, height=1800) 
    cv2.imshow("Android_cam", img)
    model = YOLO('../YOLO Weights/yolov8n.pt')

    classNames = ["person","bicycle","car","motorbike","aeroplane","bus","train","truck","boat","traffic light","fire hydrant","stop sign","parking meter","bench","bird","cat","dog","horse","sheep","cow","elephant","bear","zebra","giraffe","backpack","umbrella","handbag","tie","suitcase","frisbee","skis","snowboard","sports ball","kite","baseball bat","baseball glove","skateboard","surfboard""tennis racket","bottle","wine glass","cup","fork","knife","spoon","bowl","banana","apple","sandwich","orange","broccoli","carrot","hot dog","pizza","donut","cake","chair","sofa","pottedplant","bed","diningtable","toilet","tvmonitor","laptop","mouse","remote","keyboard","cell phone""microwave","oven","toaster","sink","refrigerator","book","clock","vase","scissors","teddy bear","hair drier","toothbrush"]

    pv_obj = []
    cr_obj = []

    c = 0
    while c != 1000:
        img_resp = requests.get(url) 
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8) 
        img = cv2.imdecode(img_arr, -1) 
    # Read a frame from the video capture
    # success, img  =cap.read()
    # Pass the frame to the YOLO model by calling model(img, stream=True)This will return the detection results.
        results = model(img, stream=True)
        for r in results:
            pv_obj = cr_obj
            cr_obj = {}
            pre_obj = []

            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                w, h = x2-x1, y2-y1
                cvzone.cornerRect(img, (x1, y1, w, h))

                conf = math.ceil((box.conf[0]*100))/100

                cls = box.cls[0]
                name = classNames[int(cls)]
                pre_obj.append(name)
                cvzone.putTextRect(img, f'{name} 'f'{conf}', (max(0,x1), max(35,y1)), scale = 0.5)
            for obj in pre_obj:
                if obj not in cr_obj:
                    if 1000/2 < (x1+x2)/2:
                        cr_obj[obj] = [0, 1]
                    else:
                        cr_obj[obj] = [1, 0]
                else:
                    if 1000/2 < (x1+x2)/2:
                        cr_obj[obj][1] +=1
                    else:
                        cr_obj[obj][0] +=1
                
            if cr_obj != pv_obj:
                for obj in cr_obj:
                    img_resp = requests.get(url) 
                    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8) 
                    img = cv2.imdecode(img_arr, -1) 
                    img = imutils.resize(img, width=1000, height=1800) 
                    cv2.imshow("Android_cam", img)
                    if cr_obj[obj][0] ==1:
                        speech(f"There is {cr_obj[obj][0]} {obj} on the left")
                    if cr_obj[obj][1] ==1:
                        speech(f"There is {cr_obj[obj][1]} {obj} on the right")
                    if cr_obj[obj][0] > 1:
                        speech(f"There are {cr_obj[obj][0]} {obj} on the left")
                    else:
                        speech(f"There are {cr_obj[obj][1]} {obj} on the right")
                #position left or right if x<0 say left, x>0 say right. 
            
        
        c +=1
        


        # cv2.imshow("Image", img)
        cv2.waitKey(1)

    # Press Esc key to exit 
        if cv2.waitKey(1) == 27: 
            break
    
    cv2.destroyAllWindows()
if __name__ == "__main__":
#     Process(target=loop_a).start()
    Process(target=loop_b).start()
    
