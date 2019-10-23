



def imprimeDatos(conexion, sql):

    cursor = conexion.cursor()

    # Mostrar registros
    cursor.execute(sql)
    filas = cursor.fetchall()
    # Metadatos print(cursor.description)

    for fila in filas:
        print(fila)


def insertaDatos(conexion, sql, datos):
    # Ejecutar comandos
    cursor = conexion.cursor()
    cursor.execute(sql,datos)
    conexion.commit()

def updateDatos(conexion, sql, datos):
    # Ejecutar comandos
    cursor = conexion.cursor()
    cursor.execute(sql,datos)
    conexion.commit()


def borraDatos(conexion, sql):
    cursor = conexion.cursor()
    cursor.execute(sql)
    conexion.commit()

def importSchema(conexion, sql):
    cursor = conexion.cursor()
    cursor.execute(sql)
    conexion.commit()


import pymysql

# Conectar con base de datos
conexion = pymysql.connect(host="localhost",
                           port=3306,
                           user="root",
                           passwd="root",
                           database="test")
cursor = conexion.cursor()

sql="USE `test`;"
importSchema(conexion,sql)
sql="DROP TABLE IF EXISTS `usuarios`;"
importSchema(conexion,sql)
sql="""CREATE TABLE `usuarios` (
  `id_user` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(20) CHARACTER SET Utf8mb4 COLLATE Utf8mb4_unicode_520_ci NOT NULL,
  `password` varchar(50) CHARACTER SET Utf8mb4 COLLATE Utf8mb4_unicode_520_ci NOT NULL,
  `email` varchar(70) CHARACTER SET Utf8mb4 COLLATE Utf8mb4_unicode_520_ci NOT NULL,
  `name` varchar(50) CHARACTER SET Utf8mb4 COLLATE Utf8mb4_unicode_520_ci DEFAULT NULL,
  `encmethod` varchar(50) CHARACTER SET Utf8mb4 COLLATE Utf8mb4_unicode_520_ci NOT NULL DEFAULT 'sha1',
  `active` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id_user`),
  UNIQUE KEY `nombre_usuario_user` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=Utf8mb4 COLLATE=Utf8mb4_unicode_520_ci COMMENT='Aquí van los usuarios de la aplicación';
"""
importSchema(conexion,sql)
sql="""
INSERT INTO `usuarios` VALUES
    (1,'admin','admin','admin@cursosdedesarrollo.com',NULL,'sha1',0),
    (2,'pepito','pepito','pepito@cursosdedesarrollo.com','Administrador','sha1',1),
    (5,'mery','contraseña','p@p.com',NULL,'sha1',0),
    (6,'bea','contraseña','p@p.com',NULL,'sha1',0);

"""
importSchema(conexion,sql)


# Recuperar registros de la tabla 'usuarios'
registros = "SELECT * FROM usuarios;"

# Mostrar registros
imprimeDatos(conexion,sql=registros)




# Definir comandos para insertar registros
registro1 = "INSERT INTO usuarios " + \
                " (username, password, email) " + \
                "VALUES" + \
                " (%s, %s, %s);"
insertaDatos(conexion, registro1, ('pepesan','contraseña','p@p.com'))
# ts = time.time()
# now = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
# print(now)

registros = "SELECT * FROM usuarios WHERE username='pepesan';"

# Mostrar registros
imprimeDatos(conexion,registros)


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
"""

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


"""