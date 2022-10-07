"""
código referente a aula 4 e 2º experimento sobre "Capacitor em regime AC"
resistor 0.992 kohm
capacitor 219.1 nF -> 0.219 uF
milivolt -> 10^-3
"""
import math

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

for count in range(len(i_ef)):
    xc.append(v_cef[count]/i_ef[count])

print(f'Xc: {xc}')
