import matplotlib.pyplot as plt  #el as sirve para cambiar el nombre de la libreria y asi no tener que escribir el nombre completo


def generate_bar_chart(name, labels, values):
  flg, ax = plt.subplots()
  ax.bar(
      labels, values
  )  #lo que permite esto es que el grafico se genere en el eje x y en el eje y
  plt.savefig(f'./imgs/{name}.png') #el f sirve para que se pueda concatenar el nombre con el .png
  plt.close()

def generate_pie_chart(labels, values):
  flg, ax = plt.subplots()
  ax.pie(values, labels=labels)  #el pie permite generar un grafico de torta
  ax.axis(
      'equal')  #el axis permite que el grafico se muestre en forma de circulo
  plt.savefig('pie.png')
  plt.close()


if __name__ == '__main__':  #esta condicional nos permite ejecutar el archivo como script desde la terminal
  labels = ['a', 'b', 'c']
  values = [10, 40, 800]
  #generate_bar_chart(labels, values)
  generate_pie_chart(labels, values)
