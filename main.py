from flask import Flask
from flask import render_template
from flask import request
from sodapy import Socrata
import pandas as pd
import dateutil

#Obteniendo datos de vacunacion
client = Socrata("www.datos.gov.co", None)
results = client.get("sdvb-4x4j", limit=2000)
vacunas = pd.DataFrame.from_records(results)
vacunas['fecha_resolucion'] = vacunas['fecha_resolucion'].apply(dateutil.parser.parse)
vacunas['fecha_corte'] = vacunas['fecha_corte'].apply(dateutil.parser.parse)

app = Flask(__name__)
#Pagina principal
@app.route('/')
def index():
    return render_template('index.html', tables=[vacunas.to_html(classes='data', header=True)])

#Pagina del formulario
@app.route('/formulario', methods=['GET', 'POST'])
def show_formulario():
    opcion = ''
    datos = vacunas
    titulo = ''
    vacunaT = ''

    if request.method == 'POST':
        opcion = request.form['opcion']
        vacunaT = request.form['vacunaT']

    #Logica de filtrado
    if opcion=='1':
        titulo = "Descripcion General"
        datos = datos.describe()
    elif opcion=='2':
        titulo = "Datos iniciales"
        datos = datos.head(int(request.form['numeroH']))
    elif opcion=='3':
        titulo = "Datos Finales"
        datos = datos.tail(int(request.form['numeroT']))
    elif opcion=='4':
        titulo = "Laboratorio Vacuna"
        if vacunaT == '1':
            datos = datos[datos["laboratorio_vacuna"] == 'PFIZER']
        elif vacunaT =='2':
            datos = datos[datos["laboratorio_vacuna"] == 'SINOVAC']
    elif opcion=='7':
        titulo = "Matriz con un rango de filas y columnas determinado"
        datos = datos.loc[int(request.form['fila1']):int(request.form['fila2']), 
                              request.form['columna1']:request.form['columna2']]

    return render_template('formulario.html', decision=opcion, title=titulo, tables=[datos.to_html(classes='data', header=True)])

if __name__ == '__main__':
    app.run(debug=True, port=8000)
