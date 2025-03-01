# -*- coding: utf-8 -*-
# file portees_var.py


a = 1
b = 2
c = 3


def incr_affiche(b):
    global c
    # a += 1
    # => UnboundLocalError
    b += 1
    c += 1
    print("Dans la fonction")
    print(a, b, c)

print("Avant l'appel")
print(a, b, c)
incr_affiche(b)
print("Après l'appel")
print(a, b, c)
