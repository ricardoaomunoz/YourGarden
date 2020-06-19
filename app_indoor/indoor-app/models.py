# coding: utf-8
from sqlalchemy import Boolean, Column, Date, Float, ForeignKey, Integer, LargeBinary, String, Text, Time
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class GerminationType(db.Model):
    __tablename__ = 'germination_type'

    name = db.Column(db.String(20))
    comments = db.Column(db.Text)
    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())



class Growing(db.Model):
    __tablename__ = 'growing'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.String(30))
    plants_user_id = db.Column(db.ForeignKey('plant_user.id', ondelete='CASCADE', onupdate='CASCADE'))

    plants_user = db.relationship('PlantUser', primaryjoin='Growing.plants_user_id == PlantUser.id', backref='growings')



class Peripheral(db.Model):
    __tablename__ = 'peripherals'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.String(30), nullable=False)
    state = db.Column(db.Boolean, nullable=False)
    growing_id = db.Column(db.ForeignKey('growing.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

    growing = db.relationship('Growing', primaryjoin='Peripheral.growing_id == Growing.id', backref='peripherals')



class Plant(db.Model):
    __tablename__ = 'plant'

    banco = db.Column(db.Boolean)
    comentario = db.Column(db.Text)
    fecha_ingreso = db.Column(db.Date)
    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    meta_data = db.Column(db.Text)
    sustrato = db.Column(db.String(30))
    volumen_matera = db.Column(db.Float(53))
    germination_type_id = db.Column(db.ForeignKey('germination_type.id'), nullable=False)
    planting_technique_id = db.Column(db.ForeignKey('planting_technique.id'), nullable=False)
    stage_id = db.Column(db.ForeignKey('stage.id'), nullable=False)
    plants_user_id = db.Column(db.ForeignKey('plant_user.id'))
    imagen = db.Column(db.LargeBinary)
    growing_id = db.Column(db.ForeignKey('growing.id', ondelete='CASCADE', onupdate='CASCADE'))
    nikname = db.Column(db.String(30))

    germination_type = db.relationship('GerminationType', primaryjoin='Plant.germination_type_id == GerminationType.id', backref='plants')
    growing = db.relationship('Growing', primaryjoin='Plant.growing_id == Growing.id', backref='plants')
    planting_technique = db.relationship('PlantingTechnique', primaryjoin='Plant.planting_technique_id == PlantingTechnique.id', backref='plants')
    plants_user = db.relationship('PlantUser', primaryjoin='Plant.plants_user_id == PlantUser.id', backref='plants')
    stage = db.relationship('Stage', primaryjoin='Plant.stage_id == Stage.id', backref='plants')



class PlantHistory(db.Model):
    __tablename__ = 'plant_history'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    seed_bank = db.Column(db.Boolean)
    comments = db.Column(db.Text)
    start_date = db.Column(db.Date)
    plant_id = db.Column(db.Integer)
    meta_data = db.Column(db.Text)
    substrate = db.Column(db.String(30))
    matera_size = db.Column(db.Float(53))
    germination_type_id = db.Column(db.ForeignKey('germination_type.id', ondelete='CASCADE', onupdate='CASCADE'))
    planting_technique_id = db.Column(db.ForeignKey('planting_technique.id', ondelete='CASCADE', onupdate='CASCADE'))
    stage_id = db.Column(db.ForeignKey('stage.id', ondelete='CASCADE', onupdate='CASCADE'))
    user_system = db.Column(db.String(250))
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    plant_user_id = db.Column(db.ForeignKey('plant_user.id', ondelete='CASCADE', onupdate='CASCADE'))
    imagen = db.Column(db.LargeBinary)
    growing_id = db.Column(db.ForeignKey('growing.id', ondelete='CASCADE', onupdate='CASCADE'))

    germination_type = db.relationship('GerminationType', primaryjoin='PlantHistory.germination_type_id == GerminationType.id', backref='plant_histories')
    growing = db.relationship('Growing', primaryjoin='PlantHistory.growing_id == Growing.id', backref='plant_histories')
    plant_user = db.relationship('PlantUser', primaryjoin='PlantHistory.plant_user_id == PlantUser.id', backref='plant_histories')
    planting_technique = db.relationship('PlantingTechnique', primaryjoin='PlantHistory.planting_technique_id == PlantingTechnique.id', backref='plant_histories')
    stage = db.relationship('Stage', primaryjoin='PlantHistory.stage_id == Stage.id', backref='plant_histories')



class PlantUser(db.Model):
    __tablename__ = 'plant_user'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.String(50))
    nit = db.Column(db.String(30))
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))



class PlantingTechnique(db.Model):
    __tablename__ = 'planting_technique'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.String(30))
    comments = db.Column(db.Text)



class Sensor(db.Model):
    __tablename__ = 'sensors'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    name = db.Column(db.String(30), nullable=False)
    value = db.Column(db.Integer, nullable=False)
    unit = db.Column(db.String(20), nullable=False)
    growing_id = db.Column(db.ForeignKey('growing.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)

    growing = db.relationship('Growing', primaryjoin='Sensor.growing_id == Growing.id', backref='sensors')



class Stage(db.Model):
    __tablename__ = 'stage'

    name = db.Column(db.String(30))
    comments = db.Column(db.Text)
    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
