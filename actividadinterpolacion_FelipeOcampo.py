import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

# Rango de movimiento
deltabeta = np.array([20, 40, 60, 80]) #Valores en grados

#Valores para criterios de rectitud
deltaxL2 = np.array([0.601, 1.193, 1.763, 2.299]) 
LinkRatiosR1 = np.array([2.975, 2.950, 2.900, 2.825])
LinkRatiosR3 = np.array([3.963, 3.925, 3.850, 3.738])

#Valores para criterios de velocidad
deltaxV2= np.array([0.480, 0.950, 1.411, 1.845])  
LinkRatiosR1V= np.array([2.075, 2.050, 2.025, 1.975])
LinkRatiosR3V= np.array([2.613, 2.575, 2.538, 2.463])

##Procedimiento
n = len(deltabeta) #Longitud de array
x = sym.Symbol('x')

#Inicializar polinomios para ambas soluciones

##Polinomios para criterio de rectitud
polinomioL2 = 0
polinomioL1 = 0
polinomioL3 = 0
##Polinomios para criterios de velocidad
polinomioL2V = 0
polinomioL1V = 0
polinomioL3V = 0


for i in range(0,n,1):
    numerador = 1
    denominador = 1
    for j in range(0,n,1):
        if (i != j):
            numerador = numerador*(x-deltabeta[j])
            denominador = denominador*(deltabeta[i]-deltabeta[j])

        # Cálculo de los términos de Lagrange 
        ##Terminos para criterios de rectitud en sus longitudes (L1, L2 y L3)
        terminoL2 = (numerador/denominador)*deltaxL2[i]
        terminoL1 = (numerador/denominador)*LinkRatiosR1[i]
        terminoL3 = (numerador/denominador)*LinkRatiosR3[i]
        ###Terminos para criterios de velocidad en sus longitudes (L1, L2 y L3)
        terminoV2 = (numerador/denominador)*deltaxV2[i]
        terminoR1V = (numerador/denominador)*LinkRatiosR1V[i]
        terminoR3V = (numerador/denominador)*LinkRatiosR3V[i]

    ##Polimonios para criterios de rectitud
    polinomioL2 = polinomioL2 + terminoL2
    polinomioL1 = polinomioL1 + terminoL1
    polinomioL3 = polinomioL3 + terminoL3

    #Polinomios para criterios de velocidad
    polinomioL2V = polinomioL2V + terminoV2
    polinomioL1V = polinomioL1V + terminoR1V
    polinomioL3V = polinomioL3V + terminoR3V

# Simplificación de ecuaciones
##Ecuaciones para criterios de rectitud
polisimpleL2 = sym.expand(polinomioL2)
polisimpleL1 = sym.expand(polinomioL1)
polisimpleL3 = sym.expand(polinomioL3)
##Ecuaciones para criterios de velocidad
polisimpleL2V = sym.expand(polinomioL2V)
polisimpleL1V = sym.expand(polinomioL1V)
polisimpleL3V = sym.expand(polinomioL3V)

# Forma lamda de los polinomios
##Criterio de rectitud
pxL2 = sym.lambdify(x, polinomioL2)
pxL1 = sym.lambdify(x, polinomioL1)
pxL3 = sym.lambdify(x, polinomioL3)
##Criterio de velocidad
pxL2V = sym.lambdify(x, polinomioL2V)
pxL1V = sym.lambdify(x, polinomioL1V)
pxL3V = sym.lambdify(x, polinomioL3V)


#Cálculo de punto en criterio de rectitud
p55L2 = pxL2(55)
p55L1= pxL1(55)
p55L3= pxL3(55)
#Cálculo de punto en criterio de velocudad
p55LV2= pxL2V(55)
p55LV1= pxL1V(55)
p55LV3= pxL3V(55)

# Cálculo de longitudes para criterio de rectitud
#Cálculo L2
Deltax= 20 #Medida en cm
L2= Deltax/ p55L2 #Valor L2
# Calculo L1
L1= L2*p55L1 #Valor L1
# Calculo L3
L3= L2*p55L3 #Valor L3

# Cálculo de longitudes para criterio de velocidad
#Cálculo L2
Deltax= 20 #Medida en cm
L2V= Deltax/ p55LV2 #Valor L2
# Calculo L1
L1V= L2V*p55LV1 #Valor L1
# Calculo L3
L3V= L2V*p55LV3 #Valor L3

#Salida de valores
print('Dimensiones obtenidas')
print('Criterio de rectitud')
print('Valor L1:')
print(L1)
print('Valor L2:')
print(L2)
print('Valor L3:')
print(L3)
print('Criterio de velocidad')
print('Valor L1:')
print(L1V)
print('Valor L2:')
print(L2V)
print('Valor L3:')
print(L3V)
