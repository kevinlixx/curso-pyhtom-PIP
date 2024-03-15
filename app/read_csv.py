import csv 

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',') #puede variar la, si esta separado de diferente manera
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)# el zip une los dos arrays 
      country_dict = {key: value for key, value in iterable} #aca lo que hacemos es crear un diccionario con la clave y el valor
      data.append(country_dict)
    return data



if __name__ == '__main__': #este if lo que hace es que si el archivo se ejecuta desde la terminal, no se ejecute la funcion read_csv
  data = read_csv('./app/data.csv')
  print(data[0])

