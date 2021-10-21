from flask import Flask, jsonify, request
import json
from flask_cors import CORS, cross_origin

import os
import pickle
import cv2
import numpy as np
from scipy.stats import kurtosis, skew
from scipy import ndimage
import skimage.measure
import pandas as pd
  
app = Flask(__name__)
cors = CORS(app)  

model=pickle.load(open('c:/Users/adhyansh/Desktop/web demo/final_Demo/final/api/model.pkl','rb'))

@app.after_request

@app.route('/predict', methods=['GET','POST'])
def predict():
    return json.dumps("predict")

@app.route('/', methods=['GET'])
def helloworld():
    if(request.method == 'GET'):
        
        return json.dumps("hello")  
  
if __name__ == '__main__':
    app.run(debug=True)