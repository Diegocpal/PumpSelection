#import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy
from sympy.solvers import solve
from sympy import Symbol

# Fuente presión de vapor: https://www.conncoll.edu/media/website-media/offices/ehs/envhealthdocs/Transformer_Oil.pdf
y = 8260.02 #(N/m^3)

def calcular_npsha(hbp):
    Hatm = 101325/y #Se asume presión atmosferica Patm=101325 Pa
    Hvp = 13.33/y
    npsha = Hatm - hbp - Hvp
    return npsha

def calcular_npshr(bomba, q):
        Qlist = []
        Hlist = []
        for value in bomba['nqlmin']:
            if math.isnan(value) == False:
                Qlist.append(value)

        for value in bomba['nhm']:
            if math.isnan(value) == False:
                Hlist.append(value)

        Q = numpy.array(Qlist, dtype=float)  # Q(l/min)
        H = numpy.array(Hlist, dtype=float)  # H(m)
        e_npsh = numpy.polyfit(Q, H, 3)  # Dada la forma p1*x^3+p2*x^2+p3*x+p4 [p1, p2, p3, p4]

        p1 = e_npsh[0]
        p2 = e_npsh[1]
        p3 = e_npsh[2]
        p4 = e_npsh[3]

        npshr = (p1*q**3)+(p2*q**2)+(p3*q)+p4

        return npshr
