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

#Dichiarazioni delle dataframe
Mezzi=gpd.read_file('/workspace/Flask/tpl_percorsi_shp (1).zip')
quartieri = gpd.read_file('/workspace/Flask/AppEs6/static/ds964_nil_wm-20220322T104009Z-001.zip')

#Home
@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/selezione', methods=['GET'])
def selezione():
    scelta = request.args["scelta"]
    if scelta=="es1":
        return redirect(url_for("kmlong"))
    elif scelta=="es2":
        return redirect(url_for("sceltaqrt"))
    elif scelta=="es3":
        return redirect(url_for("sceltalinea"))

######################################################################################################################################################

@app.route('/kmlong', methods=['GET'])
def lunghezzaKm():
    return render_template('kmlong.html')

@app.route('/map', methods=['GET'])
def MappaFinale():
    global Min,Max,linee_distanza
   
    Min = min(request.args["Kmmin"], request.args["Kmmax"])#ritorna il numero piu piccolo tra i 2 valori
    Max = max(request.args["Kmmin"], request.args["Kmmax"])#ritorna il numero piu grande tra i 2 valori

    linee_distanza = Mezzi[(Mezzi["lung_km"] > Min) & (Mezzi["lung_km"] < Max)].sort_values("linea")
    return render_template("finalmap.html", tabella = linee_distanza.to_html())

@app.route("/mappafinale.png", methods=["GET"])

def mappa2png():
    

    fig, ax = plt.subplots(figsize = (12,8))


    linee_distanza.to_crs(epsg=3857).plot(ax=ax)
    contextily.add_basemap(ax=ax)   

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

######################################################################################################################################################

@app.route('/sceltaqt', methods=['GET'])
def sceltaqt():
    return render_template('sceltaqrt.html')

@app.route('/visualizzamezzi', methods=['GET'])
def visualizzamezzi():
   
    nome_quartiere=request.args["quartiere"]
    quartiere=quartieri[quartieri.NIL.str.contains(nome_quartiere)]
    mezzi_quartiere=Mezzi[Mezzi.intersects(quartiere.geometry.squeeze())]
    mezzi_quartiere=mezzi_quartiere.astype({"linea":int})#solo la colonna divnta un intero 
    
    return render_template('mezzi_visualizza.html',risultato=sorted(list(mezzi_quartiere.linea.drop_duplicates()))) #sorted riordina la lista

######################################################################################################################################################

@app.route('/sceltalinea', methods=['GET'])
def sceltalinea():
    global Mezzi
    Mezzi=Mezzi.astype({"linea":int})

    return render_template('sceltalinea.html',Mezzi=sorted(list(Mezzi.linea.drop_duplicates())))

@app.route('/visualizza', methods=['GET'])
def visualizza():
    global Linea_utente
    Linea_utente=request.args["mezzo"]
    return render_template('visualizza.html')

@app.route("/mappa.png", methods=["GET"])
def mappapng():

    fig, ax = plt.subplots(figsize = (12,8))

    mezzi20=Mezzi[Mezzi.linea==Linea_utente]
    mezzi20.to_crs(epsg=3857).plot(ax=ax)
    contextily.add_basemap(ax=ax)   

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)