# -*- coding: utf-8 -*-

#importamos el módulo de expresiones regulares
import re

"""Expresiones
Regulares"""
if re.search("cat","A cat and a rat can't be friends."):
    print ("Some kind of cat has been found :-)")
else:
    print ("No cat has been found :-(")

if re.search("c[aeuio]t","A cpt and a rat can't be friends."):
    print ("Some kind of c[vocal]t has been found :-)")
else:
    print ("No c[vocal]t has been found :-(")

if re.search("[iI][pP][sS][uU][mM]","Lorem IpSum  blah blah blah"):
    print ("Ha encontrado el ipsum con mayúscula o minúscula :-): ")
else:
    print ("Va a ser que no está :-(")
# comparación  de tarjeta de crédito
if re.search("(?:[0-9]{4}-){3}[0-9]{4}|[0-9]{16}", "5123-4567-8912-3456"):
    print ("Coincide el patrón de la tarjeta")
else:
    print("No coincide el patrón de tarjeta")
# comparación  de email
if re.search("[^@]+@[^@]+\.[^@]+", "p@p.com"):
    print ("Coincide el patrón del email")
else:
    print("No coincide el patrón del email")



