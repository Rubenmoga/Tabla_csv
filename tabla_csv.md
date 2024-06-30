# Requisitos

[x] Imprimir por pantalla la tabla, con forma de tabla.
[ ] Incluir un elemento a la tabla con un comando.
[ ] Poder modificar elementos de la tabla.
[ ] Filtrar elementos de la tabla.
[ ] Colorear los elementos de la tabla.
[ ] Poder sacar un pop-up de la tabla en formato HTML CSS.
[ ] Incluir el resultado como script ejecutable con ruta marcada para los csv.



# Opciones del script

'nombre_del_scritp' 'archivo_csv' 'opcion'

### Opciones
-s --show   Opción por defecto que muestre la tabla sin más
-h --html   Opción para el renderizado de la tabla
-n --new    Opción para añadir una nueva line a la tabla csv
-d --delete _name_  Elimina la fila que se corresponde con el _name_
-m --modify _name_ _new row_ Modifica la fila que corresponde con _name_ por _new row_
