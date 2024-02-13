from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ahorcado import Ahorcado

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

juego_ahorcado = None
ERROR_PARTIDA = "Debe iniciar una partida"

@app.get("/get_palabra/")
def get_palabra():
    if juego_ahorcado is not None:
        return juego_ahorcado.palabra_correcta
    else:
        return {"error": ERROR_PARTIDA}
    
@app.get("/get_vidas/")
def get_vidas():
    if juego_ahorcado is not None:
        return juego_ahorcado.vidas
    else:
        return {"error": ERROR_PARTIDA}
    
@app.get("/get_estado/")
def get_estado():
    if juego_ahorcado is not None:
        return juego_ahorcado.estado_palabra
    else:
        return {"error": ERROR_PARTIDA}
    
@app.get("/get_letras_incorrectas/")
def get_letras_incorrectas():
    if juego_ahorcado is not None:
        return juego_ahorcado.letras_incorrectas
    else:
        return {"error": ERROR_PARTIDA}

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