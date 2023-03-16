import requests

url = 'http://127.0.0.1:8080/predict'  # Set destination URL here

request = requests.post(url=url,
                        json={
                            'model_data': {
                                "No": "414",
                                "transaction_date": "2013.500",
                                "house_age": "6.5",
                                "distance_to_the_nearest_MRT_station": "90.45606",
                                "number_of_convenience_stores": "9",
                                "latitude": "24.97433",
                                "longitude": "121.5431"
                            },
                            'dropped_columns': ['No', 'transaction_date', 'house_age']
                        },

                        headers={"Content-Type": "application/json"},
                        )
response = request.text
print('label= ', 63.9)
print(response)
