#Desarrollado por Felipe Prieto
import pandas as pd
import csv

# Lo que vamos a hacer es acomodar las columnas para que cada línea contenga el mismo número de columnas en este caso el alrchivo se encuentra dañado
# Por lo que se asume algunas cabeceras, para probar el archivo
rows = []
csv_header = ['id', 'hip', 'hr', 'gl', 'lum','var','var_min','var_max']
frame_header = ['id', 'hip', 'hr', 'gl', 'lum','var','var_min','var_max']

# Con DictReader nosotros vamos a poder acceder a la cabecera, lo que se hará es recorrer nuestros campos, si hay un dato que falta
#Insertaremos un dato de la cabecera para que así cada línea contenga el mismo número de columnas y se pueda leer el archivo para este caso 
#Para este ejercicio utilizaremos 7 columnas para recuperar los datos que podamos, adicionalmente se deben agregar todas.
with open('starts_data_updated.csv', 'r') as f_input:
    for row in csv.DictReader(f_input, delimiter='|', fieldnames=csv_header[:-1], restkey=csv_header[-1], quotechar='"', doublequote=True, skipinitialspace=True):
        try:
            rows.append([row['id'], row['hip'], row['hr'], row['gl'], row['lum'], row['var'],row['var_min'], ' '.join(row['var_max'])])
        except KeyError as e:
            rows.append([row['id'], row['hip'], row['hr'], row['gl'],row['lum'],row['var'], row['var_min'], ' '])
frame = pd.DataFrame(rows, columns=frame_header)
print (frame)
#Convertimos nuestro DataFrame en CSV
frame.to_csv('starts_data_encoding.csv', encoding='utf-8',quotechar='"',doublequote=True, sep = '|')

df = pd.read_csv ('starts_data_encoding.csv')

#Nos aseguramos que podemos leer nuestro archivo
with open('starts_data_encoding.csv', 'rt') as f:
    # same as csv_reader = csv.reader(f, skipinitialspace=True)
    csv_reader = csv.reader(f, skipinitialspace=True,quotechar='"',doublequote=True)
    
    for line in csv_reader:
        print(line)

    
#Para el delimitador utilizamos funciones que contiene la librería de csv
with open('starts_data_encoding.csv', 'r') as infile, open('starts_data_with_quote.psv', 'w',encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile,quoting=csv.QUOTE_ALL,escapechar='|',delimiter ="|")
    writer.writerows(reader)
    
    
 #Para el delimitador utilizamos funciones que contiene la librería de csv y este archivo lo haremos en csv
with open('starts_data_encoding.csv', 'r') as infile, open('starts_data_with_quote.csv', 'w',encoding='utf-8') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile,quoting=csv.QUOTE_ALL,escapechar='|',delimiter ="|")
    writer.writerows(reader)
    
    
    
 #Verificamos que se pueda leer el archivo   
df2 = pd.read_csv ('starts_data_with_quote.csv')
