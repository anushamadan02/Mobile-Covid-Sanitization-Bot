from flask import Flask, render_template, Response,redirect,request
import camera_stream
import time
from MQTT_drive import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('image_server.html')

def frame_generator():
    """This is our main video feed"""
    camera = camera_stream.setup_camera()

    # allow the camera to warm up
    time.sleep(0.1)
    for frame in camera_stream.start_stream(camera):
        encoded_bytes = camera_stream.get_encoded_bytes_for_frame(frame)
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + encoded_bytes + b'\r\n')

@app.route('/display')
def display():
    return Response(frame_generator(),
        mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/controlit', methods = ['POST'])
def signup():
    buttonHit = request.form['buttonPress']
    print("The button hit is '" + buttonHit + "'")
    if buttonHit == 'Forward':
        Drive_MQTT('f')#increase or decrese this time for sensitivity
	    
    elif buttonHit == 'Back':
        Drive_MQTT('b')
	   
    elif buttonHit == 'Left':
         Drive_MQTT('l')
	    
    elif buttonHit == 'Right':
         Drive_MQTT('r')
	    #print ("Move Right")
    elif buttonHit == 'Stop':
         Drive_MQTT('s')
    else :
        print ("Move Right")
    return redirect('/')

app.run(host="0.0.0.0", debug=True, port=5001)
