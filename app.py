
from flask import Flask, request
from flask_cors import CORS, cross_origin

import os
import json
import pickle
import cv2
import numpy as np
from scipy.stats import kurtosis, skew
from scipy import ndimage
import skimage.measure
import pandas as pd

app = Flask(__name__)
cors = CORS(app)

model = pickle.load(open('./model.pkl', 'rb'))


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    return json.dumps("predict")


@app.route('/', methods=['GET'])
def helloworld():
    if(request.method == 'GET'):

        return json.dumps("hello")


if __name__ == '__main__':
    app.run(debug=True)
