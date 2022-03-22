import cv2
from deepface import DeepFace
import numpy as np
import time
import SMSAlert

start = time.time()

count = {
    "sad": 0,
    "happy": 0,
    "neutral": 0,
    "fear": 0,
    "surprise": 0,
    "disgust": 0,
    "angry": 0
}

faceCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

video = cv2.VideoCapture(0)

if not video.isOpened():
    video = cv2.VideoCapture(1)

if not video.isOpened():
    raise IOError("Cannot Open Webcam")

while True:
    # Capture Frame
    ret, frame = video.read()

    # We are specifying the action as emotion because we need only the emotion of the person
    result = ""
    try:
        result = DeepFace.analyze(frame, actions=['emotion'])
        count[result['dominant_emotion']] += 1
        print(result['dominant_emotion'])

    except:
        pass
    end = time.time()
    if int(end - start) == 60:
        print("Here")
        maxEmotion = max(count, key=lambda x: count[x])
        if maxEmotion == "sad":
            SMSAlert.email_alert(
                "poovizhikannan370@gmail.com", "Sad", "Just smile bro")
        elif maxEmotion == "fear":
            SMSAlert.email_alert(
                "poovizhikannan370@gmail.com", "Sad", "Dont worry bro bro")

        start = time.time()
    # Conevert colored image frame to grey since deepface algorithm works on grey scale images
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(grey, 1.1, 4)

    # Drawing rectange around face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Setting Font to display on the image
    font = cv2.FONT_HERSHEY_SIMPLEX
    if result != "":
        cv2.putText(frame,
                    result['dominant_emotion'],
                    (0, 50),
                    font, 1,
                    (0, 255, 0),
                    2,
                    cv2.LINE_4)
    cv2.imshow('Video', cv2.resize(
        frame, (960, 800), interpolation=cv2.INTER_CUBIC))

    if cv2.waitKey(2) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
