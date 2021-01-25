#import pandas as pd
#import math
#import matplotlib.pyplot as plt
#import numpy
#from sympy.solvers import solve
#from sympy import Symbol
from NPSH import *

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy
from sympy.solvers import solve
from sympy import Symbol

# Inicialmente se consideraran 4 modos de funcionamiento
# 1. En serie desde el tanque A pasando por el tanque 1 y llegando al tanque c
# 2. En serie desde el tanque A pasando por el tanque 2 y llegando a D
# 3. En paralelo, ambos tanques funcionando y retornando a la descarga de la bomba (caso más crítico)
# 4. En paralelo, ambos tanques funcionando y depositando en los tanques de descarga C y D

#factores de fricción de los accesorios para los diferentes modos de funcionamiento
kal = 75 # filtros de pie de alcachofa tipo colador K=75f
kma = 45 # Valvulas de mariposa K=45f
kco = 20 # codos a 90° k=20f
kte = 60 # conexiones en T K=60f

def calcular_reynolds(dia, vel, v):
    return (vel * (dia * 10.0 ** (-3.0))) / (v*10**(-6))


def calcular_f(Re, dia, rug):
    if Re < 2000:  # flujo laminar
        return 64.0 / Re
    elif Re > 4000:  # flujo turbulento
        Log = math.log10((1.0 / (3.7 * (dia/ rug))) + (5.74 / (Re ** 0.9)))
        return 0.25 / (Log ** 2.0)  # Swanee and Jain
    else:
        #print("El fluido se encuentra en estado de transición")
        #print("Se asumira comportamiento turbulento en ese tramo")
        Log = math.log((1.0 / 3.7 * (dia * 10 ** (-3)) / rug) + (5.74 / (Re ** 0.9)))
        return 0.25 / (Log ** 2.0)  # Swanee and Jain


def calcular_hL(dia, vel, long, f):
    return f * (long / (dia * 10.0 ** (-3.0))) * ((vel ** 2.0) / (2.0 * 9.81))  # Ecuación de Darcy


def calcular_acce(vel, f, k):
    return (f*k)*((vel**2)/(2*9.81))


def graficar_curva_instalacion(df, x, y):
    df.plot(x = x, y = y, kind = 'line')
    plt.xlabel('Q(l/min)')
    plt.ylabel('H(m)')
    plt.show()

def perdidas_succion(f, dia, vel):
    l = 0.3 #m
    k = kal + kma + kte
    hl = calcular_hL(dia, vel, l, f)
    ha = calcular_acce(vel, f, k)
    return hl + ha

