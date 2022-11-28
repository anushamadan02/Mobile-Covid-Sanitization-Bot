# create by @CarmelitoA  - to repair/add Pi control to the broken moster truck - Feel free to use and remix
# you can run this directly using the shell
#using the Adafruit DC motor Pi Hat http://www.adafruit.com/product/2348
#import pygame  #for more info on keyboard events https://www.pygame.org/docs/ref/key.html
import time

#importing flask 

from flask import Flask,  request, render_template, Response , redirect 
from MQTT_drive import *
import cv2


app = Flask(__name__)
camera=cv2.VideoCapture(-1)
def gen_frames():  
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/controlit', methods = ['POST'])
def signup():
    buttonHit = request.form['buttonPress']
    print("The button hit is '" + buttonHit + "'")
    if buttonHit == 'Foward':
        Drive_MQTT('f')#increase or decrese this time for sensitivity
	    
    elif buttonHit == 'Back':
        Drive_MQTT('b')
	   
    elif buttonHit == 'Left':
         Drive_MQTT('l')
	    
    elif buttonHit == 'Right':
           Drive_MQTT('r')
	    #print ("Move Right")
    else :
        print ("Move Right")
    return redirect('/')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(host= '0.0.0.0', debug = True)
