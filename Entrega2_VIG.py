## ENTREGA 2
## VICTOR IGLESIAS GONZALEZ
## MASTER EN IA

import math
import numpy as np
import random

# Definir el diccionario de modelos de automóviles
modelos_de_automoviles = {
    "Kia Picanto": {"Categoría": "A", "Plazas": 5, "Mín. (días)": 1, "Coste (€/día)": 8, "Descuento (días min)": "10% (>4)"},
    "Chevrolet Matiz": {"Categoría": "A", "Plazas": 5, "Mín. (días)": 1, "Coste (€/día)": 7},
    "Citroën C1": {"Categoría": "A", "Plazas": 4, "Mín. (días)": 3, "Coste (€/día)": 5, "Descuento (días min)": "12% (>5)"},
    "Opel Corsa": {"Categoría": "B", "Plazas": 4, "Mín. (días)": 2, "Coste (€/día)": 8},
    "Seat Ibiza": {"Categoría": "B", "Plazas": 4, "Mín. (días)": 3, "Coste (€/día)": 8},
    "VW Caddy": {"Categoría": "C", "Plazas": 7, "Mín. (días)": 6, "Coste (€/día)": 9, "Descuento (días min)": "5% (>3)"},
    "Opel Zafira": {"Categoría": "D", "Plazas": 9, "Mín. (días)": 5, "Coste (€/día)": 12, "Descuento (días min)": "8% (>4)"},
    "Peugeot Expert": {"Categoría": "D", "Plazas": 9, "Mín. (días)": 1, "Coste (€/día)": 27},
    "Hyundau Tucson": {"Categoría": "D", "Plazas": 7, "Mín. (días)": 5, "Coste (€/día)": 20},
    "Mercedes Clase E": {"Categoría": "E", "Plazas": 5, "Mín. (días)": 5, "Coste (€/día)": 15, "Descuento (días min)": "10% (>7)"},
    "Jaguar XF": {"Categoría": "E", "Plazas": 5, "Mín. (días)": 7, "Coste (€/día)": 30},
    "VW Polo": {"Categoría": "B", "Plazas": 5, "Mín. (días)": 2, "Coste (€/día)": 12, "Descuento (días min)": "5% (>5)"}
}

dia_reco = int(input('Indica el dia de recogida del vehículo: '))
dia_entrega = int(input('Indica el dia de entrega del vehiculo: '))
plazas = int(input('Indica el numero de plazas que necesitas en tu coche: '))

dias_tot = dia_entrega - dia_reco

modelos_disponibles = []

for modelo in modelos_de_automoviles:
    if (modelos_de_automoviles[modelo]["Plazas"] >= plazas) and (modelos_de_automoviles[modelo]["Mín. (días)"] <= dias_tot):
        modelos_disponibles.append(modelo)

precio_modelo = []

print(100*'-')
print("Este es el listado de vehículos disponibles junto a su precio total: ", modelos_disponibles)
print(100*'-')

for i in range(len(modelos_disponibles)):
    if modelos_disponibles[i] == 'Kia Picanto' and dias_tot >= 4:
        print(modelos_disponibles[i], ((modelos_de_automoviles[modelos_disponibles[i]]["Coste (€/día)"])*dias_tot)-(modelos_de_automoviles[modelos_disponibles[i]]["Coste (€/día)"])*dias_tot*0.1,'€')
        precio_modelo.append(((modelos_de_automoviles[modelos_disponibles[i]]["Coste (€/día)"])*dias_tot)-(modelos_de_automoviles[modelos_disponibles[i]]["Coste (€/día)"])*dias_tot*0.1)
    elif modelos_disponibles[i] == 'Citroën C1' and dias_tot >= 5:
        print(modelos_disponibles[i], ((modelos_de_automoviles[modelos_disponibles[i]]["Coste (€/día)"])*dias_tot)-(modelos_de_automoviles[modelos_disponibles[i]]["Coste (€/día)"])*dias_tot*0.12,'€')
        precio_modelo.append(((modelos_de_automoviles[modelos_disponibles[i]]["Coste (€/día)"])*dias_tot)-(modelos_de_automoviles[modelos_disponibles[i]]["Coste (€/día)"])*dias_tot*0.12)
    elif modelos_disponibles[i] == 'VW Caddy' and dias_tot >= 3:
        print(modelos_disponibles[i], ((modelos_de_automoviles[modelos_disponibles[i]]["Coste (€/día)"])*dias_tot)-(modelos_de_automoviles[modelos_disponibles[i]]["Coste (€/día)"])*dias_tot*0.05,'€')
        precio_modelo.append(((modelos_de_automoviles[modelos_disponibles[i]]["Coste (€/día)"])*dias_tot)-(modelos_de_automoviles[modelos_disponibles[i]]["Coste (€/día)"])*dias_tot*0.05)
    elif modelos_disponibles[i] == 'Opel Zafira' and dias_tot >= 4:
        print(modelos_disponibles[i], ((modelos_de_automoviles[modelos_disponibles[i]]["Coste (€/día)"])*dias_tot)-(modelos_de_automoviles[modelos_disponibles[i]]["Coste (€/día)"])*dias_tot*0.08,'€')
        precio_modelo.append(((modelos_de_automoviles[modelos_disponibles[i]]["Coste (€/día)"])*dias_tot)-(modelos_de_automoviles[modelos_disponibles[i]]["Coste (€/día)"])*dias_tot*0.08)
    elif modelos_disponibles[i] == 'Mercedes Clase E' and dias_tot >= 7:
        print(modelos_disponibles[i], ((modelos_de_automoviles[modelos_disponibles[i]]["Coste (€/día)"])*dias_tot)-(modelos_de_automoviles[modelos_disponibles[i]]["Coste (€/día)"])*dias_tot*0.1,'€')
        precio_modelo.append(((modelos_de_automoviles[modelos_disponibles[i]]["Coste (€/día)"])*dias_tot)-(modelos_de_automoviles[modelos_disponibles[i]]["Coste (€/día)"])*dias_tot*0.1)         
    elif modelos_disponibles[i] == 'VW Polo' and dias_tot >= 5:
        print(modelos_disponibles[i], ((modelos_de_automoviles[modelos_disponibles[i]]["Coste (€/día)"])*dias_tot)-(modelos_de_automoviles[modelos_disponibles[i]]["Coste (€/día)"])*dias_tot*0.05,'€')
        precio_modelo.append(((modelos_de_automoviles[modelos_disponibles[i]]["Coste (€/día)"])*dias_tot)-(modelos_de_automoviles[modelos_disponibles[i]]["Coste (€/día)"])*dias_tot*0.05)
    else:
        print(modelos_disponibles[i], (modelos_de_automoviles[modelos_disponibles[i]]["Coste (€/día)"])*dias_tot,'€')
        precio_modelo.append((modelos_de_automoviles[modelos_disponibles[i]]["Coste (€/día)"])*dias_tot)
        
