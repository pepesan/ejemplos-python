# -*- coding: utf-8 -*-

# Load the Pandas libraries with alias 'pd'
import pandas as pd
# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
data = pd.read_csv("pokemon/pokedex.csv")
# Preview the first 5 lines of the loaded data
print(data.head())

print("Fin de salida")


from csv import reader
# Load a CSV File

def buscaEnListado(listado,elemento):
    if len(listado)>0:
        for item in listado:
            if item==elemento:
                return True
    return False

def load_csv(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file,delimiter=',')
        for row in csv_reader:
            if not row: continue
            dataset.append(row)
    return dataset

# load and prepare data
dataset = load_csv('random_forest/sonar.all-data.csv')
for fila in dataset:
    print(fila)
#print(dataset)

#print("lectura segura")

def load_csv_float(filename):
    dataset = list()
    try:

        with open(filename, 'r') as file:
            csv_reader = reader(file,delimiter=',')
            numerofila=0
            listado = list()
            for row in csv_reader:
                if not row: continue
                numerocampo=0

                for item in row:
                    #print(item)
                    if numerocampo==60:
                        row[numerocampo] = item
                        if buscaEnListado(listado,item):
                            break
                        else:
                            listado.append(item)
                    else:
                        try:
                            row[numerocampo] = float(item)
                        except ValueError:
                            row[numerocampo] = 0
                            print("Fallo",numerofila,numerocampo)
                    numerocampo+=1
                dataset.append(row)
                numerofila+=1
    except FileNotFoundError:
        print("Ha habido un error al abrir el fichero")
    print(listado)
    return dataset

dataset = load_csv_float('random_forest/sonar.all-data.csv')
#for fila in dataset:
    #
    # print(fila)

