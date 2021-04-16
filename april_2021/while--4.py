#!/usr/bin/env python

p = 6
q = p - 8

valor = 18

while q < 0:
    valor = valor +(valor*p+q)
    p =p +2
    q = q+1
    print(valor)
    continue
    