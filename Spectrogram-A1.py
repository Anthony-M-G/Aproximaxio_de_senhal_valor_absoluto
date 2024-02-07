# UNIVERSIDAD DE COSTA RICA - SEDE GUANACASTE
# IE-0247 SEÑALES Y SISTEMAS I
# PROYECTO 3: Espectrograma de Archivos Audibles.
# PROGRAMA 3B: Definición y Generación de Espectrogramas en Python.
# PROFESOR: Ing. Luis Carlos García Serrano.
# Archivo Modificado por los estudiantes: Anthony Medina García - Gerardo Jara Rojas
# Archivo principal realizado por: Dr. Alejandro Delgado Castro
# DESCRIPCIÓN: Este programa genera el espectrograma de una señal de prueba.
# Determinación de la nota musical presenta en los archivos audibles mediante el uso de un espectrograma.
# -----------------------------------------------------------------------------------------------
# LIBRERÍAS
# -----------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp


# -----------------------------------------------------------------------------------------------
# FUNCIONES PROPIAS
# -----------------------------------------------------------------------------------------------
def mouse_event(event):
    print(f"Punto --> t: {event.xdata:.3f} s ; f: {event.ydata:.3f} Hz")


# -----------------------------------------------------------------------------------------------
# DEFINICIÓN DE PARÁMETROS
# -----------------------------------------------------------------------------------------------
F_Size = 2048

# -----------------------------------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# -----------------------------------------------------------------------------------------------
# Encabezado.
print("UNIVERSIDAD DE COSTA RICA - SEDE DE GUANACASTE LIBERIA")
print("IE-0247 Señales y Sistemas I")
print("Determinación Nota Musical en el Archivo de Audio Número 2.")
print("Prof: Ing. Luis Carlos García Serrano")
print("Estudiantes:")
print("Jara Rojas Gerardo B93970")
print("Medina García Anthony C14600")
print("Proyecto 3")
print("II Semestre 2023\n")
input("Por favor presione enter para continuar con el código:\n")
# Definiendo parámetro: Tamaño de Trama.
print(f"Parámetros: Tamaño de Trama = {F_Size}")
# -----------------------------------------------------------------------------------------------
# Lectura de Archivo de Audio con la Señal de Prueba.
print("Leyendo Archivo WAV con Señal de Prueba...")
# Abrir un Archivo WAV.
# Arreglo para abrir archivos con diferentes frecuencias.
# Archivo de Audio Número 1:
sr, Audio_Ori = sp.io.wavfile.read("N02_331FLNOF.wav")
# Cambiar de Escala a -1.0 -- 1.0.
if Audio_Ori.dtype == 'int16':
    # -> Muestras son de 16-bit
    nb_bits = 16
elif Audio_Ori.dtype == 'int32':
    # -> Muestras son de 32-bit
    nb_bits = 32
else:
    # -> Muestras son de 24-bit
    nb_bits = 24
# Calcular Valor Máximo por Muestra.
max_value = float(2 ** (nb_bits - 1))
Signal = Audio_Ori / (max_value + 1)
# Mensaje.
print("Proceso de lectura completo.\n")

# -----------------------------------------------------------------------------------------------
# Intervalo de muestreo.
Ts = 1/sr
# Número de Muestras.
L_Sig = np.shape(Signal)[0]
# Duración de la Señal.
t_max = Ts * (L_Sig - 1)
# Eje del Tiempo.
t_eje = np.linspace(0, t_max, L_Sig)

# -----------------------------------------------------------------------------------------------
# Gráficar la Señal de Prueba en el Dominio del Tiempo.
plt.figure(num=1, figsize=[12, 6])
plt.plot(t_eje, Signal)
plt.grid()
plt.xlim([0, t_max])
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.title("Señal de Prueba en el Dominio del Tiempo")
plt.show(block=False)

# -----------------------------------------------------------------------------------------------
# Cálculo del espectrograma (STFT) de la señal de prueba.
f, t, MagSP = sp.signal.spectrogram(Signal, fs=sr, window="hann", nperseg=F_Size,
                                    noverlap=3*F_Size//4, nfft=F_Size, mode="magnitude")
# Aplicar logaritmo.
MagSP = 10 * np.log10(MagSP)
# Gráfica del espectrograma de magnitud.
plt.rcParams["figure.autolayout"] = True
fig = plt.figure(num=2, figsize=[12, 6])
cid = fig.canvas.mpl_connect('button_press_event', mouse_event)
plt.pcolormesh(t, f, MagSP, vmin=np.min(MagSP), vmax=np.max(MagSP), shading="gouraud")
#A continuación se ajusta los límites del eje y con el propósito de encontrar la frecuencia fundamental del audio.

plt.ylim([0, 2850])
plt.ylabel("Frecuencia (Hz)")
plt.xlabel("Tiempo (s)")
plt.title("Espectrograma de la Señal de Prueba")
plt.show()

# -----------------------------------------------------------------------------------------------
# Final del programa.
input("Presione ENTER para terminar...")
