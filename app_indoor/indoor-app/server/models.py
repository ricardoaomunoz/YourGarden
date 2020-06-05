# coding: utf-8
from sqlalchemy import Boolean, Column, Date, Float, ForeignKey, Integer, String, Text, Time
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import relationship
from app import db



class GerminationType(db.Model):
    __tablename__ = 'germination_type'

    name = db.Column(db.String(20))
    comments = db.Column(db.Text)
    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())



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

    germination_type = db.relationship('GerminationType', primaryjoin='Plant.germination_type_id == GerminationType.id', backref='plants')
    planting_technique = db.relationship('PlantingTechnique', primaryjoin='Plant.planting_technique_id == PlantingTechnique.id', backref='plants')
    plants_user = db.relationship('PlantUser', primaryjoin='Plant.plants_user_id == PlantUser.id', backref='plants')
    stage = db.relationship('Stage', primaryjoin='Plant.stage_id == Stage.id', backref='plants')

    def __init__(self, banco, comentario, fecha_ingreso, meta_data, sustrato, volumen_matera, germination_type_id, planting_technique_id, stage_id, plants_user_id):
        self.banco = banco
        self.comentario = comentario
        self.fecha_ingreso = fecha_ingreso
        self.meta_data = meta_data
        self.sustrato = sustrato
        self.volumen_matera = volumen_matera
        self.germination_type_id = germination_type_id
        self.planting_technique_id = planting_technique_id
        self.stage_id = stage_id
        self.plants_user_id = plants_user_id

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'comentario':self.comentario
        }

class PlantHistory(db.Model):
    __tablename__ = 'plant_history'

    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
    seed_bank = db.Column(db.Boolean)
    comments = db.Column(db.Text)
    start_date = db.Column(db.Date)
    meta_data = db.Column(db.Text)
    plant_id = db.Column(db.Integer)
    substrate = db.Column(db.String(30))
    matera_size = db.Column(db.Float(53))
    germination_type_id = db.Column(db.Integer)
    planting_technique_id = db.Column(db.Integer)
    stage_id = db.Column(db.Integer)
    user_system = db.Column(db.String(250))
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    plant_user_id = db.Column(db.Integer)



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



class Stage(db.Model):
    __tablename__ = 'stage'

    name = db.Column(db.String(30))
    comments = db.Column(db.Text)
    id = db.Column(db.Integer, primary_key=True, server_default=db.FetchedValue())
