""" Programa Apoyo multas#
    incorpora al modulo multas.py
    Daniel Valencia Cordero
    Mayo 3-2021 """

#---------------- Zona librerias------------
import multas as mult
#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================
distancia_uno = int(input("Digite el valor de la distancia 1: \n"))
distancia_dos = int(input("Digite el valor de la distancia 2: \n"))
tiempo = int(input("Digie el tiempo que demoro: \n"))
ms_vlocidad, ms_alcolemia = mult. multar_velocidad(distancia_uno, distancia_dos,tiempo)

print("Mensaje multa de velocidad: "+ms_vlocidad+"\n")
print("Mensaje multa de alcoholemia: "+ms_alcolemia+"\n")