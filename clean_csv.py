import pandas as pd
import csv

# Lo que vamos a hacer es acomodar las columnas para que cada línea contenga el mismo número de columnas en este caso el alrchivo se encuentra bastante #dañado así que renombraremos las columnas de una manera manual 
rows = []
csv_header = ['id', 'item', 'time', 'rating', 'review']
frame_header = ['user', 'item', 'rating', 'review']

# Con DictReader nosotros vamos a poder acceder a la cabecera, lo que se hará es recorrer nuestros campos, si hay un dato que falta
#Insertaremos un dato de la cabecera para que así cada línea contenga el mismo número de columnas y se pueda leer el archivo
with open('starts_data.csv', 'r') as f_input:
    for row in csv.DictReader(f_input, delimiter=' ', fieldnames=csv_header[:-1], restkey=csv_header[-1], skipinitialspace=True):
        try:
            rows.append([row['user'], row['item'], row['rating'], ' '.join(row['review'])])
        except KeyError as e:
            rows.append([row['user'], row['item'], row['rating'], ' '])
frame = pd.DataFrame(rows, columns=frame_header)
print (frame)


#Nuestro data Frame lo vamos a convertir en un CSV para que pueda ser leido con un encoding de utf-8
frame.to_csv('outpout.csv', encoding='utf-8') 

# Crearemos el archivo psv con las comillas faltantes
#Para el delimitador utilizamos funciones que contiene la librería de csv
with open('starts_data.csv', 'r') as infile, open('output.psv', 'w') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile, delimiter='|')
    writer.writerows(reader)
