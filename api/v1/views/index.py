#!/usr/bin/python3
"""app_views /status way"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=["GET"])
def status():
    """Return /status api way"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=["GET"])
def stats():
    """Return /status api way"""
    d = {
        "amenities": "Amenity",
        "cities": "City",
        "places": "Place",
        "reviews": "Review",
        "states": "State",
        "users": "User"
    }
    d = {k: storage.count(v) for k, v in d.items()}
    return jsonify(d)
