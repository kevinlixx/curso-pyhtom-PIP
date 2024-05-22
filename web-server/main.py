import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI() 

@app.get("/") #decorador que permite definir una ruta, en este caso la raiz
def read_root():
    return [1,2,3,4,5]

@app.get("/contacto") #decorador que permite definir una ruta, en este caso la raiz
def get_list():
    return """
    <h1> Hola mundo </h1>
    <p> Este es un parrafo </p>   
    """ 


def run():
    store.get_categories()

if __name__ == '__main__': #sirve para que solo se ejecute el codigo si se ejecuta el archivo main.py
    run()