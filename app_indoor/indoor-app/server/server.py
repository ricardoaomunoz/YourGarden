


# from flask import Flask, render_template, request
# from flask_socketio import SocketIO, send, emit
# from flask import render_template, session
# from flask_cors import CORS


# app = Flask('indoor-app')
# app = Flask(__name__.split('.')[0])
# app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)
# CORS(app)
# # socketio.init_app(app, resources={r"/*": {"origins":"*"}}, headers=['Content-Type'], expose_headers=['Access-Control-Allow-Origin'], supports_credentials=True)
# users = {}


# @socketio.on('usernamesss')
# def new_user(msg):
#     print(f"mensaje {msg}")
#     # user = {
#     #     "name": msg,
#     #     "id": request.namespace.socket.sessid
#     # }
#     # users[request.namespace.socket.sessid] = user
#     # emit('connected', user, broadcast=True)
#     # emit('users', users, broadcast=True)
# 	# emit('light_status', {'light_state': LIGHT_STATE})


# @socketio.on('disconnect')
# def test_disconnect():
#     print('Client disconnected')



# # if __name__ == '__main__':
# socketio.run(app, host="localhost", port=5010, debug=True, use_reloader=False )


from flask import Flask, jsonify, request, session
from flask_socketio import SocketIO, send, emit
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

socketIo = SocketIO(app, cors_allowed_origins="*")

app.debug = True
app.host = 'localhost'
users = {}


def read_jsonfile():
    with open('config.json', 'r') as config_file:
        data = json.load(config_file)
        time_light = {
            "turn_on": data['light_time'][0],
            "turn_off": data['light_time'][1]
        }
    return time_light

def modifyJson_file(data):
    print(f"modify json {data}")
    with open('config.json', 'w') as config_file:
        # data = json.load(config_file)
        data= {"light_time" : data}
        json.dump(data, config_file)
  






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

@socketIo.on('activate_user')
def on_active_user(data):
    print(f"active user  {data}  #####")
    user = data.get('username')
    emit('user_activated', {'user': user}, broadcast=True)
    emit('time_setter', read_jsonfile(), broadvast=True)


@socketIo.on('time-light')
def set_time_light(data):
    print(f"###### SEt Time LIGHT ######## {data}")
    modifyJson_file(data["timer"])
    emit('time_setter', read_jsonfile(), broadvast=True)



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
    socketIo.run(app, host="192.168.1.100")
