from flask import Blueprint, request, make_response, jsonify
from flaskr.models import House
from ml_module import create_model

pr_bp = Blueprint('routes', __name__)


# TODO set criteria through api call
model = create_model(criteria='ridge_regression')


@pr_bp.route('/predict', methods=['POST', 'GET'])
def predict():
    json_data = request.get_json(silent=True)
    house = House()
    house.json_to_object(json_data['model_data'])
    df = house.object_to_pandas_dataframe()
    df = house.drop_columns(df, json_data['dropped_columns'])
    df = house.mean_normalize(df)
    result = model.predict(data=df)

    return make_response(jsonify({"prediction": str(result[0])}), 200)
