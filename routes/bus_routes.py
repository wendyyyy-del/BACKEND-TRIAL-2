from flask import Blueprint, jsonify, request
from models import db, Bus
from flask_jwt_extended import jwt_required

bus_bp = Blueprint("bus", __name__)

@bus_bp.route("/", methods=["GET"])
@jwt_required()
def get_buses():
    buses = Bus.query.all()
    return jsonify([{"id": b.id, "number_plate": b.number_plate, "capacity": b.capacity} for b in buses])
