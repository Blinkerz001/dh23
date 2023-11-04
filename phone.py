import requests 
import cv2 
import numpy as np 
import imutils 

# Replace the below URL with your own. Make sure to add "/shot.jpg" at last. 
url = "http://10.241.190.149:8080/shot.jpg" #use the url from IP webcam
  
# While loop to continuously fetching data from the Url 
while True: 
    img_resp = requests.get(url) 
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8) 
    img = cv2.imdecode(img_arr, -1) 
    img = imutils.resize(img, width=1000, height=1800) 
    cv2.imshow("Android_cam", img) 
  
    # Press Esc key to exit 
    if cv2.waitKey(1) == 27: 
        break
  
cv2.destroyAllWindows()