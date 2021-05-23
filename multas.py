""" Modulo Multas
    Funciones para el cálculo de multas
    de tránsito 
    Daniel Valencia Cordero
    Mayo 10-2021 """
# Definición de Funciones

def velocidad(recorrido,tiempo):
  return(recorrido//tiempo)

def recorrido(disInicial, disFinal):
  return (disFinal-disInicial)

def multar_velocidad(distancia_uno, distancia_dos,tiempo):
  recorTotal = recorrido(distancia_dos,distancia_uno)
  velo = velocidad(recorTotal,tiempo) 
  if(velo <= 20):
    return "llamado de atención por baja velocidad","No se hace"
  elif(velo >= 21 and velo <= 60):
    return "Normal"
  elif(velo >= 61 and velo <= 80):
    return "llamado de atención por alta velocidad","No se hace"
  elif(velo >= 81 and velo <= 120):
    print("Realizar prueba de alcoholimetria y digite el valor dado aqu: \n")
    grado = int(input())
    return "multa tipo I",multar_alcoholemia(grado)
  elif(velo >= 121):
    print("Realizar prueba de alcoholimetria y digite el valor dado aqu: \n")
    grado = int(input())
    return "multa tipo II e inmovilización del vehículo",multar_alcoholemia(grado)

def multar_alcoholemia(grado_alcohol):
#TODO: Documentar función 
  if(grado_alcohol >= 20 and grado_alcohol <= 39):
    return "Por tener entre 20 y 39 mg de etanol/l00ml, además de las sanciones previstas en la presente ley, se decretará la suspensión de la licencia de conducción entre seis (6) y doce (12) meses."
  elif(grado_alcohol >= 40 and grado_alcohol <= 99):
    return "Primer grado de embriaguez entre 40 y 99 mg de etanol/100 ml de sangre total, adicionalmente a la sanción multa, se decretará la suspensión de la Licencia de Conducción entre uno (1) y tres (3) años."
  elif(grado_alcohol >= 100 and grado_alcohol <= 149):
    return "Segundo grado de embriaguez entre 100 y 149 mg de etanol/100 ml de sangre total, adicionalmente a la sanción multa, se decretará la suspensión de la Licencia de Conducción entre tres (3) y cinco (5) años, y la obligación de realizar curso de sensibilización, conocimientos y consecuencias de la alcoholemia y drogadicción en centros de rehabilitación debidamente autorizados, por un mínimo de cuarenta (40) horas."
  elif(grado_alcohol >= 150):
    return "Tercer grado de embriaguez, desde 150 mg de etanol/100 ml de sangre total en adelante, adicionalmente a la sanción de la sanción de multa, se decretará la suspensión entre cinco (5) y diez (10) años de la Licencia de Conducción, y la obligación de realizar curso de sensibilización, conocimientos y consecuencias de la alcoholemia y drogadicción en centros de rehabilitación debidamente autorizados, por un mínimo de ochenta (80) horas."


