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


# Funcion para mostrar formateada el archivo csv
def mostrar_matiz():

    # Con esto se lee el archivo csv
    archivo_csv = sys.argv[1]

    # Abro el archivo csv y guardo los valores en una matriz(lista de listas)
    with open(archivo_csv, 'r', newline='', encoding='utf-8-sig') as fcsv:
        reader = csv.reader(fcsv)
        matriz = [] # Creo un lista vacia para añadirle el resot de listas   
        for row in reader:
            matriz.append(row)

    col = [0] * len(matriz[0]) #Inicializo el vector de tamaños maximos de las columnas

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





if not args.show and not args.new:
    control = 1
elif args.show and not args.new:
    control = 1
elif not args.show and args.new:
    control = 2
else:
    print('No pueden estar los dos argumentos a la vez')




match control:
    case 1:
        mostrar_matiz()
    case 2:
        print('Por implementar')
    case _:
        print('Opcion por defecto')