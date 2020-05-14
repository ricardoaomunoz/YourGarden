# USAGE
# python webstreaming.py --ip 0.0.0.0 --port 8000

# import the necessary packages
from pyimagesearch.motion_detection import SingleMotionDetector
from imutils.video import VideoStream
from flask import Response
from flask import Flask
from flask import render_template, session
from flask_socketio import SocketIO, send, emit
from services.dth22 import DTH22
from services.gpio_control import Gpio_controller
import threading
import argparse
import datetime
import imutils
import time
import cv2

# initialize the output frame and a lock used to ensure thread-safe
# exchanges of the output frames (useful for multiple browsers/tabs
# are viewing tthe stream)
outputFrame = None
lock = threading.Lock()

# initialize a flask object
app = Flask('Raspberry')
app = Flask(__name__.split('.')[0])
# app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret' #SOCKETIO
socketio = SocketIO(app)  #SOCKETIO

# initialize the video stream and allow the camera sensor to
# warmup
#vs = VideoStream(usePiCamera=1).start()
vs = VideoStream(src=0).start()
time.sleep(2.0)

LIGHT_STATE = False

@app.route('/')
def index():
	return render_template("index.html", now = datetime.datetime.now())

@app.route("/video_streaming")
def video_streaming():
	# return the rendered template
	return render_template("video_s.html")

# @socketio.on('connect')
# def test_connect():
# 	print("CONNECTED!!!!")
# 	dth_sensor = DTH22()
# 	while True:
# 		temp, hum = dth_sensor.read_values()
# 		print(f"temperatura {temp} humedad {hum}")
# 		send(f"temperatura {temp} humedad {hum}")
# 		# emit('dth22 response', {'temperatura': str(temp), 'humedad': str(hum)})
		# time.sleep(3)



@socketio.on('connect')
def test_connect():
	print("CONECTED!!!!!!!")
	emit('my_response', {'data': 'Connected', 'count': 0})
	emit('light_status', {'light_state': LIGHT_STATE})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

@socketio.on('my_event')
def test_message(message):
	# USERS += 1
	print("Start new Session!!")
	session['receive_count'] = session.get('receive_count', 0) + 1
	emit('my_response',
         {'data': message['data'], 'count': session['receive_count']})


dth_sensor = DTH22()
@socketio.on('get_dh22')
def dh22():
	# temp, hum = dth_sensor.read_values()
	temp = 20.033
	hum = 70.243
	print(f"temperatura {temp} humedad {hum}")
	emit('sensor_data', {'temperatura': str(temp), 'humedad': str(hum)})


@socketio.on('light_auto')
def auto_light(message):
	if message:
		print("Encendido automatico Prendido!!!!")
		# light_control.turn_on()
	else:
		print("Apagado el encendido automatico")
		# light_control.turn_off()

light_control = Gpio_controller()
@socketio.on('light')
def light(message):
	if message:
		print("Encendiendo Luz!!!!")
		light_control.turn_on()
		LIGHT_STATE = True
		emit('light_status', {'light_state': LIGHT_STATE}, broadcast=True)
	else:
		print("Apagado Luz")
		light_control.turn_off()
		LIGHT_STATE = False
		emit('light_status', {'light_state': LIGHT_STATE}, broadcast=True)








def detect_motion(frameCount):
	# grab global references to the video stream, output frame, and
	# lock variables
	global vs, outputFrame, lock

	# initialize the motion detector and the total number of frames
	# read thus far
	md = SingleMotionDetector(accumWeight=0.1)
	total = 0

	# loop over frames from the video stream
	while True:
		# read the next frame from the video stream, resize it,
		# convert the frame to grayscale, and blur it
		frame = vs.read()
		# frame = imutils.resize(frame, width=1280)
		frame = imutils.resize(frame, width=920)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		gray = cv2.GaussianBlur(gray, (7, 7), 0)

		# grab the current timestamp and draw it on the frame
		timestamp = datetime.datetime.now()
		cv2.putText(frame, timestamp.strftime(
			"%A %d %B %Y %I:%M:%S%p"), (10, frame.shape[0] - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

		# if the total number of frames has reached a sufficient
		# number to construct a reasonable background model, then
		# continue to process the frame
		if total > frameCount:
			# detect motion in the image
			motion = md.detect(gray)

			# cehck to see if motion was found in the frame
			if motion is not None:
				# unpack the tuple and draw the box surrounding the
				# "motion area" on the output frame
				(thresh, (minX, minY, maxX, maxY)) = motion
				cv2.rectangle(frame, (minX, minY), (maxX, maxY),
					(0, 0, 255), 2)
		
		# update the background model and increment the total number
		# of frames read thus far
		md.update(gray)
		total += 1

		# acquire the lock, set the output frame, and release the
		# lock
		with lock:
			outputFrame = frame.copy()
		
def generate():
	# grab global references to the output frame and lock variables
	global outputFrame, lock

	# loop over frames from the output stream
	while True:
		# wait until the lock is acquired
		with lock:
			# check if the output frame is available, otherwise skip
			# the iteration of the loop
			if outputFrame is None:
				continue

			# encode the frame in JPEG format
			(flag, encodedImage) = cv2.imencode(".jpg", outputFrame)

			# ensure the frame was successfully encoded
			if not flag:
				continue

		# yield the output frame in the byte format
		yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
			bytearray(encodedImage) + b'\r\n')

@app.route("/video_feed")
def video_feed():
	# return the response generated along with the specific media
	# type (mime type)
	return Response(generate(),
		mimetype = "multipart/x-mixed-replace; boundary=frame")

# check to see if this is the main thread of execution
if __name__ == '__main__':
	# construct the argument parser and parse command line arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--ip", type=str, required=True,
		help="ip address of the device")
	ap.add_argument("-o", "--port", type=int, required=True,
		help="ephemeral port number of the server (1024 to 65535)")
	ap.add_argument("-f", "--frame-count", type=int, default=32,
		help="# of frames used to construct the background model")
	args = vars(ap.parse_args())

	# start a thread that will perform motion detection
	t = threading.Thread(target=detect_motion, args=(
		args["frame_count"],))
	t.daemon = True
	t.start()

	# start the flask app
	socketio.run(app, host=args["ip"], port=args["port"], debug=True, use_reloader=False )
	#app.run(host=args["ip"], port=args["port"], debug=True,
	#	threaded=True, use_reloader=False)

# release the video stream pointer
vs.stop()