def calcular_cabeza(temp, i, q, ptk): #la presión ptk se ingresa en bares y es la misma para ambos tanques
    # q (litros/min)
    va = 8.079*math.exp(-0.1802*temp) #(mm^2/s)
    vt = 8.079*math.exp(-0.1802*60) #(mm^2/s)
    g = 9.81 #(m/s^2)
    y = 8260.02 #(N/m^3)
    Q = q*(10**(-3))*(60**(-1)) #(m3/s)
    Ds = 76.2 #(mm)
    D = 12.7 #(mm)
    Rug = 0.0305 #mm
    Vels = Q / (3.14159 * 0.25 * (Ds * 10.0 ** (-3.0)) ** 2.0)  # (m/s)
    Vel = Q / (3.14159 * 0.25 * (D * 10.0 ** (-3.0)) ** 2.0) #(m/s)
    Vel2 = (Q/2) / (3.14159 * 0.25 * (D * 10.0 ** (-3.0)) ** 2.0) #(m/s)
    Datos_red = pd.DataFrame(
                            columns=['Longa', 'Longt',
                                     'Res', 'Rea', 'Ret' 
                                     'fs', 'fa', 'ft', 'hLa',
                                     'hLt', 'hLtotal',
                                     'k1', 'k2',
                                     'hsuccion'
                                     ])



    Datos_red.loc[1, 'k1'] = kal + 2 * kma + 2 * kco
    Datos_red.loc[1, 'k2'] = 2 * kco + kma
    Datos_red.loc[2, 'k1'] = 2 * kal + 3 * kma + 3 * kco + kte
    Datos_red.loc[2, 'k2'] = 2 * kco + kma

    #Se establecen los datos inamovibles de longitud de las redes de los diferentes modos
    #de funcionamiento
    Datos_red.loc[1, 'Longa'] = 1 #m
    Datos_red.loc[1, 'Longt'] = 0.5 #m
    Datos_red.loc[2, 'Longa'] = 1 #m
    Datos_red.loc[2, 'Longt'] = 0.25 #m

    # Se convierte la presión de los tanques de bares a pascales
    Ptk1 = ptk * (10 ** 5)  # Pa
    Ptk2 = ptk * (10 ** 5)  # Pa

    # Se asume que la presión en los tanques A,B,C y D es atmosferica
    Pa = 0
    Pb = 0
    Pc = 0
    Pd = 0


    if i == 1 or i == 2:
        #Calculo del Reynolds
        Datos_red.loc[i, 'Res'] = calcular_reynolds(Ds, Vels, va)
        Datos_red.loc[i, 'Rea'] = calcular_reynolds(D, Vel, va)
        Datos_red.loc[i, 'Ret'] = calcular_reynolds(D, Vel, vt)

        #Calculo del factor de fricción
        Datos_red.loc[i, 'fs'] = calcular_f(Datos_red.loc[i, 'Res'], D, Rug)
        Datos_red.loc[i, 'fa'] = calcular_f(Datos_red.loc[i, 'Rea'], D, Rug)
        Datos_red.loc[i, 'ft'] = calcular_f(Datos_red.loc[i, 'Ret'], D, Rug)

        #Calculo de las perdidas por longitud
        Datos_red.loc[i, 'hLa'] = calcular_hL(D, Vel, Datos_red.loc[i, 'Longa'], Datos_red.loc[i, 'fa'])
        Datos_red.loc[i, 'hLt'] = calcular_hL(D, Vel, Datos_red.loc[i, 'Longt'], Datos_red.loc[i, 'ft'])
        Datos_red.loc[i, 'hLtotal'] = Datos_red.loc[i, 'hLa'] + Datos_red.loc[i, 'hLt']

        # Se calculan perdidas por accesorios en el tramo 1
        h1 = calcular_acce(Vel, Datos_red.loc[i, 'fa'], Datos_red.loc[i, 'k1'])

        # Se calculan las perdidas por accesorios en el tramo 2
        h2 = calcular_acce(Vel, Datos_red.loc[i, 'ft'], Datos_red.loc[i, 'k2'])

        # Se calculan las perdidas en la succión
        Datos_red.loc[i, 'hsuccion'] = perdidas_succion(Datos_red.loc[i, 'fs'], Ds, Vels)
        hs = Datos_red.loc[i, 'hsuccion']

        #Se calcula la cabeza total
        cabeza_total = Datos_red.loc[i, 'hLtotal'] + h1 + h2 + Datos_red.loc[i, 'hsuccion']

    elif i ==3:
        Datos_red3 = pd.DataFrame(
            columns=['Longt1', 'Longt2', 'Longt3', 'Longt4',
                     'Res', 'Ret1', 'Ret2', 'Ret3', 'Ret4',
                     'fs', 'ft1', 'ft2', 'ft3', 'ft4',
                     'hLt1', 'hLt2', 'hLt3', 'hLt4',
                     'hLtotal', 'k1', 'k2', 'k3', 'k4',
                     'hAt1', 'hAt2', 'hAt3', 'hAt4', 'hAtotal'])

        #Se ingresan las longitudes de los tramos para el modo de funcionamiento 3
        Datos_red3.loc[3, 'Longt1'] = 0.3 #m
        Datos_red3.loc[3, 'Longt2'] = 0.4 + 0.3 + 0.7  #m
        Datos_red3.loc[3, 'Longt3'] = 0.5 + 0.4 + 0.5  #m
        Datos_red3.loc[3, 'Longt4'] = 0.6 + 0.2  #m

        #Se ingresan las resistencias de los accesorios para los tramos para el mdoo de funcionamiento 3
        Datos_red3.loc[3, 'k1'] = kal + kma + kco + 2 * kte
        Datos_red3.loc[3, 'k2'] = 2 * kma + 4 * kco
        Datos_red3.loc[3, 'k3'] = 2 * kma + 2 * kco + kte
        Datos_red3.loc[3, 'k4'] = 1 * kma + 1 * kco

        #Calculos para el tramo 1 (antes de la T)

        #Numero de Reynolds
        Datos_red3.loc[i, 'Res'] = calcular_reynolds(Ds, Vels, va)
        Datos_red3.loc[i, 'Ret1'] = calcular_reynolds(D, Vel, va)
        Datos_red3.loc[i, 'Ret2'] = calcular_reynolds(D, Vel2, va)
        Datos_red3.loc[i, 'Ret3'] = calcular_reynolds(D, Vel2, vt)
        Datos_red3.loc[i, 'Ret4'] = calcular_reynolds(D, Vel, vt)

        #Factor de fricción
        Datos_red3.loc[i, 'fs'] = calcular_f(Datos_red3.loc[i, 'Res'], D, Rug)
        Datos_red3.loc[i, 'ft1'] = calcular_f(Datos_red3.loc[i, 'Ret1'], D, Rug)
        Datos_red3.loc[i, 'ft2'] = calcular_f(Datos_red3.loc[i, 'Ret2'], D, Rug)
        Datos_red3.loc[i, 'ft3'] = calcular_f(Datos_red3.loc[i, 'Ret3'], D, Rug)
        Datos_red3.loc[i, 'ft4'] = calcular_f(Datos_red3.loc[i, 'Ret4'], D, Rug)


        #Perdidas por longitud
        Datos_red3.loc[i, 'hLt1'] = calcular_hL(D, Vel, Datos_red3.loc[i, 'Longt1'], Datos_red3.loc[i, 'ft1'])
        Datos_red3.loc[i, 'hLt2'] = calcular_hL(D, Vel2, Datos_red3.loc[i, 'Longt2'], Datos_red3.loc[i, 'ft2'])
        Datos_red3.loc[i, 'hLt3'] = calcular_hL(D, Vel2, Datos_red3.loc[i, 'Longt3'], Datos_red3.loc[i, 'ft3'])
        Datos_red3.loc[i, 'hLt4'] = calcular_hL(D, Vel, Datos_red3.loc[i, 'Longt4'], Datos_red3.loc[i, 'ft4'])

        #Perdidas por longitud totales
        Datos_red3.loc[i, 'hLtotal'] = Datos_red3.loc[i, 'hLt1'] + Datos_red3.loc[i, 'hLt2'] + Datos_red3.loc[i, 'hLt3'] + Datos_red3.loc[i, 'hLt4']

        #Perdidas por accesorios
        Datos_red3.loc[i, 'hAt1'] = calcular_acce(Vel, Datos_red3.loc[i, 'ft1'], Datos_red3.loc[i, 'k1'])
        Datos_red3.loc[i, 'hAt2'] = calcular_acce(Vel2, Datos_red3.loc[i, 'ft2'], Datos_red3.loc[i, 'k2'])
        Datos_red3.loc[i, 'hAt3'] = calcular_acce(Vel2, Datos_red3.loc[i, 'ft3'], Datos_red3.loc[i, 'k3'])
        Datos_red3.loc[i, 'hAt4'] = calcular_acce(Vel, Datos_red3.loc[i, 'ft4'], Datos_red3.loc[i, 'k4'])

       #Perdidas totales por accesorios
        Datos_red3.loc[i, 'hAtotal'] = Datos_red3.loc[i, 'hAt1'] + Datos_red3.loc[i, 'hAt2'] + Datos_red3.loc[i, 'hAt3'] + Datos_red3.loc[i, 'hAt4']

        #Se calculan las perdidas a la succión
        hs = perdidas_succion(Datos_red3.loc[i, 'fs'], Ds, Vels)

        #print(Datos_red3.loc[i, 'hAtotal'])

        #Se calcula la cabeza total
        cabeza_total = -hs + Datos_red3.loc[i, 'hAtotal'] + Datos_red3.loc[i, 'hLtotal'] + hs

    elif i ==4:
        Datos_red3 = pd.DataFrame(
            columns=['Longt1', 'Longt2', 'Longt3',
                     'Res', 'Ret1', 'Ret2', 'Ret3',
                     'fs', 'ft1', 'ft2', 'ft3',
                     'hLt1', 'hLt2', 'hLt3','hLtotal',
                     'k1', 'k2', 'k3',
                     'hAt1', 'hAt2', 'hAt3', 'hAtotal'])

        #Se ingresan las longitudes de los tramos para el modo de funcionamiento 3
        Datos_red3.loc[4, 'Longt1'] = 0.3 #m
        Datos_red3.loc[4, 'Longt2'] = 0.4 + 0.3 + 0.7  #m
        Datos_red3.loc[4, 'Longt3'] = 0.5 + 0.25  #m

        #Se ingresan las resistencias de los accesorios para los tramos para el mdoo de funcionamiento 3
        Datos_red3.loc[4, 'k1'] = kal + kma + kco + 2 * kte
        Datos_red3.loc[4, 'k2'] = 2 * kma + 4 * kco
        Datos_red3.loc[4, 'k3'] = 2 * kma + 4 * kco

        #Numero de Reynolds
        Datos_red3.loc[i, 'Res'] = calcular_reynolds(Ds, Vels, va)
        Datos_red3.loc[i, 'Ret1'] = calcular_reynolds(D, Vel, va)
        Datos_red3.loc[i, 'Ret2'] = calcular_reynolds(D, Vel2, va)
        Datos_red3.loc[i, 'Ret3'] = calcular_reynolds(D, Vel2, vt)

        #Factor de fricción
        Datos_red3.loc[i, 'fs'] = calcular_f(Datos_red3.loc[i, 'Res'], D, Rug)
        Datos_red3.loc[i, 'ft1'] = calcular_f(Datos_red3.loc[i, 'Ret1'], D, Rug)
        Datos_red3.loc[i, 'ft2'] = calcular_f(Datos_red3.loc[i, 'Ret2'], D, Rug)
        Datos_red3.loc[i, 'ft3'] = calcular_f(Datos_red3.loc[i, 'Ret3'], D, Rug)

        #Perdidas por longitud
        Datos_red3.loc[i, 'hLt1'] = calcular_hL(D, Vel, Datos_red3.loc[i, 'Longt1'], Datos_red3.loc[i, 'ft1'])
        Datos_red3.loc[i, 'hLt2'] = calcular_hL(D, Vel2, Datos_red3.loc[i, 'Longt2'], Datos_red3.loc[i, 'ft2'])
        Datos_red3.loc[i, 'hLt3'] = calcular_hL(D, Vel2, Datos_red3.loc[i, 'Longt3'], Datos_red3.loc[i, 'ft3'])

        #Perdidas por longitud totales
        Datos_red3.loc[i, 'hLtotal'] = Datos_red3.loc[i, 'hLt1'] + Datos_red3.loc[i, 'hLt2'] + Datos_red3.loc[i, 'hLt3']

        #Perdidas por accesorios
        Datos_red3.loc[i, 'hAt1'] = calcular_acce(Vel, Datos_red3.loc[i, 'ft1'], Datos_red3.loc[i, 'k1'])
        Datos_red3.loc[i, 'hAt2'] = calcular_acce(Vel2, Datos_red3.loc[i, 'ft2'], Datos_red3.loc[i, 'k2'])
        Datos_red3.loc[i, 'hAt3'] = calcular_acce(Vel2, Datos_red3.loc[i, 'ft3'], Datos_red3.loc[i, 'k3'])

        #Perdidas totales por accesorios
        Datos_red3.loc[i, 'hAtotal'] = Datos_red3.loc[i, 'hAt1'] + Datos_red3.loc[i, 'hAt2'] + Datos_red3.loc[i, 'hAt3']

        #Se calculan las perdidas en la succión
        hs = perdidas_succion(Datos_red3.loc[i, 'fs'], Ds, Vels)

        #Se calcula la cabeza total
        cabeza_total = Datos_red3.loc[i, 'hAtotal'] + Datos_red3.loc[i, 'hLtotal'] + hs


    #qsuccion = [q, hsuccion]
    #print(qsuccion)
    output = [cabeza_total, hs]
    return output


