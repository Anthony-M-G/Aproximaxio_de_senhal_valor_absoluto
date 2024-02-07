# UNIVERSIDAD DE COSTA RICA - SEDE GUANACASTE
# IE-0247 SEÑALES Y SISTEMAS I
# PROYECTO 1: Parte 2.
# Programa Código: Obtención señal Valor Absoluto Sen(t).
# Profesor: Ing. Luis Carlos García Serrano.
# Realizado por:
# Anthony Medina García C14600
# Gerardo Jara Rojas B93970
# II Semestre 2023
# Fecha de entrega: 03/10/2023

# DESCRIPCIÓN: El presente programa genera una aproximación para la señal del valor absoluto del seno, a partir de la
# aplicación de la serie de fourier de dicha señal y seguidamente se presenta su gráfica considerando N términos y una
# frecuencia f0.
# -----------------------------------------------------------------------------------------------
# IMPORTANDO LIBRERÍAS A UTILIZAR:
# -----------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# -----------------------------------------------------------------------------------------------
# Variables a Definir.
# Número de Puntos para las Señales.
Puntos = 1500
# Se decide utilizar 1500 puntos con el fin de obtener una mejor aproximación en la gráfica.

# Número de Ciclos a Visualizar.
Ciclos = 2

# Frecuencia de la Señal.
# El periodo para dicha señal es de π; por lo tanto:
f0 = 1 / np.pi

# Amplitud de la Señal.
Amp = 1

# Número de Armónicos.
N = 100

# -----------------------------------------------------------------------------------------------
# Otros Parámetros de la Señal.
# Período.
T = (1) / f0
# Frecuencia Angular.
w0 = 2 * np.pi * f0
# Duración.
t_max = Ciclos * T

# -----------------------------------------------------------------------------------------------
# Encabezado.
print("\nUNIVERSIDAD DE COSTA RICA - SEDE DE GUANACASTE")
print("IE-0247 Señales y Sistemas I\n")
print("Proyecto 1: Parte 2.\n")
print("Estudiantes:\n")
print("            Anthony Medina García C14600")
print("            Gerardo Jara Rojas B93970")
print("Aplicaciones: Aproximación de la Señal Valor Absoluto Seno por Series de Fourier\n")
print(f"Variables: Frecuencia: {f0:.2f} Hz")
print(f"           Número de Armónicos: {N:.0f}")
print(f"           Número de Ciclos: {Ciclos:.0f}")
print(f"           Número de Puntos: {Puntos:.0f}\n")

# -----------------------------------------------------------------------------------------------
# Generar Arreglos de Coeficientes an y bn.
print("Generando coeficientes an y bn de la serie...")
# Generación de Coeficientes:
a0 = (4) / (np.pi)
an = np.zeros([1, N + 1])
bn = np.zeros([1, N + 1])

# Ciclo de Cálculo: El ciclo For no tiene ninguna restricción para n, es decir, n puede ser par e impar. Por lo tanto
# se realizan las correspondientes modificaciones para que el ciclo for acepte cualquier número n.
for n in range(1, N + 1):
    # Calcular Coeficiente con Fórmula.
    an[0, n] = (-4 * Amp) / ((4 * np.pi * n **2)-np.pi)
# Coeficiente an calculado en la Primera Parte del Presente proyecto.
# Observación: El valor absoluto del seno es una señal par, por lo tanto, su coeficiente bn es igual a cero.
# -----------------------------------------------------------------------------------------------
# Generación de los Armónicos de la Señal desde n = 0 hasta n = N.
print("Generando armónicos y señal cuadrada aproximada...")
# Creación del Eje del Tiempo (t).
t = np.linspace(0, t_max, Puntos)
# Arreglo-Matriz para Almacenar los Armónicos de la Señal.
Harmonics = np.zeros([N + 1, Puntos])
# Generación de Armónicos.
for n in range(0, N + 1):
    # Revisar si n = 0
    if n == 0:
        # Generar Componente Fundamental. Coeficiente a0 calculado en la primera parte del presente proyecto.
        Harmonics[n, :] = (a0 / 2) * np.ones([1, Puntos])
    else:
        # Generar un Armónico.
        Harmonics[n, :] = an[0, n] * np.cos(n*w0*t) + bn[0, n] * np.sin(n*w0*t)
# Sumar los Armónicos para Generar la Señal Aproximada.
Signal = np.sum(Harmonics, 0)

# -----------------------------------------------------------------------------------------------
# Gráfica con los Armónicos de la Señal.
print("Generando gráfica de los armónicos...")
# Crear Ventana de Gráfico.
plt.figure(figsize=[24, 12])
# Ciclo para Generar Gráficas de Armónicos.
for n in range(0, N + 1):
    # Graficar Armónico.
    if n == 0 or np.sum(Harmonics[n, :]) != 0:
        plt.plot(t, Harmonics[n, :])
# Formato del Gráfico.
plt.xlim([0, t_max])
plt.grid()
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (V)")
plt.title("Armónicos de la Señal Valor Absoluto Seno")
plt.show()

# -----------------------------------------------------------------------------------------------
print("Generando gráfica de la señal aproximada...\n")
# Graficando Señal Aproximada.
plt.figure(figsize=[24, 12])
plt.plot(t, Signal)
# Formato del Gráfico.
plt.xlim([0, t_max])
plt.grid()
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud (V)")
plt.title("Aproximación de la Señal Valor Absoluto Seno con " + str(N) + " Armónicos")
plt.show()

# -----------------------------------------------------------------------------------------------
# Final del Programa.
print("Final del Programa...")