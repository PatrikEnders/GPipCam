import cv2
from time import sleep
firstRun = 1
crash = True #Its not true
urlInput = input("Please enter your ip and port (ip:port): ")
while crash == True:
    try:
        while True:
            if firstRun == 1:
                crash == False
                firstRun == 0
            if crash == True:
                sleep(3)
            url = "https://"+urlInput+"/video" #<--- insert https-URL to your video stream here
            video_stream = cv2.VideoCapture(url)
            while True:
                _, frame = video_stream.read()
                cv2.imshow("Smartphone", frame)
        
                if cv2.waitKey(1) == ord("x"):
                    break
    
            video_stream.realease()
            crash = False
            cv2.destroyAllWindows
    except:
        crash = True
