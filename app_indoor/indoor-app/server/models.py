# coding: utf-8
from sqlalchemy import Boolean, Column, Date, DateTime, Float, ForeignKey, Integer, JSON, String, Text
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql.base import ENUM
from flask_sqlalchemy import SQLAlchemy
import datetime

import jwt
from app import db, bcrypt, app





class Fertilizer(db.Model):
    __tablename__ = 'fertilizer'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.String, nullable=False)
    descriptions = db.Column(db.Text, nullable=False)



class Garden(db.Model):
    __tablename__ = 'garden'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.String, nullable=False)
    width = db.Column(db.Float(53), nullable=False)
    height = db.Column(db.Float(53), nullable=False)
    length = db.Column(db.Float(53), nullable=False)
    user_id = db.Column(db.ForeignKey('user.id'), nullable=False)

    user = db.relationship('User', primaryjoin='Garden.user_id == User.id', backref='gardens')



class Plant(db.Model):
    __tablename__ = 'plant'

    enum = ENUM('female', 'male', 'hermaphrodite', 'n/a', name='sex')
    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    garden_id = db.Column(db.ForeignKey('garden.id'), nullable=False)
    nick_name = db.Column(db.String, nullable=False)
    seed_bank = db.Column(db.Boolean, nullable=False)
    sex = db.Column(enum, nullable=False)
    commends = db.Column(db.Text, nullable=False)
    meta_data = db.Column(db.JSON, nullable=False)
    plant_species_id = db.Column(db.ForeignKey('plant_species.id'), nullable=False)
    ini_date = db.Column(db.Date, nullable=False)

    garden = db.relationship('Garden', primaryjoin='Plant.garden_id == Garden.id', backref='plants')
    plant_species = db.relationship('PlantSpecy', primaryjoin='Plant.plant_species_id == PlantSpecy.id', backref='plants')



class PlantHistory(db.Model):
    __tablename__ = 'plant_history'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    time_stamp = db.Column(db.DateTime, nullable=False)
    plant_id = db.Column(db.ForeignKey('plant.id'), nullable=False)
    plant_stage_id = db.Column(db.ForeignKey('plant_stage.id'), nullable=False)
    container_width = db.Column(db.Float(53), nullable=False)
    container_height = db.Column(db.Float(53), nullable=False)
    container_length = db.Column(db.Float(53), nullable=False)
    symptom_id = db.Column(db.ForeignKey('symptom.id'), nullable=False)
    fertilizer_id = db.Column(db.ForeignKey('fertilizer.id'), nullable=False)
    substrate_id = db.Column(db.ForeignKey('substrate.id'), nullable=False)

    fertilizer = db.relationship('Fertilizer', primaryjoin='PlantHistory.fertilizer_id == Fertilizer.id', backref='plant_histories')
    plant = db.relationship('Plant', primaryjoin='PlantHistory.plant_id == Plant.id', backref='plant_histories')
    plant_stage = db.relationship('PlantStage', primaryjoin='PlantHistory.plant_stage_id == PlantStage.id', backref='plant_histories')
    substrate = db.relationship('Substrate', primaryjoin='PlantHistory.substrate_id == Substrate.id', backref='plant_histories')
    symptom = db.relationship('Symptom', primaryjoin='PlantHistory.symptom_id == Symptom.id', backref='plant_histories')



class PlantSpecy(db.Model):
    __tablename__ = 'plant_species'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.String, nullable=False)



class PlantStage(db.Model):
    __tablename__ = 'plant_stage'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.String, nullable=False)



class Sensor(db.Model):
    __tablename__ = 'sensor'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    sensor_type_id = db.Column(db.ForeignKey('sensor_type.id'), nullable=False)
    serial = db.Column(db.String, nullable=False)
    garden_id = db.Column(db.ForeignKey('garden.id'), nullable=False)
    ini_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date)
    end_user = db.Column(db.Integer)

    garden = db.relationship('Garden', primaryjoin='Sensor.garden_id == Garden.id', backref='sensors')
    sensor_type = db.relationship('SensorType', primaryjoin='Sensor.sensor_type_id == SensorType.id', backref='sensors')



