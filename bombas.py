#Importar y convertir toda la información de las bombas desde unos csv
#Recalcular las tablas de operación para incluir H(m) y Q (l/min)
#Return una lista de dataframes con todas las bombas
#Return un dataframe con las ecuaciones de todas las bombas

import pandas as pd
import math
import matplotlib.pyplot as plt
import numpy
from sympy.solvers import solve
from sympy import Symbol

y = 8260.02 #(N/m^3)

def info_bomba(csv):
    return pd.read_csv(csv)


def graficar_curva_bomba(df, x, y):
    df.plot(x = x, y = y, kind = 'line')
    plt.xlabel('Q(l/min)')
    plt.ylabel('H(m)')
    plt.show()


def cabeza_bomba(i, datos, q): #q(l/min)
    return (datos.loc[i, 'p1']*q**3)+(datos.loc[i, 'p2']*q**2)+(datos.loc[i, 'p3']*q)+datos.loc[i, 'p4']


def tablas_bombas():
    #Bombas Etabloc 050-032-250.1 n=1160 rpm
    e5060_200 = info_bomba('bombas/etabloc/e50n1160/bombas/200.csv')
    e5060_210 = info_bomba('bombas/etabloc/e50n1160/bombas/210.csv')
    e5060_220 = info_bomba('bombas/etabloc/e50n1160/bombas/220.csv')
    e5060_232 = info_bomba('bombas/etabloc/e50n1160/bombas/232.csv')
    e5060_246 = info_bomba('bombas/etabloc/e50n1160/bombas/246.csv')
    e5060_254 = info_bomba('bombas/etabloc/e50n1160/bombas/254.csv')

    #Bombas Etabloc 050-032-250.1 n=1750
    e5050_200 = info_bomba('bombas/etabloc/e50n1750/bombas/200.csv')
    e5050_210 = info_bomba('bombas/etabloc/e50n1750/bombas/210.csv')
    e5050_220 = info_bomba('bombas/etabloc/e50n1750/bombas/220.csv')
    e5050_232 = info_bomba('bombas/etabloc/e50n1750/bombas/232.csv')
    e5050_246 = info_bomba('bombas/etabloc/e50n1750/bombas/246.csv')
    e5050_254 = info_bomba('bombas/etabloc/e50n1750/bombas/254.csv')

    #Bombas Etabloc 065-040-315 n=1160
    e6560_260 = info_bomba('bombas/etabloc/e65n1160/bombas/260.csv')
    e6560_280 = info_bomba('bombas/etabloc/e65n1160/bombas/280.csv')
    e6560_300 = info_bomba('bombas/etabloc/e65n1160/bombas/300.csv')
    e6560_318 = info_bomba('bombas/etabloc/e65n1160/bombas/318.csv')
    e6560_326 = info_bomba('bombas/etabloc/e65n1160/bombas/326.csv')

    #Bombas Etabloc 065-040-315 n=1750
    e6550_260 = info_bomba('bombas/etabloc/e65n1750/bombas/260.csv')
    e6550_280 = info_bomba('bombas/etabloc/e65n1750/bombas/280.csv')
    e6550_300 = info_bomba('bombas/etabloc/e65n1750/bombas/300.csv')
    e6550_318 = info_bomba('bombas/etabloc/e65n1750/bombas/318.csv')
    e6550_326 = info_bomba('bombas/etabloc/e65n1750/bombas/326.csv')

    # Curvas de bomba bombas/cpkn/cpkd65-315-30n3500
    c65_315_30_260 = info_bomba('bombas/cpkn/cpkd65-315-30n3500/curvas/260.csv')
    c65_315_30_280 = info_bomba('bombas/cpkn/cpkd65-315-30n3500/curvas/280.csv')
    c65_315_30_300 = info_bomba('bombas/cpkn/cpkd65-315-30n3500/curvas/300.csv')
    c65_315_30_320 = info_bomba('bombas/cpkn/cpkd65-315-30n3500/curvas/320.csv')

    # Curvas de bomba bombas/cpkn/cpkd65-315-55n1750
    c65_315_55_260 = info_bomba('bombas/cpkn/cpkd65-315-55n1750/curvas/260.csv')
    c65_315_55_280 = info_bomba('bombas/cpkn/cpkd65-315-55n1750/curvas/280.csv')
    c65_315_55_300 = info_bomba('bombas/cpkn/cpkd65-315-55n1750/curvas/300.csv')
    c65_315_55_320 = info_bomba('bombas/cpkn/cpkd65-315-55n1750/curvas/320.csv')

    # Curvas de bomba bombas/cpkn/cpkd80-400-60n1750
    c80_400_60_320 = info_bomba('bombas/cpkn/cpkd80-400-60n1750/curvas/320.csv')
    c80_400_60_340 = info_bomba('bombas/cpkn/cpkd80-400-60n1750/curvas/340.csv')
    c80_400_60_360 = info_bomba('bombas/cpkn/cpkd80-400-60n1750/curvas/360.csv')
    c80_400_60_380 = info_bomba('bombas/cpkn/cpkd80-400-60n1750/curvas/380.csv')
    c80_400_60_400 = info_bomba('bombas/cpkn/cpkd80-400-60n1750/curvas/400.csv')
    c80_400_60_404 = info_bomba('bombas/cpkn/cpkd80-400-60n1750/curvas/404.csv')

    # Curvas de bomba bombas/cpkn/cpkd100-400-122n1160
    c100_400_122_320 = info_bomba('bombas/cpkn/cpkd100-400-122n1160/curvas/320.csv')
    c100_400_122_340 = info_bomba('bombas/cpkn/cpkd100-400-122n1160/curvas/340.csv')
    c100_400_122_360 = info_bomba('bombas/cpkn/cpkd100-400-122n1160/curvas/360.csv')
    c100_400_122_380 = info_bomba('bombas/cpkn/cpkd100-400-122n1160/curvas/380.csv')
    c100_400_122_400 = info_bomba('bombas/cpkn/cpkd100-400-122n1160/curvas/400.csv')
    c100_400_122_404 = info_bomba('bombas/cpkn/cpkd100-400-122n1160/curvas/404.csv')

    # Curvas de bomba bombas/cpkn/cpkn25-160-13n3500
    c25_160_13_130 = info_bomba('bombas/cpkn/cpkn25-160-13n3500/curvas/130.csv')
    c25_160_13_140 = info_bomba('bombas/cpkn/cpkn25-160-13n3500/curvas/140.csv')
    c25_160_13_150 = info_bomba('bombas/cpkn/cpkn25-160-13n3500/curvas/150.csv')
    c25_160_13_160 = info_bomba('bombas/cpkn/cpkn25-160-13n3500/curvas/160.csv')
    c25_160_13_169 = info_bomba('bombas/cpkn/cpkn25-160-13n3500/curvas/169.csv')

    # Curvas de bomba bombas/cpkn/cpkn25-200-14n3500
    c25_200_14_160 = info_bomba('bombas/cpkn/cpkn25-200-14n3500/curvas/160.csv')
    c25_200_14_190 = info_bomba('bombas/cpkn/cpkn25-200-14n3500/curvas/190.csv')
    c25_200_14_209 = info_bomba('bombas/cpkn/cpkn25-200-14n3500/curvas/209.csv')

    # Curvas de bomba bombas/cpkn/cpkn32-125-15n3500
    c32_125_15_100 = info_bomba('bombas/cpkn/cpkn32-125-15n3500/curvas/100.csv')
    c32_125_15_120 = info_bomba('bombas/cpkn/cpkn32-125-15n3500/curvas/120.csv')
    c32_125_15_139 = info_bomba('bombas/cpkn/cpkn32-125-15n3500/curvas/139.csv')

    # Curvas de bomba bombas/cpkn/cpkn80-200-115n1160
    c80_200_115_140 = info_bomba('bombas/cpkn/cpkn80-200-115n1160/curvas/140.csv')
    c80_200_115_160 = info_bomba('bombas/cpkn/cpkn80-200-115n1160/curvas/160.csv')
    c80_200_115_180 = info_bomba('bombas/cpkn/cpkn80-200-115n1160/curvas/180.csv')
    c80_200_115_200 = info_bomba('bombas/cpkn/cpkn80-200-115n1160/curvas/200.csv')
    c80_200_115_209 = info_bomba('bombas/cpkn/cpkn80-200-115n1160/curvas/209.csv')

    # Curvas de bomba bombas/etanorm-r/Etanorm250-330n1750
    em250_330_290 = info_bomba('bombas/etanorm-r/Etanorm250-330n1750/curvas/290.csv')
    em250_330_310 = info_bomba('bombas/etanorm-r/Etanorm250-330n1750/curvas/310.csv')
    em250_330_330 = info_bomba('bombas/etanorm-r/Etanorm250-330n1750/curvas/330.csv')

    # Curvas de bomba bombas/etanorm-r/Etanorm250-400n1750
    em250_400_340 = info_bomba('bombas/etanorm-r/Etanorm250-400n1750/curvas/340.csv')
    em250_400_360 = info_bomba('bombas/etanorm-r/Etanorm250-400n1750/curvas/360.csv')
    em250_400_380 = info_bomba('bombas/etanorm-r/Etanorm250-400n1750/curvas/380.csv')
    em250_400_405 = info_bomba('bombas/etanorm-r/Etanorm250-400n1750/curvas/405.csv')

    # Curvas de bomba bombas/etanorm-r/Etanorm300-360n1750
    em300_360_320 = info_bomba('bombas/etanorm-r/Etanorm300-360n1750/curvas/320.csv')
    em300_360_340 = info_bomba('bombas/etanorm-r/Etanorm300-360n1750/curvas/340.csv')
    em300_360_360 = info_bomba('bombas/etanorm-r/Etanorm300-360n1750/curvas/360.csv')

    # Curvas de bomba bombas/etanorm-r/Etanorm300-400n1750
    em300_400_360 = info_bomba('bombas/etanorm-r/Etanorm300-400n1750/curvas/360.csv')
    em300_400_380 = info_bomba('bombas/etanorm-r/Etanorm300-400n1750/curvas/380.csv')
    em300_400_400 = info_bomba('bombas/etanorm-r/Etanorm300-400n1750/curvas/400.csv')
    em300_400_420 = info_bomba('bombas/etanorm-r/Etanorm300-400n1750/curvas/420.csv')
    em300_400_430 = info_bomba('bombas/etanorm-r/Etanorm300-400n1750/curvas/430.csv')

    # Curvas de bomba bombas/megacpk/mega40-025-160n3500
    m40_025_160_135 = info_bomba('bombas/megacpk/mega40-025-160n3500/curvas/135.csv')
    m40_025_160_145 = info_bomba('bombas/megacpk/mega40-025-160n3500/curvas/145.csv')
    m40_025_160_165 = info_bomba('bombas/megacpk/mega40-025-160n3500/curvas/165.csv')
    m40_025_160_169 = info_bomba('bombas/megacpk/mega40-025-160n3500/curvas/169.csv')

    # Curvas de bomba bombas/megacpk/mega40-025-200n3500
    m40_025_200_165 = info_bomba('bombas/megacpk/mega40-025-200n3500/curvas/165.csv')
    m40_025_200_180 = info_bomba('bombas/megacpk/mega40-025-200n3500/curvas/180.csv')
    m40_025_200_195 = info_bomba('bombas/megacpk/mega40-025-200n3500/curvas/195.csv')
    m40_025_200_205 = info_bomba('bombas/megacpk/mega40-025-200n3500/curvas/205.csv')
    m40_025_200_209 = info_bomba('bombas/megacpk/mega40-025-200n3500/curvas/209.csv')

    # Curvas de bomba bombas/megacpk/mega50-032-125.1n3500
    m50_032_1251_114 = info_bomba('bombas/megacpk/mega50-032-125.1n3500/curvas/114.csv')
    m50_032_1251_124 = info_bomba('bombas/megacpk/mega50-032-125.1n3500/curvas/124.csv')
    m50_032_1251_134 = info_bomba('bombas/megacpk/mega50-032-125.1n3500/curvas/134.csv')
    m50_032_1251_139 = info_bomba('bombas/megacpk/mega50-032-125.1n3500/curvas/139.csv')

    # Curvas de bomba bombas/megacpk/mega50-032-125.1n3500
    m50_032_125_110 = info_bomba('bombas/megacpk/mega50-032-125n3500/curvas/110.csv')
    m50_032_125_120 = info_bomba('bombas/megacpk/mega50-032-125n3500/curvas/120.csv')
    m50_032_125_130 = info_bomba('bombas/megacpk/mega50-032-125n3500/curvas/130.csv')
    m50_032_125_139 = info_bomba('bombas/megacpk/mega50-032-125n3500/curvas/139.csv')

    # Curvas de bomba bombas/megacpk/mega50-032-160n3500
    m50_032_160_135 = info_bomba('bombas/megacpk/mega50-032-160n3500/curvas/135.csv')
    m50_032_160_150 = info_bomba('bombas/megacpk/mega50-032-160n3500/curvas/150.csv')
    m50_032_160_162 = info_bomba('bombas/megacpk/mega50-032-160n3500/curvas/162.csv')
    m50_032_160_174 = info_bomba('bombas/megacpk/mega50-032-160n3500/curvas/174.csv')

    # Curvas de bomba bombas/megacpk/mega50-032-200n3500
    m50_032_200_170 = info_bomba('bombas/megacpk/mega50-032-200n3500/curvas/170.csv')
    m50_032_200_180 = info_bomba('bombas/megacpk/mega50-032-200n3500/curvas/180.csv')
    m50_032_200_193 = info_bomba('bombas/megacpk/mega50-032-200n3500/curvas/193.csv')
    m50_032_200_206 = info_bomba('bombas/megacpk/mega50-032-200n3500/curvas/206.csv')
    m50_032_200_209 = info_bomba('bombas/megacpk/mega50-032-200n3500/curvas/209.csv')

    #Lista de bombas Etabloc
    bombas_total = [
    e5060_200, e5060_210, e5060_220, e5060_232, e5060_246, e5060_254,
    e5050_200, e5050_210, e5050_220, e5050_232, e5050_246, e5050_254,
    e6560_260, e6560_280, e6560_300, e6560_318, e6560_326,
    e6550_260, e6550_280, e6550_300, e6550_318, e6550_326,
    c65_315_30_260, c65_315_30_280, c65_315_30_300, c65_315_30_320,
    c65_315_55_260, c65_315_55_280, c65_315_55_300, c65_315_55_320,
    c80_400_60_320, c80_400_60_340, c80_400_60_360, c80_400_60_380, c80_400_60_400, c80_400_60_404,
    c100_400_122_320, c100_400_122_340, c100_400_122_360, c100_400_122_380, c100_400_122_400, c100_400_122_404,
    c25_160_13_130, c25_160_13_140, c25_160_13_150, c25_160_13_160, c25_160_13_169,
    c25_200_14_160, c25_200_14_190, c25_200_14_209,
    c32_125_15_100, c32_125_15_120, c32_125_15_139,
    c80_200_115_140, c80_200_115_160, c80_200_115_180, c80_200_115_200, c80_200_115_209,
    em250_330_290, em250_330_310, em250_330_330,
    em250_400_340, em250_400_360, em250_400_380, em250_400_405,
    em300_360_320, em300_360_340, em300_360_360,
    em300_400_360, em300_400_380, em300_400_400, em300_400_420, em300_400_430,
    m40_025_160_135, m40_025_160_145, m40_025_160_165, m40_025_160_169,
    m40_025_200_165, m40_025_200_180, m40_025_200_195, m40_025_200_205, m40_025_200_209,
    m50_032_1251_114, m50_032_1251_124, m50_032_1251_134, m50_032_1251_139,
    m50_032_125_110, m50_032_125_120, m50_032_125_130, m50_032_125_139,
    m50_032_160_135, m50_032_160_150, m50_032_160_162, m50_032_160_174,
    m50_032_200_170, m50_032_200_180, m50_032_200_193, m50_032_200_206, m50_032_200_209
    ]
    return bombas_total

