from flask import Blueprint, jsonify
from .db_sicei import alumnos, profesores

bp = Blueprint('sicei', __name__)

@bp.route('/sicei/alumnos', methods=['GET'])
def obtener_alumnos():
    return jsonify(alumnos[:10])

@bp.route('/sicei/profesores', methods=['GET'])
def obtener_profesores():
    return jsonify(profesores[:10])