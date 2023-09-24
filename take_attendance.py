import cv2 
from simple_facerec import SimpleFacerec  
from datetime import datetime
from datetime import date
import pyttsx3 

today = date.today()
day = today.strftime("%b-%d-%Y")
day_str = "Ders yoklaması-" + day + ".csv"
print(day_str)

dosya = open(day_str, "a")
dosya.write("Ad,Soyad,Numara,Saat")
dosya.close()

engine = pyttsx3.init()

def yoklamayaYaz(name):
    with open(day_str, 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])

        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')
            
            engine.say(f"welcome, {name}")
            engine.runAndWait()

sfr = SimpleFacerec()  
sfr.load_encoding_images("images/")  
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read() 
    face_locations, face_names = sfr.detect_known_faces(frame) 
    for face_loc, name in zip(face_locations, face_names):
        #print(face_loc)
        y, h, w, x = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        cv2.putText(frame, name,(x, y - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x, y), (h, w), (0, 0, 200), 2) 
        
        yoklamayaYaz(name)


    cv2.imshow("Yoklama", frame) 
    key = cv2.waitKey(1)   
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

