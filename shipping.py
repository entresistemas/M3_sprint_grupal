
import time, os, json
from helpers import update, open_file


# Verificar si el archivo de envios existe, y crearlo si no
if not os.path.isfile("shipping.json"):
    with open("shipping.json", "w") as archivo:
        json.dump([], archivo)

envios = open_file('shipping.json')

def stock(envio):
    envio_total = 0
    for envio_bodega in envios:
        if envio_bodega["type"] == envio['type']:
            envio_total = envio_total + envio_bodega["amount"]
    return envio_total + envio['amount']
    
def sending():
    print('**************** Te lo Vendo - ENVIO ****************')
    while True:
        amount = input('Ingrese Cantidad de Productos a Enviar: ')
        if amount.isdigit() and int(amount):
            amount = int(amount)
            break  
        print("Debe ingresar Cantidad en números enteros.")
   
    
    while True:
        km = input('Ingrese Kilometraje en números enteros: ')
        if km.isdigit() and int(km):
            if int(km) > 1000:
                type = "largo"
                print("Envío Largo. chequeando Bodega_B")
                time.sleep(3)
            else :
                type = "rapido"
                print("Envío Rápido. chequeando Bodega A")
                time.sleep(3)

            break
        print("Debe ingresar Kilometraje en números enteros.")
    envio = {"kilometres": km, "type": type, "amount": amount  }    
    print('**********************************************')
    if envio["type"] == "rapido" and stock(envio) <= 500 :
        print("Envío Exitoso, enviando a Bodega A") 
        envios.append(envio)
        update(envios, 'shipping.json')
    elif envio["type"] == "largo" and stock(envio) <= 500 :
        print("Envío Exitoso, enviando a Bodega B") 
        envios.append(envio)
        update(envios, 'shipping.json')
    else:
        print("Envío rechazado por sobre Stock de Bodega")
    print('**********************************************')
         

