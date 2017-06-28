# -*- coding: utf-8 -*-

#importamos el módulo de expresiones regulares
import re

"""Expresiones
Regulares"""
if re.search("cat","A cat and a rat can't be friends."):
    print ("Some kind of cat has been found :-)")
else:
    print ("No cat has been found :-(")

if re.search("c[aeuio]t","A cat and a rat can't be friends."):
    print ("Some kind of c[vocal]t has been found :-)")
else:
    print ("No c[vocal]t has been found :-(")





