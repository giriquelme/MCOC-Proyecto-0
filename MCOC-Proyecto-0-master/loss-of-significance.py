# -*- coding: utf-8 -*-
"""
Created on Sun Aug 04 19:11:44 2019

@author: rique
"""

import math
from numpy import*
from matplotlib import pyplot
    #Valores entregados por defecto
a=2**0.5
b=math.pi
c=math.e
d=-math.cos(90)
e=math.sin(90)
print "los valores entregados por defecto son:"
print a
print b
print c
print d
print e
print "El error se define como:"
print " error= (|valor con decimales ajustados-valor por defecto|)/(valor por defecto) "
    #Valores asignando dos decimales
a1=float(format(a,".2f"))
b1=float(format(b,".2f"))
c1=float(format(c,".2f"))
d1=float(format(d,".2f"))
e1=float(format(e,".2f"))

error_a_1=(abs(a1-a)/a)*100
error_b_1=(abs(b1-b)/b)*100
error_c_1=(abs(c1-c)/c)*100
error_d_1=(abs(d1-d)/d)*100
error_e_1=(abs(e1-e)/e)*100

print"considerando 2 digitos decimales el error para la raiz cuadrada de 2 es:",error_a_1,"%"
print"considerando 2 digitos decimales el error para el numero pi es:",error_b_1,"%"
print"considerando 2 digitos decimales el error para el numero euler es:",error_c_1,"%"
print"considerando 2 digitos decimales el error para el coseno de 90 es:",error_d_1,"%"
print"considerando 2 digitos decimales el error para el seno de 90 es:",error_e_1,"%"
print "-------------------------------------------------------------------------------------------"

    #Valores asignando seis decimales
a2=float(format(a,".6f"))
b2=float(format(b,".6f"))
c2=float(format(c,".6f"))
d2=float(format(d,".6f"))
e2=float(format(e,".6f"))

error_a_2=(abs(a2-a)/a)*100
error_b_2=(abs(b2-b)/b)*100
error_c_2=(abs(c2-c)/c)*100
error_d_2=(abs(d2-d)/d)*100
error_e_2=(abs(e2-e)/e)*100

print"considerando 6 digitos decimales el error para la raiz cuadrada de 2 es:",error_a_2,"%"
print"considerando 6 digitos decimales el error para el numero pi es:",error_b_2,"%"
print"considerando 6 digitos decimales el error para el numero euler es:",error_c_2,"%"
print"considerando 6 digitos decimales el error para el coseno de 90 es:",error_d_2,"%"
print"considerando 6 digitos decimales el error para el seno de 90 es:",error_e_2,"%"
print "-------------------------------------------------------------------------------------------"

print " Grafico de error por aproximacion"
x=[a,b,c,d,e]
y=[error_a_1,error_b_1,error_c_1,error_d_1,error_e_1]
z=[error_a_2,error_b_2,error_c_2,error_d_2,error_e_2]
pyplot.plot(x,y,"o")
pyplot.plot(x,z,"o")
pyplot.show()
print "Error para 2 digitos: color Azul"
print "Error para 6 digitos: color verde"