import cv2
import pyttsx3
import playsound
import speech_recognition as sr
import datetime
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Time Managing
def greetMe ():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 10 and currentH < 3:
        speak('Hi,Good Morning! Iam a Altra7 welcome robot. The time is',currentH)

    elif currentH >= 3 and currentH < 15:
        speak('Hi,Good Afternoon!')

    elif currentH >= 15 and currentH !=19:
        speak('Hi,Good Evening!') 

    elif currentH >= 19 and currentH !=10:
        speak('Good Night! It is night')
    else:
        print("finish")    

# Initialize OpenCV DNN for object detection
net = cv2.dnn.readNet("models/yolov4-tiny.weights", "models/yolov4-tiny.cfg")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(220, 220), scale=1/255)

# Load class list
classes = []
with open("models/classes.txt", "r") as file_object:
    for class_name in file_object.readlines():
        class_name = class_name.strip()
        classes.append(class_name)

print("Objects list")
print(classes)

# Initialize the camera
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Create the "data-details" folder if it doesn't exist
if not os.path.exists("data-details"):
    os.makedirs("data-details")

while True:
    ret, frame = cap.read(1)

    # Object Detection
    (class_ids, scores, bboxes) = model.detect(frame)
    
    for class_id, score, bbox in zip(class_ids, scores, bboxes):
        (x, y, w, h) = bbox
        class_name = classes[class_id]

        cv2.putText(frame, class_name, (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 3, (200, 0, 50), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (200, 0, 50), 3)

        
        if class_name == 'person':
            greetMe ()
            speak('You are warmly welcomed!')
            playsound.playsound('C:/Users/Nithushan/OneDrive/Desktop/altra-7-welcome-robot/Audios/tamil-4.mp3')
            
            # Save image of detected object
            object_img = frame[y:y+h, x:x+w]
            label = class_name.lower()  # Convert class name to lowercase for filename
            now = datetime.datetime.now()
            object_filename = f"{label}_{now.strftime('%Y-%m-%d_%H-%M-%S')}.jpg"
            cv2.imwrite(os.path.join("data-details", object_filename), object_img)

            print(f"Image saved as {object_filename}")      
        
        cv2.imshow("Object Detection", frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
