import os
import sys

import pandas as pd
from flask import Flask, jsonify, redirect, render_template, request, url_for
from flask_cors import CORS
from werkzeug.utils import secure_filename

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import sat_solve

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solusction', methods = ['POST'])
def solusction():
    garments = []
    colors = []
    n = int(len(request.form)/2)
    for i in range(n):
        garment = request.form['g'+ str(i)]
        color = request.form['c'+ str(i)]
        garments.append(garment)
        colors.append(color)
    dict = {'garment': garments, 'color': colors} 
    df = pd.DataFrame(dict)
    sol = sat_solve(df)
    return render_template('index.html', data=sol)

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename('input.txt'))
      data = pd.read_csv('input.txt', delimiter=', ', comment='#', engine='python')
      sol = sat_solve(data)
      return render_template('index.html', data=sol)
