from fastapi import FastAPI
from Ahorcado import Ahorcado

app = FastAPI()

@app.post("/inicializar")
async def inicializar():
    partida = Ahorcado('manzana')
    return partida.id # Aun no tenemos el atributo id en la clase

@app.post("/probar_letra/")
async def probar_letra(letra, id_partida):
     # pendiente definir como hacer get_partida_por_id
     # partida seria una instancia de Ahorcado
    partida = get_partida_por_id(id_partida)
    if partida.probar_letra(letra):
        return True
    return False