def tablas_vmoa():
    # Curvas de bomba VMOA 100
    v100_188 = info_bomba('bombas/VMOA/VMOA100/188.csv')
    v100_182 = info_bomba('bombas/VMOA/VMOA100/182.csv')
    v100_160 = info_bomba('bombas/VMOA/VMOA100/160.csv')
    v100_082 = info_bomba('bombas/VMOA/VMOA100/082.csv')
    v100_060 = info_bomba('bombas/VMOA/VMOA100/060.csv')

    # Curvas de bomba VMOA 150
    v150_190 = info_bomba('bombas/VMOA/VMOA150/190.csv')
    v150_182 = info_bomba('bombas/VMOA/VMOA150/182.csv')
    v150_175 = info_bomba('bombas/VMOA/VMOA150/175.csv')
    v150_167 = info_bomba('bombas/VMOA/VMOA150/167.csv')
    v150_160 = info_bomba('bombas/VMOA/VMOA150/160.csv')

    vmoa = [
            v100_188, v100_182, v100_160, v100_082, v100_060,
            v150_190, v150_182, v150_175, v150_167, v150_160,
           ]

    return vmoa

def ecuacion_bomba(df):
    Qlist = []
    Hlist = []
    for value in df['qlmin']:
        if math.isnan(value) == False:
            Qlist.append(value)

    for value in df['hm']:
        if math.isnan(value) == False:
            Hlist.append(value)

    Q = numpy.array(Qlist, dtype=float)  # Q(l/min)
    H = numpy.array(Hlist, dtype=float)  # H(m)
    e_bomba = numpy.polyfit(Q, H, 3) #Dada la forma p1*x^3+p2*x^2+p3*x+p4 [p1, p2, p3, p4]
    return e_bomba



