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

quartieri = gpd.read_file('/workspace/Flask/AppEs6/static/ds964_nil_wm-20220322T104009Z-001.zip')

@app.route('/', methods=['GET'])
def home():
    nomi_qrt= quartieri.NIL.to_list()
    return render_template('home.html',lst_qrt=nomi_qrt)



@app.route('/selezione', methods=['GET'])
def selezione():
    scelta = request.args["scelta"]
    if scelta=="centro":
        return redirect(url_for("quart_geo"))
    elif scelta=="dintorni":
        return redirect(url_for("quart_dint"))


@app.route('/quart_geo', methods=['GET'])
def quart_geo():
    
    return render_template('quart_geo.html')

@app.route('/mappa', methods=['GET'])
def mappa():

    fig, ax = plt.subplots(figsize = (12,8))
    
    quartiere.to_crs(epsg=3857).plot(ax=ax, alpha=0.5)
    contextily.add_basemap(ax=ax)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

@app.route('/quart_dint', methods=['GET'])
def quart_dint():
    
    return render_template('quart_dint.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)