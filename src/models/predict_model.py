from flask import current_app
import numpy as np


class Predictor:

    def __init__(self,
                    year: int,
                    mileage: int,
                    make: int,
                    model: int,
                    body: int,
                    horsepower: int,
                    city: float,
                    highway: float,
                    engine: int,
                    fuel: int,
                    transmission: int,
                    seating: int):
        self.features = []
        self.features.append(year)
        self.features.append(mileage)
        self.features.append(make)
        self.features.append(model)
        self.features.append(body)
        self.features.append(horsepower)
        self.features.append(city)
        self.features.append(highway)
        self.features.append(engine)
        self.features.append(fuel)
        self.features.append(transmission)
        self.features.append(seating)

    def predict_price(self):
        model = current_app.model
        arr = np.array(self.features).reshape((1, -1))
        p = model.predict(arr)
        return p[0]



