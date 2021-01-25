import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy
from sympy.solvers import solve
from sympy import Symbol
from red import *
from bombas import *



def punto_operacion(bomba, red):
    limit = bomba['qlmin'].idxmax()
    ecuacion = ecuacion_bomba(bomba)
    p1 = ecuacion[0]
    p2 = ecuacion[1]
    p3 = ecuacion[2]
    p4 = ecuacion[3]

    z1 = red[0]
    z2 = red[1]
    z3 = red[2]

    x = Symbol('x')
    caudal = solve((p1*x**3)+((p2-z1)*x**2)+((p3-z2)*x)+(p4-z3), x)
    for q in caudal:
        qt = str(q)
        cut = qt.split( )
        if float(cut[0]) > 0:
            Qp = float(cut[0])
    H = (z1*Qp**2)+(z2*Qp)+z3
    punto_op = [Qp, H]

    Qlist = []
    for value in bomba['qlmin']:
        if math.isnan(value) == False:
            Qlist.append(value)

    qmax = max(Qlist)

    if qmax < Qp:
        #print("La bomba no es apropiada para las condiciones propuestas")
        punto_op = [0,0]
        return punto_op
    else:
        return punto_op


def graficar_punto_operacion(red, bomba):
    x1 = red['Q']
    y1 = red['H']

    x2 = bomba['qlmin']
    y2 = bomba['hm']

    plt.plot(x1, y1, label = 'Curva de la instalación')
    plt.plot(x2, y2, label = 'Curva de la bomba')
    plt.xlabel('Q(l/min)')
    plt.ylabel('H(m)')
    plt.show()


#b1602.to_csv('160.csv', encoding='utf-8', index=False)

