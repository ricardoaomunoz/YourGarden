from flask import render_template, request
import datetime
from models import Plant
from app import app, db


@app.route('/', methods=['GET'])
def hello():
    return "HEllo World"

@app.route('/register_plant', methods=['GET', 'POST'])
def add_plant():
    print("ENtro a ruta register plant")
    if request.method == 'GET':
        return render_template('add.html')
    print("POST METHOD")
    print(f"request args: {request.json}")
    banco=request.json.get('seed_bank')
    comentario=request.json.get('comment')
    fecha_ingreso=datetime.datetime.now()
    meta_data=request.json.get('meta_data')
    sustrato=request.json.get('substrate')
    volumen_matera=request.json.get('matera_size')
    germination_type_id=request.json.get('germination_type_id')
    planting_technique_id=request.json.get('planting_technique_id')
    stage_id=request.json.get('stage_id')
    plants_user_id=request.json.get('plants_user_id')

    try:
        plant = Plant(
            banco=banco,
            comentario=comentario,
            fecha_ingreso=fecha_ingreso,
            meta_data=meta_data,
            sustrato=sustrato,
            volumen_matera=volumen_matera,
            germination_type_id=germination_type_id,
            planting_technique_id=planting_technique_id,
            stage_id=stage_id,
            plants_user_id=plants_user_id

        )
        db.session.add(plant)
        db.session.commit()
        return "Plant added. plant id={}".format(plant.id)
    except Exception as e:
        return(str(e))