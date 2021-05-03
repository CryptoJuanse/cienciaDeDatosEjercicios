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
    num_resolucion = ''
    fecha_resolucion = ''

    if request.method == 'POST':
        opcion = request.form['opcion']
        vacunaT = request.form['vacunaT']
        num_resolucion = request.form['num_resolucion']
        fecha_resolucion = request.form['fecha_resolucion']

    #Logica de filtrado
    if opcion=='1':
        titulo = "Columnas del DataFrame"
        datos = pd.DataFrame(datos.columns)
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
    elif opcion=='5':
        titulo='Número de resolución'
        if num_resolucion == '168':
            datos = datos[datos["num_resolucion"] == '00000168']
        elif num_resolucion == '195':
            datos = datos[datos["num_resolucion"] == '00000195']
        elif num_resolucion == '205':
            datos = datos[datos["num_resolucion"] == '00000205']
        elif num_resolucion == '267':
            datos = datos[datos["num_resolucion"] == '00000267']
        elif num_resolucion == '302':
            datos = datos[datos["num_resolucion"] == '00000302']
        elif num_resolucion == '330':
            datos = datos[datos["num_resolucion"] == '00000330']
        elif num_resolucion == '333':
            datos = datos[datos["num_resolucion"] == '00000333']
        elif num_resolucion == '342':
            datos = datos[datos["num_resolucion"] == '00000342']
        elif num_resolucion == '361':
            datos = datos[datos["num_resolucion"] == '00000361']
        elif num_resolucion == '364':
            datos = datos[datos["num_resolucion"] == '00000364']

    elif opcion=='6':
        titulo = "Fecha de resolución"
        datos = datos[datos["fecha_resolucion"] == str(fecha_resolucion)]

    elif opcion=='7':
        titulo = "Matriz con un rango de filas y columnas determinado"
        datos = datos.loc[int(request.form['fila1']):int(request.form['fila2']), 
                              request.form['columna1']:request.form['columna2']]
    elif opcion=='8':
        titulo = "Filtrado por grupos"
        datos = datos.groupby([request.form['col1'], request.form['col2']])[request.form['col3']].count()
        datos = datos.to_frame()

    return render_template('formulario.html', decision=opcion, title=titulo, tables=[datos.to_html(classes='data', header=True)])

if __name__ == '__main__':
    app.run(debug=True, port=8000)
