
from flask import Blueprint, jsonify, request
from .calculator import calculate_demo_score
from .database import save_demo_calculation

api = Blueprint("api", __name__, url_prefix="/api")


@api.get("/health")
def health():
    return jsonify({"status": "ok"})


@api.post("/calculate")
def calculate():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "JSON object required"}), 400

    age = data.get("age")
    smoking = data.get("smoking")
    family_history = data.get("family_history")

    if type(age) is not int or not 18 <= age <= 100:
        return jsonify({"error": "Invalid age"}), 400

    if smoking not in ("never", "former", "current"):
        return jsonify({"error": "Invalid smoking status"}), 400

    if type(family_history) is not bool:
        return jsonify({"error": "Invalid family history"}), 400

    score = calculate_demo_score(age, smoking, family_history)
    record_id = save_demo_calculation(age, smoking, family_history, score)

    return jsonify({
        "id": record_id,
        "demo_score": score,
        "max_score": 100,
        "disclaimer": (
            "Fictional educational score only. "
            "Not a medical prediction."
        )
    })
