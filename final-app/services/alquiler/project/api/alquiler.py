from flask import Blueprint, jsonify, request, render_template

from project.api.models import Alquiler
from project.api.models import Cliente
from project.api.models import Empleado
from project.api.models import Pelicula
from project.api.models import Alq_Pel
from sqlalchemy import exc
from project import db


#alquiler_blueprint = Blueprint('alquiler', __name__)
alquiler_blueprint = Blueprint('alquiler', __name__, template_folder='./templates')


@alquiler_blueprint.route('/alquiler/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })


@alquiler_blueprint.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@alquiler_blueprint.route('/alquiler', methods=['POST'])
def add_alquiler():
    post_data = request.get_json()
    fecha_alqui = post_data.get('fecha_alqui')
    fecha_devol = post_data.get('fecha_devol')
    id_cliente = post_data.get('id_cliente')
    id_empleado = post_data.get('id_empleado')
    db.session.add(Alquiler(fecha_alqui=fecha_alqui, fecha_devol=fecha_devol, id_cliente=id_cliente, id_empleado=id_empleado))
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': f'{email} was added!'
    }
    return jsonify(response_object), 201


@alquiler_blueprint.route('/alquileres/<alquiler_id>', methods=['GET'])
def get_single_alquiler(alquiler_id):
    alquiler = Alquiler.query.filter_by(id=alquiler_id).first()
    response_object = {
        'status': 'satisfactorio',
        'data': {
            'id'.alquiler.id,
            'fecha_alqui'.alquiler.fecha_alqui,
            'fecha_devol'.alquiler.fecha_devol,
            'id_cliente'.alquiler.id_cliente,
            'id_empleado'.alquiler.id_empleado,
            'active'.alquiler.active
        }
    }
    return jsonify(response_object), 200


@alquiler_blueprint.route('/alquileres', methods=['GET'])
def get_all_alquileres():
    """"Obteniendo todos los alquileres"""
    response_object = {
        'status' : 'success',
        'data': {
            'alquiler':[alquiler.to_json() for alquiler in Alquiler.query.all()]
        }
    }
    return jsonify(response_object), 200


@alquiler_blueprint.route('/clientes', methods=['POST'])
def add_clientes():
    post_data = request.get_json()
    nombre = post_data.get('nombre')
    apellido = post_data.get('apellido')
    db.session.add(nombre=nombre, apellido=apellido)
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': f'{nombre} was added!'
    }
    return jsonify(response_object), 201


@alquiler_blueprint.route('/clientes/<cliente_id>', methods=['GET'])
def get_single_cliente(cliente_id):
    cliente = Cliente.query.filter_by(id=cliente_id).first()
    response_object = {
        'status': 'satisfactorio',
        'data': {
            'id'.cliente.id,
            'nombre'.cliente.nombre,
            'apellido'.cliente.apellido,
            'active'.cliente.active
        }
    }
    return jsonify(response_object), 200


@alquiler_blueprint.route('/clientes', methods=['GET'])
def get_all_clientes():
    """"Obteniendo todos los clientes"""
    response_object = {
        'status' : 'success',
        'data': {
            'clientes':[Cliente.to_json() for Cliente in Cliente.query.all()]
        }
    }
    return jsonify(response_object), 200


@alquiler_blueprint.route('/empleados', methods=['POST'])
def add_empleado():
    post_data = request.get_json()
    nombre = post_data.get('nombre')
    apellido = post_data.get('apellido')
    db.session.add(nombre=nombre, apellido=apellido)
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': f'{nombre} was added!'
    }
    return jsonify(response_object), 201


@alquiler_blueprint.route('/empleados/<empleado_id>', methods=['GET'])
def get_single_empleado(empleado_id):
    empleado = Empleado.query.filter_by(id=empleado_id).first()
    response_object = {
        'status': 'satisfactorio',
        'data': {
            'id'.empleado.id,
            'nombre'.empleado.nombre,
            'apellido'.empleado.apellido,
            'active'.empleado.active
        }
    }
    return jsonify(response_object), 200


@alquiler_blueprint.route('/empleados', methods=['GET'])
def get_all_empleados():
    """"Obteniendo todos los empleados"""
    response_object = {
        'status' : 'success',
        'data': {
            'empleados':[Empleado.to_json() for Empleado in Empleado.query.all()]
        }
    }
    return jsonify(response_object), 200


@alquiler_blueprint.route('/peliculas', methods=['POST'])
def add_pelicula():
    post_data = request.get_json()
    nombre = post_data.get('nombre')
    genero = post_data.get('genero')
    fecha_lanzamiento = post_data.get('fecha_lanzamiento')
    db.session.add(nombre=nombre, genero=genero, fecha_lanzamiento=fecha_lanzamiento)
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': f'{nombre} was added!'
    }
    return jsonify(response_object), 201


@alquiler_blueprint.route('/peliculas/<pelicula_id>', methods=['GET'])
def get_single_pelicula(pelicula_id):
    pelicula = Pelicula.query.filter_by(id=pelicula_id).first()
    response_object = {
        'status': 'satisfactorio',
        'data': {
            'id'.pelicula.id,
            'nombre'.pelicula.nombre,
            'genero'.pelicula.genero,
            'fecha_lanzamiento'.pelicula.fecha_lanzamiento,
            'active'.pelicula.active
        }
    }
    return jsonify(response_object), 200


@alquiler_blueprint.route('/peliculas', methods=['GET'])
def get_all_peliculas():
    """"Obteniendo todos los peliculas"""
    response_object = {
        'status' : 'success',
        'data': {
            'peliculas':[Pelicula.to_json() for Pelicula in Pelicula.query.all()]
        }
    }
    return jsonify(response_object), 200


@alquiler_blueprint.route('/alq_pel', methods=['POST'])
def add_alq_pel():
    post_data = request.get_json()
    id_alquiler = post_data.get('id_alquiler')
    id_pelicula = post_data.get('id_pelicula')
    db.session.add(id_alquiler=id_alquiler, id_pelicula=id_pelicula)
    db.session.commit()
    response_object = {
        'status': 'success',
        'message': f'{id_alquiler} was added!'
    }
    return jsonify(response_object), 201


@alquiler_blueprint.route('/alq_pel/<alq_pel_id>', methods=['GET'])
def get_single_alq_pel(empleado_id):
    alq_pel = Alq_Pel.query.filter_by(id=alq_pel_id).first()
    response_object = {
        'status': 'satisfactorio',
        'data': {
            'id'.alq_pel.id,
            'id_alquiler'.alq_pel.id_alquiler,
            'id_pelicula'.alq_pel.id_pelicula,
            'active'.empleado.active
        }
    }
    return jsonify(response_object), 200


@alquiler_blueprint.route('/alq_pel', methods=['GET'])
def get_all_alq_pels():
    """"Obteniendo todos los Alq_Pels"""
    response_object = {
        'status' : 'success',
        'data': {
            'peliculas':[Alq_Pel.to_json() for Alq_Pel in Alq_Pel.query.all()]
        }
    }
    return jsonify(response_object), 200