for j in range(len(precio_modelo)):
    if precio_modelo[j] == min(precio_modelo):
        print(100*'-')
        print('La opción más económica de entre las disponibles es el modelo',modelos_disponibles[j],'con un precio total transcurridos los',dias_tot,'días de',min(precio_modelo),'€')

while True:
    vehiculo_escogido = input('Escoge uno de los vehículos: ')
    if vehiculo_escogido in modelos_disponibles:
        print(100*'-')
        indice = modelos_disponibles.index(vehiculo_escogido)
        print('Modelo seleccionado:',vehiculo_escogido)
        print('Precio total:',precio_modelo[indice],'€')
        break
    else:
        print('Por favor, escoja un vehiculo de entre los disponibles.')
 
precio_total = precio_modelo[indice] 
 
print(100*'-')
print('Muchas gracias por la confianza depositada. A continuación le ofrecemos los siguientes extras:')
print('Opcion 1. Cancelación gratuita: 2€/día de alquiler. En su caso:',2*dias_tot,'€')
print('Opcion 2. Cobertura de daños por colisión básica: 15€')

if modelos_de_automoviles[vehiculo_escogido]["Categoría"] == 'B' or modelos_de_automoviles[vehiculo_escogido]["Categoría"] == 'C' or modelos_de_automoviles[vehiculo_escogido]["Categoría"] =='D':
     print('Opcion 3. Cofre de equipaje en techo: 20€')
else:
    print('La Opcion 3. Cofre de equipaje de techo no esta disponible para este vehiculo')

print('Opcion 4. Ambientador de pino en retrovisor: 30€')

extras = []
opcion = ''

while opcion!='f':
    opcion = input('Escriba el numero del extra que quieras añadir (f para salir): ')
    if opcion == '1' or opcion == '2' or (opcion == '3' and (modelos_de_automoviles[vehiculo_escogido]["Categoría"] == 'B' or modelos_de_automoviles[vehiculo_escogido]["Categoría"] == 'C' or modelos_de_automoviles[vehiculo_escogido]["Categoría"] =='D')) or opcion == '4':
        extras.append(opcion)
    elif opcion == 'f':
        break
    else:
        print('Ese numero de opcion no esta disponible.')      
            
for extra in extras:
    if extra == '1':
        precio_total = precio_total + (2*dias_tot)
    elif extra == '2':
        precio_total = precio_total + (15)
    elif extra == '3' and (modelos_de_automoviles[vehiculo_escogido]["Categoría"] == 'B' or modelos_de_automoviles[vehiculo_escogido]["Categoría"] == 'C' or modelos_de_automoviles[vehiculo_escogido]["Categoría"] =='D'):
        precio_total = precio_total + (20)
    elif extra == '4':
        precio_total = precio_total + (30)

print(100*'-')
print('El nuevo precio total tras los extras es de:',precio_total,'€')

if '3' not in extras:
    decision = input('Insistimos en que añada el ambientador. Teclee (yes) si lo desea añadir, y (no) en caso contrario: ')
    if decision == 'yes':
        precio_total = precio_total + 20

print('Finalmente el precio total más 12% IVA es de',precio_total + (precio_total*0.12),'€')
apellidos = input('Introduzaca sus apellidos: ')
nombre = input('Introduzca su nombre: ')
DNI = input('Introduzca su DNI: ')
reserva = random.randrange(99999999)  
print(100*'-')
print('Reserva confirmada número:',reserva)
print('Nombre:',nombre)
print('Apellidos:',apellidos)
print('DNI:',DNI)
print('Precio total + IVA',precio_total + (precio_total*0.12),'€')
    