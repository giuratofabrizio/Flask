from flask import Flask,render_template, request, Response, redirect, url_for
app = Flask(__name__)

import io
import pandas as pd
import geopandas as gpd
import contextily
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


stazioni=pd.read_csv('/workspace/Flask/CorrezioneVerificaA/coordfix_ripetitori_radiofonici_milano_160120_loc_final.csv', sep=';')
radio=gpd.read_file('/workspace/Flask/CorrezioneVerificaA/quartieri.geojson')
qrt=gpd.read_file('/workspace/Flask/AppEs6/static/ds964_nil_wm-20220322T104009Z-001.zip')

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/radiob', methods=['GET'])
def radiob():
    return render_template('radqrt.html',qrt=qrt.NIL)


@app.route('/radqrt', methods=['GET'])
def radqrt():
    global radsqrts, radsqrts1
    quartiere= request.args['quart']
    qrt_user= qrt[qrt.NIL==quartiere.upper()]
    radsqrts= radio[radio.within(qrt_user.geometry.squeeze())]
    radsqrts1= radsqrts.reset_index().sort_values()
    return render_template('result.html',quartiere=quartiere, tabella=radsqrts1.to_html())