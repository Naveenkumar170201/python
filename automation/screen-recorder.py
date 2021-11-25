import cv2
import numpy as np
import pyautogui
screen_size = (1920,1080)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (screen_size))
while True :
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    #if user click q it exit
    if cv2.waitKey(1) == ord("q") :
        break
    cv2.destroyAllWindows()
    out.release()






'''from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
import datetime

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")

file_name = f"{time_stamp}.mp4"

fourcc = cv2.Videowriter_fourcc('m','p','4','v')
captured_video = cv2.VideoWriter(file_name,fourcc,20,(width,height))
while True:
    img = ImageGrab.grab(bbox=(0,0,width,height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)

    cv2.imshow("screen r((ecorder",img_final)
    captured_video.writer(img_final)
    k = cv2.waitkey(1)
    if k==27:
        break'''
