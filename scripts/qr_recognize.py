from datetime import datetime
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN
# log_file = open('log.txt', 'a')

bandejas = {}
count = 0
print('ready to detect!')
while True:
    _, frame = cap.read()

    decodedObjects = pyzbar.decode(frame)
    
    for obj in decodedObjects:
        # print("Data", obj.data)
        if(obj.data in bandejas):
            now = datetime.now()
            delta = (now - bandejas[obj.data]).total_seconds()
            if(delta >= 15):
                bandejas[obj.data] = now
                print('bandeja reconocida')
                name = "frame%d.jpg"%count
                count += 1
                cv2.imwrite(name, frame)

        else:
            bandejas[obj.data] = datetime.now()
            print('bandeja agregada ', obj.data)
            name = "frame%d.jpg"%count
            count += 1
            cv2.imwrite(name, frame)
        
    #     cv2.putText(frame, str(obj.data), (50, 50), font, 2,
    #                 (255, 0, 0), 3)

    # cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        print('holamundo')
        print(frame_counter)
        print(frame_detected)
        break