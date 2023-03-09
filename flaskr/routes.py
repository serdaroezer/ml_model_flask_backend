from flask import Blueprint, request, make_response, jsonify
from flaskr.models import House
from flaskr.service import make_prediction

pr_bp = Blueprint('routes', __name__)


@pr_bp.route('/predict', methods=['POST', 'GET'])
def predict():
    data = request.get_json(silent=True)
    h = House()
    h.dictionary_to_object(data)
    result=make_prediction(data=h.pandas_dataframe())

    return make_response(jsonify({"prediction": str(result[0])}), 200)

