class FileManager(): # declaro la clase
     def __init__(self, filename, mode):
         self.filename = filename
         self.mode = mode
         self.file = None
     def __enter__(self): # abro el fichero
         try:
            self.file = open(self.filename, self.mode)
         except:
            print("salta excepción")
            pass
         return self.file
     def __exit__(self, exc_type, exc_value, exc_traceback): # Cierro el fichero
        print("salida")
        self.file.close()
with FileManager('test.txt', 'w') as f: # Gestiona el contexto
    f.write('Test')
print(f.closed)