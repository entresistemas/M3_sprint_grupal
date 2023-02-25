import json
import time
from helpers import clear

# Cargar los datos de clientes desde el archivo
with open("clientes.json", "r") as archivo:
    datos_clientes = json.load(archivo)


def update_clients():
    with open('clientes.json', 'w') as archivo_json:
        # Usamos json.dump() para escribir la lista de diccionarios en el archivo
        json.dump(datos_clientes, archivo_json)

    # Cerramos el archivo
    archivo_json.close()

def client_view():
    for client in datos_clientes: 
        print('*********************************************')
        print(f'ID: {client["id"]} / Nombre: {client["nombre"]} / Apellido: {client["apellido"]} / Edad: {client["edad"]} / Contraseña: {client["clave"]}')
        print('*********************************************')
        time.sleep(1)

def agregar_cliente():
    name = input('Ingrese Nombre: ')
    last_name = input('Ingrese Apellido: ')
    age = input('Ingrese Edad: ')
    password = input('Ingrese Contraseña: ')
    new_client = {'id':len(datos_clientes)+1, 'nombre': name, 'apellido': last_name,
                  'edad': age, 'clave': password}
    datos_clientes.append(new_client)

    update_clients()
    clear()
    client_view()

# Función para eliminar un cliente según su ID
def eliminar_cliente():
    client_view()
    id = input('Ingrese ID a eliminar: ')
    for i, cliente in enumerate(datos_clientes):
        if cliente["id"] == int(id):
            print('INGRESO A BORRAR')
            del datos_clientes[i]
            update_clients()
            break
    clear()
    client_view()
