#!/usr/bin/python3
"""Place related endpoints"""
from api.v1.views import app_views
from api.v1.views import *
from flask import jsonify, make_response, abort, request
from models import storage
from models.review import Review

model = "Review"
parent_model = "Place"


@app_views.route("/places/<place_id>/reviews", strict_slashes=False,
                 methods=["GET"])
def get_reviews(place_id):
    """getting /place api way"""
    return get_models(parent_model, place_id, "reviews")


@app_views.route("/reviews/<review_id>", methods=["GET"])
def get_review(review_id):
    """getting /review api way"""
    return get_model(model, review_id)


@app_views.route("/reviews/<review_id>", methods=["DELETE"])
def delete_review(review_id):
    """deleting /review api way"""
    return delete_model(model, review_id)


@app_views.route("/places/<place_id>/reviews", strict_slashes=False,
                 methods=["POST"])
def post_review(place_id):
    """posting /reviews api way"""
    required_data = {"text", "user_id"}
    return post_model(model, parent_model, place_id, required_data)


@app_views.route("/reviews/<review_id>", methods=["PUT"])
def put_review(review_id):
    """putting /reviews api way"""
    ignore_data = ["id", "created_at", "updated_at", "user_id", "place_id"]
    return put_model(model, review_id, ignore_data)
