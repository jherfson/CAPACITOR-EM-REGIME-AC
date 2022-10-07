"""
código referente a aula 4 e 2º experimento sobre "Capacitor em regime AC"
resistor 0.992 kohm
capacitor 219.1 nF -> 0.219 uF
milivolt -> 10^-3
"""
import math
import numpy as np
from scipy.optimize import curve_fit
resitor = 0.992
capacitor = 219.1

v_rpps = [1.01, 2.00, 3.00, 3.72, 4.72]
v_cpps = [0.766, 1.60, 2.24, 2.76, 3.50]


def v_ef(vpp):
    """
    Agora cálcular o valor da Vref
    para isso vamos usar as expressões
    Vp = Vpp/2
    Vef = Vp/sqrt(raiz(2))
    """
    vp = vpp / 2
    return vp / math.sqrt(2)


# tensão efetiva do resistor
v_ref = [v_ef(vpp) for vpp in v_rpps]
print(f"VRef: {v_ref}")

# tensão efetiva do capacitor
v_cef = [v_ef(cpp) for cpp in v_cpps]
print(f"VCef: {v_cef}")

# Corrente efetiva
# r -> 992
i_ef = [v / 992 for v in v_ref]

print(f"Ief: {i_ef}")

xc =[]
frequencia = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for count in range(len(i_ef)):
    xc.append(v_cef[count]/i_ef[count])

print(f'Xc: {xc}')
# segunda tabela
vrpp = [3.88, 4.40, 4.56, 4.64, 4.68, 4.64, 4.64, 4.68, 4.72, 4.72]
vcpp = [2.70, 1.62, 1.12, 0.856, 0.688, 0.612, 0.492, 0.456, 0.4, 0.356]

vref = [v_ef(r) for r in vrpp]
vcef = [v_ef(c) for c in vcpp]

ief = [r/992 for r in vref]
print(f'I_EF: {ief}')
xc_2 = []
for index in range(len(ief)):
    xc_2.append(vcef[index]/ief[index])

print(f'XC_2: {xc_2}')

def reatancia(frequencia, c):
    return (1/2*math.pi*c)*(1/np.array(frequencia))

param, param_cov = curve_fit(reatancia, frequencia, xc_2)

print(f'param: {param}')
print(f'param_cov: {param_cov}')
y_c = ((1/2*np.pi*param[0])*(1/np.array(frequencia)))

from matplotlib import pyplot as plt

plt.plot(frequencia, xc_2, 'o', color='red', label='data')
plt.plot(frequencia, y_c, '-', color='blue', label='fit')
plt.legend()
plt.show()
