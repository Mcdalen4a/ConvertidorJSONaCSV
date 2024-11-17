from flask import Flask, render_template, request, send_file
import json
import csv
import os

app = Flask(__name__)


def json_to_csv(json_data, csv_filename):
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)

        headers = json_data[0].keys()
        writer.writerow(headers)

  
        for row in json_data:
            writer.writerow(row.values())

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obtener el archivo JSON cargado
        file = request.files['file']
        
        if file and file.filename.endswith('.json'):
       
            data = json.load(file)
            
       
            csv_filename = "output.csv"
            
            # Convertir el JSON a CSV
            json_to_csv(data, csv_filename)

            # Enviar el archivo CSV como respuesta
            return send_file(csv_filename, as_attachment=True)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
