
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

    def actualizaRegistro(self,nombreTabla, campos, datos, condiciones):
        sql= "update "+nombreTabla+" set "
        for index in range(len(campos)):
            sql += campos[index] + "=" + datos[index]
            if(index<(len(campos)-1)):
                sql+=","
        sql+=" Where "
        for index in range(len(condiciones)):
            sql += condiciones[index]
            if (index < (len(condiciones) - 1)):
                sql += ","
        sql+=";"
        print(sql)
        self.cursor.execute(sql)
        self.conexion.commit()

    def borraDatos(self,sql):

        self.cursor.execute(sql)
        self.conexion.commit()

    def importSchema(self, sql):
        cursor = self.conexion.cursor()
        cursor.execute(sql)
        self.conexion.commit()

    def __del__(self):
        self.conexion.close()
        print("Conexión cerrada")




# Conectar con base de datos
#conexion = Conexion()
conexion = ConexionMySql(port=3306, password="root")

sql="USE `test`;"
conexion.importSchema(sql)
sql="DROP TABLE IF EXISTS `usuarios`;"
conexion.importSchema(sql)
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
conexion.importSchema(sql)
sql="""
INSERT INTO `usuarios` VALUES
    (1,'admin','admin','admin@cursosdedesarrollo.com',NULL,'sha1',0),
    (2,'pepito','pepito','pepito@cursosdedesarrollo.com','Administrador','sha1',1),
    (5,'mery','contraseña','p@p.com',NULL,'sha1',0),
    (6,'bea','contraseña','p@p.com',NULL,'sha1',0);

"""
conexion.importSchema(sql)
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

registros = "SELECT * FROM usuarios WHERE username='pepesan';"

# Mostrar registros
conexion.imprimeDatos(registros)
# Ejecutar comandos
conexion.updateDatos(registro1, datos)
conexion.actualizaRegistro('usuarios',['password'],["'contraseña nueva'"],["username='pepesan'"])

registros = "SELECT * FROM usuarios WHERE username='pepesan';"

# Mostrar registros
conexion.imprimeDatos(registros)

registro1 = "Delete from usuarios where username='pepesan';"

conexion.borraDatos(registro1)

conexion.insertaRegistro('usuarios',['username', 'password', 'email'], ['pepesan','contraseña','p@p.com'])



registros = "SELECT * FROM usuarios WHERE username='pepesan';"

# Mostrar registros
conexion.imprimeDatos(registros)
registro1 = "Delete from usuarios where username='pepesan';"

conexion.borraDatos(registro1)
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