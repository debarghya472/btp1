
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

model=pickle.load(open('c:/Users/adhyansh/Desktop/web demo/final_Demo/final/api/model.pkl','rb'))

@app.after_request
# def resizeGrayCenter(img):
#     print(type(img))
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     img = cv2.resize(img, (600, 300), interpolation = cv2.INTER_AREA)
#     img = img - img.mean()
#     return img



# def sampleimage():
    
#     simg=cv2.imread("C:/Users/adhyansh/currency detection/2kd1.jpg")
#     sampleimg=[]
    
#     # simg = resizeGrayCenter(simg)
#     # cv2.imshow('img',simg)
#     # cv2.waitKey(0)
#     sampleimg.append((np.var(simg),skew(simg,axis=None),kurtosis(simg,axis=None),skimage.measure.shannon_entropy(simg)))
#     return sampleimg[0]


# @app.route("/", methods=["GET"])
# def home():
#     return json.dumps("hello home")

  
@app.route("/predict", methods=["GET"])
def predict():
        # v,s,k,e=sampleimage()
        # new_banknote = pd.DataFrame({'variance':[v],'skewness':[s],'kurtosis':[k],'entropy':[e]})

        # # print(f'Prediction:  Class{knn.predict(new_banknote)}')
        # if model.predict(new_banknote)==1:
        #     json_obj = json.dumps("Note is real")
        #     return json_obj
        # else:
        #     json_obj = json.dumps("Note is fake")
        #     return json_obj
        return json.dumps("hello")


if __name__ == "__main__":
    app.run(debug=True)
