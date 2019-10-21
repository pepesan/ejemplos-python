import datetime
import time
import pymysql

# Conectar con base de datos
conexion = pymysql.connect(host="localhost",
                           user="root",
                           passwd="root",
                           database="test")
cursor = conexion.cursor()

# Recuperar registros de la tabla 'usuarios'
registros = "SELECT * FROM usuarios;"

# Mostrar registros
cursor.execute(registros)
filas = cursor.fetchall()
for fila in filas:
   print(fila)


"""
# Recuperar registros de la tabla 'language'
registros = "SELECT * FROM language;"

# Mostrar registros
cursor.execute(registros)
filas = cursor.fetchall()
for fila in filas:
   print(fila)


# Definir comandos para insertar registros

ts = time.time()
now = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
print(now)
registro1 = "INSERT INTO language (name, last_update) VALUES ('Euskara', %s);"

# Ejecutar comandos
cursor.execute(registro1,now)
registros = "SELECT * FROM language;"

# Mostrar registros
cursor.execute(registros)
filas = cursor.fetchall()
for fila in filas:
   print(fila)

ts = time.time()
now = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
print(now)
registro1 = "Update language SET last_update=%s WHERE name='Euskara';"

# Ejecutar comandos
cursor.execute(registro1,now)

registros = "SELECT * FROM language;"

# Mostrar registros
cursor.execute(registros)
filas = cursor.fetchall()
for fila in filas:
   print(fila)



# Definir comandos para insertar registros
registro1 = "Delete from language where name='Euskara'"

# Ejecutar comandos
cursor.execute(registro1)

registros = "SELECT * FROM language;"

# Mostrar registros
cursor.execute(registros)
filas = cursor.fetchall()
for fila in filas:
   print(fila)

# Finalizar
conexion.commit()
conexion.close()

"""