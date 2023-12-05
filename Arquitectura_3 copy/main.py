from flask import Flask, render_template
import requests
from flask import request

def call_cedula_api(cedula):
    url = f"http://127.0.0.1:8001/cedula/{cedula}"
    response = requests.get(url)
    return response.json()

def call_ruc_api(ruc):
    url = f"http://127.0.0.1:8000/ruc/{ruc}"
    response = requests.get(url)
    return response.json()

app = Flask('app')


@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        # The form is submitted
        cedula_from_form = request.form.get('cedula_input')  # Replace 'cedula_input' with the actual name of your form input

    # If it's a GET request or form not submitted, render the template without data
    return render_template('index.html')


@app.route('/process', methods=['GET', 'POST'])
def process():
    if request.method == 'POST':
        # The form is submitted
        cedula = request.form.get('cedula')
        print(cedula)
    cedula_data = call_cedula_api(cedula)
    ruc_data = call_ruc_api(cedula+'001')
    return render_template('index.html', cedula=cedula_data, ruc=ruc_data)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8002, debug=True)  
    
    
   
    







