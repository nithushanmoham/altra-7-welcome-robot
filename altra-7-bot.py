import cv2
import pyttsx3
import wolframalpha
import playsound
import gtts as gt 
import os
from gtts import gTTS

engine = pyttsx3.init()

engine = pyttsx3.init()
engine.runAndWait()

'''len(voices)-1'''
voices = engine.getProperty('voices')
client = wolframalpha.Client(' IL 61820-7237, USA')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    engine.say(jet)
    
#Opencv DNN

jet = net = cv2.dnn.readNet("C:/Users/nithu/Desktop/school-project/my-projects/elephant-detection/dnn_model/yolov4-tiny.weights", "C:/Users/nithu/Desktop/school-project/my-projects/elephant-detection/dnn_model/yolov4-tiny.cfg")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(220,220),  scale=1/255)

#Load class  List
classes= []
with open("C:/Users/nithu/Desktop/school-project/my-projects/elephant-detection/dnn_model/classes.txt", "r") as file_object:
    for class_name in file_object.readlines():
        class_name = class_name.strip()
        classes.append(class_name)

print("Objects list")
print(classes)

#Instialize camera
cap=cv2. VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
#FULL HD 1920 X 1080

def click_button(event, x, y, flags, params):
    if event == cv2. EVENT_LBUTTONDOWN:
        print(x, y)

#Create window
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", click_button)
while True:
#Get frames
 ret, frame = cap.read()

#Object Detection
 (class_ids, scores, bboxes)=model.detect(frame)
 for class_id, score, bbox in zip(class_ids,scores, bboxes):
     (x, y, w, h) =bbox
     class_name = classes[class_id]

     cv2.putText(frame, class_name, (x, y - 10),cv2.FONT_HERSHEY_PLAIN, 3, (200,0, 50 ), 2)
     cv2.rectangle(frame, (x,y), (x+ w, y + h), (200,0, 50 ), 3)
       
     if class_name == 'person':
        speak('Hello come in please.') 


     elif class_name == 'elephant':
        speak('Warning Elephant has entered the town')
        playsound.playsound('C:/Users/nithu/Desktop/school-project/my-projects/elephant-detection/dog-audios/audios-1/10.mp3')


     cv2.waitKey(32)
     cv2.imshow("frame",frame) 