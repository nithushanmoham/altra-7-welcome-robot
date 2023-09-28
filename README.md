# Altra 7 Welcome Robot

## Introduction

  Welcome to the Altra7 Welcome Robot project repository. This project showcases a Python-based robot system that utilizes OpenCV for person detection and captures images of detected      persons along with date and time information. The robot's primary function is to provide a warm welcome to visitors by capturing their images during their arrival.

## Features

- Real-time person detection using OpenCV.
- Image capture with date and time stamp.
- Customizable welcome messages.
- Easily deployable on a variety of robotic platforms.

## Image Processing Steps

  1. Person Detection Utilize OpenCV's pre-trained deep learning models like YOLO (You Only Look Once) or Haar Cascades to detect the presence of a person in the video feed or image.
  
  2. Image Capture When a person is detected, capture the current frame or image from the camera.

  3. Timestamping Generate a timestamp with the current date and time when the image was captured.

  4. Saving Image Save the captured image with the timestamp to a specific directory on your system.

## Example Output

- The captured images will be saved in the designated directory with filenames containing the timestamp. For example: person_image_2023-09-26_14-30-15.jpg.

## Python Libraries

  Make sure you have the following Python libraries installed:

- OpenCV
- NumPy
- datetime

## Setup

- Install Speech Recognition Module

  ```
    pip install SpeechRecognition
  ```

- Install Opencv

  ```
    pip install cv2
  ```

- Install DateTime

  ```
    pip install datetime
  ```
  
- Install Os

  ```
    pip install os
  ```

  
- Install Pyttsx3

  ```
    pip install pyttsx3
  ```
  
- Install Playsound


  ```
    pip install playsound
  ```
  
  ## Social Links

  - [Linkedin](https://www.linkedin.com/in/nithushanmohan/)
  
  - [Facebook](https://www.facebook.com/profile.php?id=100077725721945)
