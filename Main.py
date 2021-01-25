# ha=Energía que se agrega al fluido con un dispositivo mecánico
# hR=Energía que se remueve del fluido por medio de un dispositivo mecánico
# hL=Pérdidas de enegía del sistema por la fricción en las tuberías y perdidas
# menores por válvulas y otros accesorios
# Se asume el uso de aceite dielectrico Electra Parafinitico,
# Catalogo: https://www.repsol.com/imagenes/global/en/dielectric_oils_catalog_tcm14-48939.pdf



# Ecuación de la energía: (P1/y)+z1+(v1^2/2g)+Ha-Hr-HL=(P2/y)+z2+(v2^2/2g)

# Programa que determina y grafica la curva de funcionamiento de los modos de funcionamiento de la red
# Como respuesta a una serie de entradas de usuario


import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy
from sympy.solvers import solve
from sympy import Symbol
from red import *
from bombas import *
from decision import *
from NPSH import *


def main(q, T, i, ptk):
    pt = ptk*6894.757
    y = 8260.02 #(N/m^3)
    D = 12.7 #(mm) 1/2"
    Rug = 0.046 #mm acero galvanizado

    caudal_cabeza = pd.DataFrame(columns=['Q', 'H'])
    caudal_metros = pd.DataFrame(columns=['Q'])

    co = 1
    while co < 401:
        caudal_cabeza.loc[co, 'Q'] = co  #l/min
        calcular_cabeza_hsuccion = calcular_cabeza(T, i, caudal_cabeza.loc[co, 'Q'], ptk)
        caudal_cabeza.loc[co, 'H'] = calcular_cabeza_hsuccion[0]
        co += 10
    #Determinar ecuación de Caudal_cabeza por ajuste polinomial polyfit
    Q = numpy.array(caudal_cabeza['Q'], dtype= float) #Q(l/min)
    H = numpy.array(caudal_cabeza['H'], dtype= float) #H(m)
    ecu_red = numpy.polyfit(Q, H, 2) #factores de la ecuación de la instalación de la forma p1*x^2+p2*x+p3

    #Recuperar lista de todas las bombas
    bombas = tablas_bombas()

    #Calcular NPSH disponible
    npsha = calcular_npsha(calcular_cabeza_hsuccion[1])

    #Calcular punto de operación
    op_point = [0,0]
    npshr = 0
    margen_npsh = 0
    b_elegida = None
    dq = 0
    for bomba in bombas:
        #Calcular NPSHR
        npshr = calcular_npshr(bomba, q)
        delta_npsh = npsha - npshr
        punto_op = punto_operacion(bomba, ecu_red)
        if punto_op != [0, 0] and delta_npsh > 0:
            dqa = punto_op[0] - q
            if dqa > 0 and dq == 0:
                dq = dqa
                b_elegida = bomba
                op_point = punto_op
                margen_npsh = delta_npsh
                npshr_op = npshr

            elif dqa > 0 and dqa < dq:
                dq = dqa
                b_elegida = bomba
                op_point = punto_op
                margen_npsh = delta_npsh

    if op_point == [0,0]:
        vmoa = tablas_vmoa()
        for bomba in vmoa:
            punto_op = punto_operacion(bomba, ecu_red)
            if punto_op != [0, 0]:
                dqa = punto_op[0] - q
                if dqa > 0 and dq == 0:
                    dq = dqa
                    b_elegida = bomba
                    op_point = punto_op
                    npshr_op = 'Anticavitación'
                    margen_npsh = 'No aplica'

                elif dqa > 0 and dqa < dq:
                    dq = dqa
                    b_elegida = bomba
                    op_point = punto_op
                    npshr_op = 'Anticavitación'
                    margen_npsh = 'No aplica'

    if op_point == [0,0]:
        name = 'No se encontró una bomba apropiada'
        rpm = ' '
        d_rodete = ' '
        margen_npsh = ' '
        caudal = ' '
        cabeza = ' '
    else:
        graficar_punto_operacion(caudal_cabeza, b_elegida)
        name = b_elegida.loc[0, 'name'] + ' ' + b_elegida.loc[1, 'name'] + ' ' + b_elegida.loc[2, 'name']
        rpm = b_elegida.loc[3, 'name']
        d_rodete = b_elegida.loc[4, 'name']
        margen_npsh = round(margen_npsh, 2)
        caudal = round(op_point[0], 2)
        cabeza = round(op_point[1], 2)

    output = [str(name), str(rpm), str(d_rodete), str(caudal), str(cabeza), str(margen_npsh)]
    return output


