from flask import render_template, request, make_response, jsonify
import datetime
import json
from models import User
from app import app, db, bcrypt


@app.route('/', methods=['GET'])
def hello():
    return "HEllo World"

# @app.route('/register_plant', methods=['GET', 'POST'])
# def add_plant():
#     print("ENtro a ruta register plant")
#     if request.method == 'GET':
#         return render_template('add.html')
#     print("POST METHOD")
#     print(f"request args: {request.json}")
#     banco=request.json.get('seed_bank')
#     comentario=request.json.get('comment')
#     fecha_ingreso=datetime.datetime.now()
#     meta_data=request.json.get('meta_data')
#     sustrato=request.json.get('substrate')
#     volumen_matera=request.json.get('matera_size')
#     germination_type_id=request.json.get('germination_type_id')
#     planting_technique_id=request.json.get('planting_technique_id')
#     stage_id=request.json.get('stage_id')
#     plants_user_id=request.json.get('plants_user_id')

#     try:
#         plant = Plant(
#             banco=banco,
#             comentario=comentario,
#             fecha_ingreso=fecha_ingreso,
#             meta_data=meta_data,
#             sustrato=sustrato,
#             volumen_matera=volumen_matera,
#             germination_type_id=germination_type_id,
#             planting_technique_id=planting_technique_id,
#             stage_id=stage_id,
#             plants_user_id=plants_user_id

#         )
#         db.session.add(plant)
#         db.session.commit()
#         return "Plant added. plant id={}".format(plant.id)
#     except Exception as e:
#         return(str(e))






@app.route('/api/user/register', methods=['POST'])
def register_user():
    try:
        data = request.get_json()

        user = User.query.filter_by(email=data.get('email')).first()
        if not user:
            try:
                user = User(
                    email=data.get('email'),
                    username=data.get('username'),
                    password=data.get('password')
                )
                db.session.add(user)
                db.session.commit()

                # generate the auth token
                auth_token = user.encode_auth_token(user.id)
                responseObject = {
                    'status': 'success',
                    'message': 'Successfully registered.',
                    'auth_token': auth_token.decode()
                }
                return make_response(jsonify(responseObject)), 201

            except Exception as e:
                responseObject = {
                    'status': 'fail',
                    'message': 'Some error occurred. Please try again.',
                    'error': str(e)
                }
                return make_response(jsonify(responseObject)), 401

        else:
            responseObject = {
                'status': 'fail',
                'message': 'User already exists. Please Log in.',
            }
            return make_response(jsonify(responseObject)), 202
    except Exception as e:
        responseObject = {
            'status': 'fail',
            'message': 'System Error.',
            'error': str(e)
        }
        return make_response(jsonify(responseObject)), 500


@app.route('/api/user/login', methods=['POST'])
def login_user():
    try:
        data = request.get_json()
        print(f"data from post login request {data}")
        try:
            if data.get('username'):
                print("Login by username")
                user = User.query.filter_by(
                    username=data.get('username')
                ).first()
            else:
                print("Login by email")
                user = User.query.filter_by(
                    email=data.get('email')
                ).first()
            if user:
                if bcrypt.check_password_hash(
                user.password, data.get('password')
                ):
                    auth_token = user.encode_auth_token(user.id)
                    if auth_token:
                        responseObject = {
                            'status': 'success',
                            'message': 'Successfully logged in.',
                            'auth_token': auth_token.decode()
                        }
                        return make_response(jsonify(responseObject)), 200
                else:
                    responseObject = {
                        'status': 'fail',
                        'message': 'Password Incorrect'
                    }
                    return make_response(jsonify(responseObject)), 404

            else:
                responseObject = {
                    'status': 'fail',
                    'message': 'User does not exist.'
                }
                return make_response(jsonify(responseObject)), 404

        except Exception as e:
            responseObject = {
                'status': 'fail',
                'message': 'Try again',
                'error': str(e)
            }
            return make_response(jsonify(responseObject)), 500
    except Exception as e:
        responseObject = {
            'status': 'fail',
            'message': 'System Error.',
            'error': str(e)
        }
        return make_response(jsonify(responseObject)), 500


@app.route('/api/user/status', methods=['GET'])
def status_user():
    try:
        auth_header = request.headers.get('Authorization')
        print(f"auth_header {auth_header}")
        if auth_header:
            try:
                auth_token = auth_header.split(" ")[1]
            except IndexError:
                responseObject = {
                    'status': 'fail',
                    'message': 'Bearer token malformed.'
                }
                return make_response(jsonify(responseObject)), 401
        else:
            auth_token = ''

        if auth_token:
            resp = User.decode_auth_token(auth_token)
            print(f"response of token decode")
            if not isinstance(resp, str):
                user = User.query.filter_by(id=resp).first()
                responseObject = {
                    'status': 'success',
                    'data': {
                        'user_id': user.id,
                        'email': user.email,
                        'username': user.username,
                        'creation_date': user.creation_date
                    }
                }
                return make_response(jsonify(responseObject)), 200

            responseObject = {
                'status': 'fail',
                'message': resp
            }
            return make_response(jsonify(responseObject)), 401
        else:
            responseObject = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return make_response(jsonify(responseObject)), 401
    except Exception as e:
        responseObject = {
            'status': 'fail',
            'message': 'System Error.',
            'error': str(e)
        }
        return make_response(jsonify(responseObject)), 500


@app.route('/api/user/log_out', methods=['POST'])
def log_out_user():
    try:
        pass
    except Exception as e:
        responseObject = {
            'status': 'fail',
            'message': 'System Error.',
            'error': str(e)
        }
        return make_response(jsonify(responseObject)), 500