class SensorHistory(db.Model):
    __tablename__ = 'sensor_history'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    value = db.Column(db.JSON, nullable=False)
    time_stamp = db.Column(db.Integer, nullable=False)
    sensor_id = db.Column(db.ForeignKey('sensor.id'), nullable=False)
    user_id = db.Column(db.ForeignKey('user.id'), nullable=False)
    status_id = db.Column(db.ForeignKey('status.id'), nullable=False)

    sensor = db.relationship('Sensor', primaryjoin='SensorHistory.sensor_id == Sensor.id', backref='sensor_histories')
    status = db.relationship('Status', primaryjoin='SensorHistory.status_id == Status.id', backref='sensor_histories')
    user = db.relationship('User', primaryjoin='SensorHistory.user_id == User.id', backref='sensor_histories')



class SensorType(db.Model):
    __tablename__ = 'sensor_type'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    unit_type_id = db.Column(db.ForeignKey('unit_type.id'), nullable=False)
    name = db.Column(db.String, nullable=False)

    unit_type = db.relationship('UnitType', primaryjoin='SensorType.unit_type_id == UnitType.id', backref='sensor_types')



class Status(db.Model):
    __tablename__ = 'status'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.Integer, nullable=False)



class Substrate(db.Model):
    __tablename__ = 'substrate'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)



class Switch(db.Model):
    __tablename__ = 'switch'

    enum = ENUM('manual', 'automaitc', 'interval', name='ejecution')
    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    switch_type_id = db.Column(db.ForeignKey('switch_type.id'), nullable=False)
    ejecution = db.Column(enum, nullable=False)
    on_time = db.Column(db.DateTime)
    off_time = db.Column(db.DateTime)
    interval_on = db.Column(db.DateTime)
    interval_off = db.Column(db.DateTime)
    garden_id = db.Column(db.ForeignKey('garden.id'), nullable=False)

    garden = db.relationship('Garden', primaryjoin='Switch.garden_id == Garden.id', backref='switches')
    switch_type = db.relationship('SwitchType', primaryjoin='Switch.switch_type_id == SwitchType.id', backref='switches')



class SwitchHistory(db.Model):
    __tablename__ = 'switch_history'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    switch_id = db.Column(db.ForeignKey('switch.id'), nullable=False)
    time_stamp = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.ForeignKey('user.id'), nullable=False)
    status_id = db.Column(db.ForeignKey('status.id'), nullable=False)

    status = db.relationship('Status', primaryjoin='SwitchHistory.status_id == Status.id', backref='switch_histories')
    switch = db.relationship('Switch', primaryjoin='SwitchHistory.switch_id == Switch.id', backref='switch_histories')
    user = db.relationship('User', primaryjoin='SwitchHistory.user_id == User.id', backref='switch_histories')



class SwitchType(db.Model):
    __tablename__ = 'switch_type'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.String, nullable=False)



class Symptom(db.Model):
    __tablename__ = 'symptom'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=False)



class UnitType(db.Model):
    __tablename__ = 'unit_type'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    symbol = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)



class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    creation_date = db.Column(db.Date, nullable=False)
    email = db.Column(db.String, nullable=False)

    def __init__(self, username, password, email):
        self.email = email
        self.username = username
        self.password = bcrypt.generate_password_hash(
            password, app.config.get('BCRYPT_LOG_ROUNDS')
        ).decode()
        self.creation_date = datetime.datetime.now()

    def encode_auth_token(self, user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=25),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Validates the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'


class BlacklistToken(db.Model):
    """
    Token Model for storing JWT tokens
    """
    __tablename__ = 'blacklist_token'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(500), unique=True, nullable=False)
    blacklisted_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, token):
        self.token = token
        self.blacklisted_on = datetime.datetime.now()

    def __repr__(self):
        return '<id: token: {}'.format(self.token)

    @staticmethod
    def check_blacklist(auth_token):
        # check whether auth token has been blacklisted
        res = BlacklistToken.query.filter_by(token=str(auth_token)).first()
        if res:
            return True
        else:
            return False