import csv
import sys
import argparse


# Paso los argumentos para el script
parser = argparse.ArgumentParser(prog='tabla_csv',
                                 description='Script para el manejo de archivos csv de tamaño moderado')
parser.add_argument('archivo_csv', type=str, help='Nombre del archivo csv')
parser.add_argument('-s', '--show', action='store_true', help='Muestra el contenido de la tabla')
parser.add_argument('-n', '--new', action='store', nargs='+', help='Añade una nueva linea  al csv') #Con nargs permito pasar múltimples argumentos a la vez para poder introducir toda la fila

args = parser.parse_args()


# Con esto se lee el archivo csv
archivo_csv = args.archivo_csv

matriz = [] # Creo un lista vacia para añadirle el resot de listas  

def leer_matriz():
    # Abro el archivo csv y guardo los valores en una matriz(lista de listas)
    with open(archivo_csv, 'r', newline='', encoding='utf-8-sig') as fcsv:
        reader = csv.reader(fcsv) 
        for row in reader:
            matriz.append(row)



# Funcion para mostrar formateada el archivo csv
def mostrar_matiz():

    if len(matriz) == 0:
        print('Tabla vacia.')
        exit(1)

    col = [0] * len(matriz[0]) # Inicializo el vector de tamaños maximos de las columnas

    # Recorro la matriz por columans y saco su tamaño máximo
    for j in range(len(matriz[0])):
        va = 0 #Valor anterior de la columna
        for i in range(len(matriz)):
            col[j]=(max(va, len(matriz[i][j])))
            va = col[j]
            
    # Recorro la matriz añadiendo el tamaño máximo correspondiente
    for j in range(len(matriz[0])):
        for i in range(len(matriz)):
            matriz[i][j] = matriz[i][j].ljust(col[j])

    # Imprimo por pantalla la tabla
    print('|'+'|'.join(matriz[0])+'|')
    for i in col:
        print('+' + '-'*i, end='')
    print('+')
    for i in range(1,len(matriz)):
        print('|'+'|'.join(matriz[i])+'|')


def añadir_linea(nueva_linea):
    
    # Compruebo si termina en un retorno de carro la última línea y sino agrega uno.
    with open(archivo_csv, 'r+b') as fcsv:
        fcsv.seek(0, 2) # Mover el cursor al final del archivo
        if fcsv.tell() > 0: # Compruebo que el archivo no está vacio
            fcsv.seek(-1, 2) # Muevo el cursor al último byte
            ultimo_caracter = fcsv.read(1)
            if ultimo_caracter != b'\n':  # Si el último byte no es un retorno de carro
                fcsv.write(b'\n')  # Escribir un retorno de carro

            

    # Abro el archivo csv y guardo los valores en una matriz(lista de listas)
    with open(archivo_csv, 'a', newline='', encoding='utf-8-sig') as fcsv:
        writer = csv.writer(fcsv, delimiter=',')
        for i in nueva_linea:
            linea_separada=i.split(',')
            writer.writerow(linea_separada)
        


if not args.show and not args.new:
    leer_matriz()
    mostrar_matiz()
elif args.show and not args.new:
    leer_matriz()
    mostrar_matiz()
elif not args.show and args.new:
    leer_matriz()
    añadir_linea(args.new)
else:
    print('No pueden estar las dos flags a la vez')