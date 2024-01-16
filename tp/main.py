from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ahorcado import Ahorcado
# from tp.ahorcado import obtener_saludo


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

juego_ahorcado = None

@app.get("/ingresa_palabra/{palabra}")
def ingresa_palabra(palabra):
    global juego_ahorcado
    juego_ahorcado = Ahorcado(palabra)
    return {"éxito": "Palabra ingresada correctamente"}

@app.get("/adivina_palabra/{palabra}")
def adivina_palabra(palabra):
    if juego_ahorcado is not None:
        return juego_ahorcado.ingresa_palabra(palabra)
    else:
        return {"error": "Primero ingresa una palabra"}

@app.get("/adivina_letra/{letra}")
def adivina_letra(letra):
    if juego_ahorcado is not None:
        return juego_ahorcado.ingresa_letra(letra)
    else:
        return {"error": "Primero ingresa una palabra"}