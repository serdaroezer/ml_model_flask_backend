from flask import Blueprint, request, make_response, jsonify
from flaskr.models import House

pr_bp = Blueprint('routes', __name__)


@pr_bp.route('/predict', methods=['POST', 'GET'])
def predict():
    data = request.get_json(silent=True)
    h = House()
    h.dictionary_to_object(data)

    # House.from_json(data)

    return make_response(jsonify({"prediction": "2.3"}), 200)
    # return {"prediction": "2.3"}
