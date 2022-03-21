# -*- coding: utf-8 -*-

cadena = "mi texto"
fobj_out = open("ad_lesbiam.txt", "w")
fobj_out.write(cadena)
fobj_out.close()

fobj_in = open("ad_lesbiam.txt")
fobj_out = open("ad_lesbiam2.txt", "w")
i = 1
for line in fobj_in:
    print(line.rstrip())
    fobj_out.write(str(i) + ": " + line)
    i = i + 1
fobj_in.close()
fobj_out.close()


#como listado
lineas= open("ad_lesbiam.txt").readlines()
print (lineas)
#como string
texto = open("ad_lesbiam.txt").read()
print (texto[16:34])