def resta(x,y):
    return x-y
res= resta(5,3)
print(res)

def divide(x,y):
    return x/y

print(divide(5,3))

def cuenta(listado):
    return len(listado)

prueba=[1,2,3]

print(cuenta(prueba))


def divide(x=0,y=1):
    return x/y

divide()
divide(1)
divide(1,2)

from csv import reader
# Load a CSV File
def load_csv(filename):
    dataset = list()
    invalid_lines = 0
    with open(filename, 'r') as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                invalid_lines+=1
                continue
            dataset.append(row)
    return (dataset,invalid_lines)

# load and prepare data
(dataset,lineas_invalidas) = load_csv('sonar.all-data.csv')
print("Lineas validas: ",len(dataset))
print("Líneas inválidas",lineas_invalidas)