from flask import Flask
import requests
from bs4 import BeautifulSoup
import uvicorn

app = Flask('app')

@app.get("/")
def root():
    return {"message": "To check if the RUC exists, go to the /ruc/{ruc} endpoint",
            "url": "localhost:8000/ruc/{ruc}"}
    
    
@app.get("/ruc/<ruc>")
def say_hello(ruc: str):
    url = (f"https://srienlinea.sri.gob.ec/sri-catastro-sujeto-servicio-internet/rest/ConsolidadoContribuyente"
           f"/existePorNumeroRuc?numeroRuc={ruc}")
    response = requests.get(url)
    if not response.json():
        return {"ruc": ruc, "existe": False}
    try:
        response.json()['mensaje']
        return {"mensaje": "Posible RUC incorrecto"}
    except TypeError:
        return {"ruc": ruc, "existe": True}


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)
