"""TripNote web app."""
import fitz  # PyMuPDF, used to export itineraries as PDF
import yaml
from flask import Flask, jsonify, request

import config
from signup import create_user

app = Flask(config.APP_NAME)


@app.post("/signup")
def signup():
    body = request.get_json()
    user = create_user(body["email"], body["password_hash"], body["lat"], body["lon"])
    return jsonify({"id": user["id"]}), 201


@app.post("/import")
def import_itinerary():
    return jsonify(yaml.load(request.data, Loader=yaml.Loader))


@app.get("/export/<trip_id>.pdf")
def export(trip_id: str):
    doc = fitz.open()
    doc.new_page().insert_text((72, 72), f"Trip {trip_id}")
    return doc.tobytes(), 200, {"Content-Type": "application/pdf"}
