import numpy as np
import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('/home/diegosnore/.local/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_alt2.xml')
while(True):
    #Captiure frame by frame
    ret,frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5 ,minNeighbors=5)

    for(x,y,w,h) in faces:
        print(x,y,w,h)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        #Recognize

        #Imprime una imagen del momento justo en el que ce cierra el panel
        img_item = "my-impg.png"
        cv2.imwrite(img_item,roi_gray)

        #Para dibujar un rectangulo
        color = (0,255,0) #BGR
        stroke = 2
        #Tamaño caja para encerrar la cara
        end_cordx = x + w
        end_cordy = y + h
        #             donde,cord ini, cord fin,        color , stroke
        cv2.rectangle(frame,(x,y),(end_cordx,end_cordy),color, stroke)





    #Display the resutl framne
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()

