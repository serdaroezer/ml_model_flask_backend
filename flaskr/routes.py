from flask import Blueprint, request, make_response, jsonify
from flaskr.models import House
from flaskr.service import make_prediction
from ml_module import create_model

model=create_model('polynomial')

pr_bp = Blueprint('routes', __name__)


@pr_bp.route('/predict', methods=['POST', 'GET'])
def predict():
    json_data = request.get_json(silent=True)
    house = House()
    house.json_to_object(json_data)
    result = model.predict(data=house.object_to_pandas_dataframe())

    return make_response(jsonify({"prediction": str(result[0])}), 200)
