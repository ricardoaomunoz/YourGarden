async_mode = None

if async_mode is None:
    try:
        import eventlet
        async_mode = 'eventlet'
    except ImportError:
        pass

    if async_mode is None:
        try:
            from gevent import monkey
            async_mode = 'gevent'
        except ImportError:
            pass

    if async_mode is None:
        async_mode = 'threading'

    print('async_mode is ' + async_mode)

# monkey patching is necessary because this application uses a background
# thread
if async_mode == 'eventlet':
    import eventlet
    eventlet.monkey_patch()
elif async_mode == 'gevent':
    from gevent import monkey
    monkey.patch_all()





from flask import Flask, jsonify, request, session
from flask_socketio import SocketIO, send, emit
import json
from threading import Thread
import time
from services.dth22 import DTH22
from services.gpio_control import Gpio_controller

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

socketIo = SocketIO(app, cors_allowed_origins="*", async_mode=async_mode)
thread = None

app.debug = True
app.host = 'localhost'
users = {}
LightControler = Gpio_controller()
Sensor1 = DTH22()






def read_jsonfile():
    with open('/home/pi/Indoor_cultivation/app_indoor/indoor-app/server/config.json', 'r') as config_file:
        data = json.load(config_file)
        time_light = {
            "turn_on": data['light_time'][0],
            "turn_off": data['light_time'][1]
        }
    return time_light

def modifyJson_file(data):
    print(f"modify json {data}")
    with open('/home/pi/Indoor_cultivation/app_indoor/indoor-app/server/config.json', 'w') as config_file:
        # data = json.load(config_file)
        data= {"light_time" : data}
        json.dump(data, config_file)
  

def turn_light():
    while True:
        time_light = read_jsonfile()
        time_actual = time.strftime('%H:%M')
        if time_light["turn_on"] > time_light["turn_off"]:
            if (time_actual >= time_light["turn_on"] and time_actual < "23:59") or (time_actual < time_light["turn_off"]):
                print("LIGHT ON")
                LightControler.turn_on()
            else:
                print("LIGHT OFF")
                LightControler.turn_off()
        else:
            if time_actual >= time_light["turn_on"] and time_actual < time_light["turn_off"]:
                print("LIGHT ON")
                LightControler.turn_on()
            else:
                print("LIGHT OFF")
                LightControler.turn_off()

        time.sleep(1)



@socketIo.on("message")
def handleMessage(msg):
    print(msg)
    send(msg, broadcast=True)
    return None


@socketIo.on('connect', namespace='/')
def test_connect():
    print("CONECTED!!!!!!!")
    retrieve_active_users()

def retrieve_active_users():
    emit('retrieve_active_users', broadcast=True)

def send_dth22_info():
    """Example of how to send server generated events to clients."""
    while True:
        temp, humd = Sensor1.read_values(save=True)
        data = {'temperature': float("{:.2f}".format(temp)), 'humidity': float("{:.2f}".format(humd))}
        print(f"emitiendo data de sensor: {data}")
        socketIo.emit('sensor1_setter', data, broadcast=True)
        time.sleep(10)


@socketIo.on('activate_user')
def on_active_user(data):
    print(f"active user  {data}  #####")
    user = data.get('username')
    emit('user_activated', {'user': user}, broadcast=True)
    emit('time_setter', read_jsonfile(), broadcast=True)


@socketIo.on('time-light')
def set_time_light(data):
    print(f"###### SEt Time LIGHT ######## {data}")
    modifyJson_file(data["timer"])
    emit('time_setter', read_jsonfile(), broadcast=True)



@socketIo.on('username')
def new_user(msg):
    print(f" ### mensaje username ## {msg} {str(socketIo)}")
    session['receive_count'] = session.get('receive_count', 0) + 1
    user = {
        "name": msg,
        "id": session['receive_count']
            # request.namespace.socket.sessid)
    }
    users[session['receive_count']] = user
    print(f"emitiendo connect and users!!!!!!!!!!!! user: {user}, users: {list(users.values())}")
    emit('connected', (user), broadcast=True)
    emit('users', list(users.values()), broadcast=True)





if __name__ == '__main__':
    if thread is None:
        thread = Thread(target=send_dth22_info)
        thread.daemon = True
        thread1 = Thread(target=turn_light)
        thread1.daemon = True
        thread.start()
        thread1.start()
    socketIo.run(app, host="192.168.1.99", port=5000)
