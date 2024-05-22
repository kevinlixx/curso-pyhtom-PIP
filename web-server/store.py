import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories') #permite hacer una peticion a la url para obtener la informacion
    print(r.status_code)#imprime el estado de la peticion si da 200 es que todo esta bien 
    print(r.text) #imprime el texto de la peticion
    print(type(r.text)) #imprime el tipo de dato que es el texto de la peticion
    categories = r.json() #convierte el texto de la peticion a un diccionario

    for category in categories:
        print(category['name'])

    