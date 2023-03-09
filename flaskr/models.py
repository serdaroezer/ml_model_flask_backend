import pandas as pd


class House(object):
    def __init__(self):
        self.No = None
        self.transaction_date = None
        self.house_age = None
        self.distance_to_the_nearest_MRT_station = None
        self.number_of_convenience_stores = None
        self.latitude = None
        self.longitude = None

    def __int__(self, No, transaction_date, house_age, distance_to_the_nearest_MRT_station,
                number_of_convenience_stores,
                latitude, longitude):
        self.No = No
        self.transaction_date = transaction_date
        self.house_age = house_age
        self.distance_to_the_nearest_MRT_station = distance_to_the_nearest_MRT_station
        self.number_of_convenience_stores = number_of_convenience_stores
        self.latitude = latitude
        self.longitude = longitude

    def json_to_object(self, json_dict):
        self.No = int(json_dict['No'])
        self.transaction_date = float(json_dict['transaction_date'])
        self.house_age = float(json_dict['house_age'])
        self.distance_to_the_nearest_MRT_station = float(json_dict['distance_to_the_nearest_MRT_station'])
        self.number_of_convenience_stores = int(json_dict['number_of_convenience_stores'])
        self.latitude = float(json_dict['latitude'])
        self.longitude = float(json_dict['longitude'])

    def object_to_pandas_dataframe(self):
        return pd.DataFrame(self.__dict__, [0])
