from flask import Flask
from flask import render_template
from flask import request
from sodapy import Socrata
import pandas as pd

#Obteniendo datos de vacunacion
client = Socrata("www.datos.gov.co", None)
results = client.get("sdvb-4x4j", limit=2000)
results_df = pd.DataFrame.from_records(results)

app = Flask(__name__)
#Pagina principal
@app.route('/')
def index():
    return render_template('index.html', tables=[results_df.to_html(classes='data', header=True)])

#Pagina del formulario
@app.route('/formulario')
def show_formulario():
    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
