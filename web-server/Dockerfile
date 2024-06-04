FROM python:3.10

#workdir permite definir o diretório de trabajo
WORKDIR /app
#el lado izquierdo es el directorio de trabajo en el contenedor y el lado derecho es el directorio en el host
COPY requirements.txt /web-server/requirements.txt 

#se coloca -r para que instale las dependencias que estan en el archivo requirements.txt debido a que -r es para leer un archivo
#--no-cache-dir es para que no guarde en cache las dependencias
#--upgrade es para que actualice las dependencias
RUN pip install --no-cache-dir --upgrade -r /web-server/requirements.txt

#se copia todo el contenido de la carpeta app en el contenedor
COPY . /app/

#CMD es para ejecutar un comando en el contenedor
#uvicorn es un servidor web asincrono
#main:app es el archivo main.py y app es la variable app que se encuentra en el archivo main.py
#--host es para definir el host
#--port es para definir el puerto
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]