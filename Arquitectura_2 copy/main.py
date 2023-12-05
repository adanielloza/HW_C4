from flask import Flask
import requests
from bs4 import BeautifulSoup
import uvicorn

app = Flask('app')


@app.get("/")
def root():
    return {"message": "Para saber si el RUC existe ir al endpoint /ruc/{ruc}",
            "url": "localhost:8000/ruc/{ruc}"}


@app.get("/cedula/<cedula>")
def cedula(cedula:str):
    url = (f"https://consultaweb.ant.gob.ec/PortalWEB/paginas/clientes/clp_grid_citaciones.jsp?ps_tipo_identificacion"
           f"=CED&ps_identificacion={cedula}")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    try:
        points = soup.find('td', {'title': 'Información adicional de Puntos'}).text
        name = soup.find('td', {'class': 'titulo1'}).text
    except AttributeError:
        return {"cedula": cedula, "nombre": "No existe", "puntos": "No existe"}
    return {"cedula": cedula, "nombre": name, "puntos": points}


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8001)