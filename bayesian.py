#/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
"""
Universidad Autónoma de Ciudad Juárez
Sistemas Inteligentes
Teorema Bayesiano
David Elizondo Ramírez
148786

== Práctica ==

Considerando las cuatro hipótesis iniciales: 
P[H1]: 0.3
P[H2]: 0.4
P[H3]: 0.2
P[H3]: 0.1

y las siguientes probabilidades condicionales: 
P[A|H1]: 0.45
P[B|H1]: 0.3
P[C|H1]: 0.2
P[D|H1]: 0.05

P[A|H2]: 0.15
P[B|H2]: 0.55
P[C|H2]: 0.2
P[D|H2]: 0.05

P[A|H3]: 0.05
P[B|H3]: 0.1
P[C|H3]: 0.65
P[D|H3]: 0.2

P[A|H4]: 0.05
P[B|H4]: 0.15
P[C|H4]: 0.3
P[D|H4]: 0.5

Observar cómo se modifica la creencia en la hipótesis un n número de
iteraciones con los experimentos alimentados por el usuario a tráves
de la consola, utilizando la fórmula bayesiana.

"""
 
inicial = [0.3, 0.4, 0.2, 0.1] #valores predeterminados
inicialcopia = [0.0, 0.0, 0.0, 0.0]
h1 = [0.45, 0.3, 0.2, 0.05] #valores predeterminados
h2 = [0.15, 0.55, 0.2, 0.1] #valores predeterminados
h3 = [0.05, 0.1, 0.65, 0.2] #valores predeterminados
h4 = [0.05, 0.15, 0.3, 0.5] #valores predeterminados
califs = []

i=0
x=0
print("Ingrese número de iteraciones: ")
x = int(input())

while i < x: 
    print ("Ingrese valor", i+1, ": ")
    califs.append(input())
    i+=1 #incrementador

def bayesian(var):
    inicialcopia[0] = ((inicial[0] * h1[var]) / ((inicial[0] * h1[var]) + (inicial[1] * h2[var]) + (inicial[2] * h3[var]) + (inicial[3] * h4[var])))
    inicialcopia[1] = ((inicial[1] * h2[var]) / ((inicial[0] * h1[var]) + (inicial[1] * h2[var]) + (inicial[2] * h3[var]) + (inicial[3] * h4[var])))
    inicialcopia[2] = ((inicial[2] * h3[var]) / ((inicial[0] * h1[var]) + (inicial[1] * h2[var]) + (inicial[2] * h3[var]) + (inicial[3] * h4[var])))
    inicialcopia[3] = ((inicial[3] * h4[var]) / ((inicial[0] * h1[var]) + (inicial[1] * h2[var]) + (inicial[2] * h3[var]) + (inicial[3] * h4[var])))
    return inicialcopia
    
def imprime(inic): #imprime los números
    j=0
    inicial = inic.copy()
    while j<4:
        print("Nuevo valor de H", j+1, ":", inicial[j])
        j+=1
    print("\n")
    return inicial

print("Ud. ingresó:", califs, "\n")

h=0
while h < x: #función ultra fregonsota la bayesiana
    if califs[h] == 'A':
        variable = 0
        inicialcopia = bayesian(variable)
        print("== Iteración", h+1, "==")
        print("== Se eligió A ==\n")
        inicial = imprime(inicialcopia)
    if califs[h] == 'B':
        variable = 1
        inicialcopia = bayesian(variable)
        print("== Iteración", h+1, "==")
        print("== Se eligió B ==\n")
        inicial = imprime(inicialcopia)
    if califs[h] == 'C':
        variable = 2
        inicialcopia = bayesian(variable)
        print("== Iteración", h+1, "==")
        print("== Se eligió C ==\n")
        inicial = imprime(inicialcopia)
    if califs[h] == 'D':
        variable = 3
        inicialcopia = bayesian(variable)
        print("== Iteración", h+1, "==")
        print("== Se eligió D ==\n")
        inicial = imprime(inicialcopia)
    h+=1
