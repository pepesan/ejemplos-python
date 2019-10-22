
import pymysql

class ConexionMySql:
    def __init__(self, host = "localhost", port=3306, username="root", password="", database="test"):
        self.host=host
        self.port = port
        self.username=username
        self.password= password
        self.database=database
        self.conexion = pymysql.connect(host=self.host,
                           port=self.port,
                           user=self.username,
                           passwd=self.password,
                           database=self.database)
        self.cursor=self.conexion.cursor()
    def imprimeTabla(self, nombreTabla):
        # Mostrar registros
        sql= "Select * from "+nombreTabla+";"
        self.imprimeDatos(sql)
    def imprimeDatos(self,sql):
        # Mostrar registros
        self.cursor.execute(sql)
        filas = self.cursor.fetchall()
        # Metadatos print(cursor.description)

        for fila in filas:
            print(fila)

    def insertaRegistro(self,nombreTabla, campos, datos):
        sql= "insert into "+nombreTabla+"("
        for index in range(len(campos)):
            if(index>=(len(campos)-1)):
                sql+=campos[index]
            else:
                sql+=campos[index]+","
        sql+=") VALUES ("
        for index in range(len(datos)):
            if(index>=(len(datos)-1)):
                sql+="%s"
            else:
                sql+="%s,"
        sql+=");"
        print(sql)
        self.insertaDatos(sql, datos)

    def insertaDatos(self,sql, datos):
        # Ejecutar comandos

        self.cursor.execute(sql,datos)
        self.conexion.commit()

    def updateDatos(self,sql, datos):
        # Ejecutar comandos

        self.cursor.execute(sql,datos)
        self.conexion.commit()


    def borraDatos(self,sql):

        self.cursor.execute(registro1)
        self.conexion.commit()

    def __del__(self):
        self.conexion.close()
        print("Conexión cerrada")




# Conectar con base de datos
#conexion = Conexion()
conexion = ConexionMySql(port=3306, password="root")

# Recuperar registros de la tabla 'usuarios'
#registros = "SELECT * FROM usuarios;"

# Mostrar registros
#conexion.imprimeDatos(sql=registros)
conexion.imprimeTabla("usuarios")



# Definir comandos para insertar registros
"""registro1 = "INSERT INTO usuarios " + \
                " (username, password, email) " + \
                "VALUES" + \
                " (%s, %s, %s);"
"""
#conexion.insertaDatos(registro1, ('pepesan','contraseña','p@p.com'))
conexion.insertaRegistro('usuarios',('username', 'password', 'email'), ('pepesan','contraseña','p@p.com'))
# ts = time.time()
# now = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
# print(now)

registros = "SELECT * FROM usuarios WHERE username='pepesan';"

# Mostrar registros
conexion.imprimeDatos(registros)

registro1 = "Update usuarios SET password=%s WHERE username='pepesan';"
datos = ('contraseñanueva')

# Ejecutar comandos
conexion.updateDatos(registro1, datos)

registros = "SELECT * FROM usuarios WHERE username='pepesan';"

# Mostrar registros
conexion.imprimeDatos(registros)

registro1 = "Delete from usuarios where username='pepesan';"

conexion.borraDatos(registro1)

registros = "SELECT * FROM usuarios WHERE username='pepesan';"

# Mostrar registros
conexion.imprimeDatos(registros)
"""

registro1 = "Update usuarios SET password=%s WHERE username='pepesan';"
datos = ('contraseñanueva')

# Ejecutar comandos
updateDatos(conexion, registro1, datos)

registros = "SELECT * FROM usuarios WHERE username='pepesan';"

# Mostrar registros
imprimeDatos(conexion,registros)

registro1 = "Delete from usuarios where username='pepesan';"

borraDatos(conexion, registro1)

registros = "SELECT * FROM usuarios WHERE username='pepesan';"

# Mostrar registros
imprimeDatos(conexion,registros)

conexion.close()


BBDD SAKILA
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