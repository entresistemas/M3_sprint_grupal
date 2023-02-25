import os
import random
import json
import sys
import time
from store import action_add, action_subtract, stock_view, action_add_product, action_remove_product
from clients import add_client, eliminar_cliente, client_view
from shipping import sending
from helpers import clear

def stock_random():
    return random.randint(300,500)

if not os.path.exists('./products.json'):
    products = [
        {
            'id':1,
            'name': 'Vasos',
            'stock': stock_random()
        },
        {
            'id':2,
            'name': 'Cucharas',
            'stock': stock_random()
        },
        {
            'id':3,
            'name': 'Cuchillos',
            'stock': stock_random()
        },
        {
            'id':4,
            'name': 'Tenedores',
            'stock': stock_random()
        },
    ]
    with open('products.json', 'w') as archivo_json:
    # Usamos json.dump() para escribir la lista de diccionarios en el archivo
        json.dump(products, archivo_json)
        
    # Cerramos el archivo
    archivo_json.close()


def menu_main():
    print('**************** Te lo Vendo ****************')
    print('1. Bodega')
    print('2. Clientes')
    print('3. Envio')
    print('0. Salir')
    print('*********************************************')
    return  input('Selecciona una opción: ')

def menu_main_parent():
    option = menu_main()
    if option == "1":
        clear()
        store_menu_parent()
    elif option == "2":
        clear()
        client_menu_parent()
    elif option == "3":
        clear()
        sending()
        menu_main_parent()
    elif option == "0":
        sys.exit()
    else:
        print('Opción inválida !!')

def stock_menu():
    print('**************** Te lo Vendo - BODEGA - STOCK ****************')
    print('1. Sumar unidades')
    print('2. Restar unidades')
    print('0. Salir')
    print('*********************************************')
    return input('Selecciona una opción: ')

def stock_menu_parent():
    option_stock = stock_menu()
    if option_stock == "1":
        action_add()
        stock_menu_parent()
    elif option_stock == "2":
        action_subtract()
        stock_menu_parent()
    elif option_stock == "0":
        clear()
        store_menu_parent()
    else:
        print('Opción inválida !!')
        time.sleep(2)
        clear()

def store_menu():
    print('**************** Te lo Vendo - BODEGA ****************')
    print('1. Stock producto')
    print('2. Nuevo producto')
    print('3. Eliminar producto')
    print('4. Visualizar productos')
    print('0. Salir')
    print('*********************************************')
    return input('Selecciona una opción: ')

def store_menu_parent():  
    option = store_menu() 
    if option == "1":
        clear()
        stock_menu_parent()
    elif option == "2":
        clear()
        action_add_product()
        store_menu_parent()
    elif option == "3":
        clear()
        action_remove_product()
        store_menu_parent()
    elif option == "4":
        stock_view()
        time.sleep(3)
        clear()
        store_menu_parent()
    elif option == "0":
        clear()
        menu_main_parent()
    else:
        print('Opción inválida !!')
        time.sleep(2)
        clear()

def client_menu():
    print('**************** Te lo Vendo - CLIENTES ****************')
    print('1. Agregar Cliente')
    print('2. Eliminar Cliente')
    print('3. Visualizar Cliente')
    print('0. Salir')
    print('*********************************************')
    return input('Selecciona una opción: ')

def client_menu_parent():  
    option = client_menu() 
    if option == "1":
        clear()
        add_client()
        client_menu_parent()
    elif option == "2":
        clear()
        eliminar_cliente()
        client_menu_parent()
    elif option == "3":
        clear()
        client_view()
        time.sleep(3)
        clear()
        client_menu_parent()
    elif option == "0":
        menu_main_parent()
    else:
        print('Opción inválida !!')
        time.sleep(2)
        clear() 

clear()
# Menú principal
menu_main_parent()
