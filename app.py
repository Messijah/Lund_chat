from flask import Flask, jsonify
from skolverket_api import SkolverketAPI

app = Flask(__name__)
skolverket_api = SkolverketAPI()

@app.route("/")
def home():
    return "Välkommen till Skolverkets API-server!"

@app.route("/subjects", methods=["GET"])
def get_subjects():
    subjects_data = skolverket_api.get_subjects()
    if subjects_data and "subjects" in subjects_data:
        subjects = subjects_data["subjects"]
        return jsonify(subjects)
    else:
        return jsonify({"error": "Kunde inte hämta ämneslistan"}), 500

if __name__ == "__main__":
    app.run(debug=True)






