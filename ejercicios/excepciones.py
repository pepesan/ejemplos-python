import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

try:
   f = open("test.txt",encoding = 'utf-8')
   # perform file operations
except:
    print("Fallo al abrir")
finally:
    try:
        f.close()
    except Exception as e:
        print("No se ha podido cerrar, porque no estaba abierto")
        print("Error:" + str(e))