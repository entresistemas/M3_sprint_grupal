import json
import os
from helpers import clear


# Verificar si el archivo de envios existe, y crearlo si no
if not os.path.isfile("envios.json"):
    with open("envios.json", "w") as archivo:
        json.dump([], archivo)


with open('envios.json', 'r') as archivo:
        # Usamos json.dump() para escribir la lista de diccionarios en el archivo
         envios = json.load(archivo)

def update_envios():
    with open('envios.json', 'w') as archivo_json:
        # Usamos json.dump() para escribir la lista de diccionarios en el archivo
        json.dump(envios, archivo_json)

def stock(envio):
    envio_total = 0
    for envio_bodega in envios:
        if envio_bodega["tipo"] == envio['tipo']:
            envio_total = envio_total + envio_bodega["cantidad"]
    return envio_total + envio['cantidad']
    
def envio():

    while True:
        cantidad = input('Ingrese Cantidad de Productos a Enviar: ')
        if cantidad.isdigit() and int(cantidad):
            cantidad = int(cantidad)
            break  
        print("Debe ingresar Cantidad en números enteros.")
   
    
    while True:
        km = input('Ingrese Kilometraje en números enteros: ')
        if km.isdigit() and int(km):
            if int(km) > 1000:
                tipo = "largo"
                print("Envío Largo. chequeando Bodega_B")
            else :
                tipo = "rapido"
                print("Envío Rápido. chequeando Bodega A")

            break
        print("Debe ingresar Kilometraje en números enteros.")
    envio = {"kilometros": km, "tipo": tipo, "cantidad": cantidad  }    

    if envio["tipo"] == "rapido" and stock(envio) <= 500 :
        print("Envío Exitoso, enviando a Bodega A") 
        envios.append(envio)
        update_envios()
    elif envio["tipo"] == "largo" and stock(envio) <= 500 :
        print("Envío Exitoso, enviando a Bodega B") 
        envios.append(envio)
        update_envios()
    else:
        print("Envío rechazado por sobre Stock de Bodega")
         
    print(envio)

envio()