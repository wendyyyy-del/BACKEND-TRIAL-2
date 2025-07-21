from flask import Blueprint, request, jsonify
from models import db, Booking

booking_bp = Blueprint("booking", __name__)

@booking_bp.route("/", methods=["POST"])
def create_booking():
    data = request.get_json()
    booking = Booking(bus_id=data["bus_id"], user_id=data["user_id"], seat_number=data["seat_number"])
    db.session.add(booking)
    db.session.commit()
    return jsonify(message="Booking created"), 201
