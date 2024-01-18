from flask import Flask,render_template,redirect,url_for,request
import pickle
import numpy as np
import pandas as pd
import re
import warnings

application = Flask(__name__)


filename = open('HP/hpmodel.pkl', 'rb')
model = pickle.load(filename)
filename.close()

@application.route('/')
def index():
	return render_template('home.html')

@application.route('/home')
def home():
	return render_template('home.html')


@application.route('/hppredict', methods=['GET','POST'])
def hppredict():
    if request.method == "POST":

        na = request.form['na']
        AAI = float(request.form['AAI'])
        AAHA = float(request.form['AAHA'])
        AANR = float(request.form['AANR'])
        AANB = float(request.form['AANB'])
        AP = float(request.form['AP'])

        dat = np.array([[AAI,AAHA,AANR,AANB,AP]])
        my_prediction = model.predict(dat)
        result=round(my_prediction[0],2)
        print(result)

        return render_template('hpshow.html',name=na,result=result)
    return render_template('hp.html')




if __name__ == '__main__':
	application.run(debug=True)

