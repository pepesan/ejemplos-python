# -*- coding: utf-8 -*-

from csv import reader
# Load a CSV File
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
"""
def load_csv_float(filename):
    dataset = list()
    with open(filename, 'r') as file:
        csv_reader = reader(file,delimiter=',')
        numerofila=0
        for row in csv_reader:
            if not row: continue
            numerocampo=0
            for item in row:
                #print(item)
                row[numerocampo]=float(item)
                numerocampo+=1
            dataset.append(row)
            numerofila+=1
    return dataset

dataset = load_csv_float('random_forest/sonar.all-data.csv')
for fila in dataset:
    print(fila)
"""