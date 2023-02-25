import os
import json
import time
from helpers import clear

# Cargar los productos desde el archivo externo
with open("products.json", "r") as archivo:
    products = json.load(archivo)

def update_products():
    with open('products.json', 'w') as archivo_json:
    # Usamos json.dump() para escribir la lista de diccionarios en el archivo
        json.dump(products, archivo_json)
        
    # Cerramos el archivo
    archivo_json.close()



def stock_view():
    for product in products: 
        print('*********************************************')
        print(f'ID: {product["id"]} / Producto: {product["name"]} / Stock: {product["stock"]}')
        print('*********************************************')
        time.sleep(1)

def action_add():
    clear()
    stock_view()
    option_product = int(input('Seleccion ID de producto: '))
    cant_product = input('Ingrese Stock a sumar: ')
    # Recorremos la lista de diccionarios
    for product_search in products:
    # Comprobamos si el ID coincide con el que buscamos
        if product_search['id'] == option_product:
            # Modificamos los valores del diccionario
            product_search['stock'] = product_search['stock'] + int(cant_product)
            update_products()
            break
    clear()
    stock_view()

def action_subtract():
    clear()
    stock_view()
    option_product = int(input('Seleccion ID de producto: '))
    cant_product = input('Ingrese Stock a restar: ')
    # Recorremos la lista de diccionarios
    for product_search in products:
    # Comprobamos si el ID coincide con el que buscamos
        if product_search['id'] == option_product:
            # Modificamos los valores del diccionario
            product_search['stock'] = product_search['stock'] - int(cant_product)
            update_products()
            break
    clear()
    stock_view()

def action_add_product():
    clear()
    new_product = {}
    new_product['id'] = int(input('Ingrese el ID del nuevo producto: '))
    new_product['name'] = input('Ingrese el nombre del nuevo producto: ')
    new_product['stock'] = int(input('Ingrese la cantidad de stock del nuevo producto: '))
    # Agregar el nuevo producto a la lista de productos
    products.append(new_product)
    update_products()
    clear()
    stock_view()

def action_remove_product():
    clear()
    stock_view()
    option_product = int(input('Seleccion ID de producto: '))
    # Recorremos la lista de diccionarios
    for product_search in products:
        # Comprobamos si el ID coincide con el que buscamos
        if product_search['id'] == option_product:
            # Eliminamos el producto de la lista
            products.remove(product_search)
            update_products()
            break
    clear()
    stock_view()



 