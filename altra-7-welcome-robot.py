import cv2
import pyttsx3
import datetime
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

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

# Create the "detected_objects" folder if it doesn't exist
if not os.path.exists("detected_objects"):
    os.makedirs("detected_objects")

val = 3  # or any other appropriate value

if val >= 2:
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
                speak('Today is a good day,You are welcome to come in')
                
                # Save image of detected object
                object_img = frame[y:y+h, x:x+w]
                label = class_name.lower()  # Convert class name to lowercase for filename
                now = datetime.datetime.now()
                object_filename = f"{label}_{now.strftime('%Y-%m-%d_%H-%M-%S')}.jpg"
                cv2.imwrite(os.path.join("Data-details", object_filename), object_img)
                val = 0
                print(f"Image saved as {object_filename}")
            
            cv2.imshow("Object Detection", frame)
    
        # Press 'q' to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the camera and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
