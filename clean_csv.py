import pandas as pd
import csv

#Para el delimitador utilizamos funciones que contiene la librería de csv
with open('starts_data.csv', 'r') as infile, open('output.psv', 'w') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile, delimiter='|')
    writer.writerows(reader)
    
#Es necesario convertirlo en un data frame nunevo para poder leerlo
rows = []
csv_header = ['user', 'item', 'time', 'rating', 'review']
frame_header = ['user', 'item', 'rating', 'review']


# Conversión
with open('starts_data.csv', 'r') as f_input:
    for row in csv.DictReader(f_input, delimiter=' ', fieldnames=csv_header[:-1], restkey=csv_header[-1], skipinitialspace=True):
        try:
            rows.append([row['user'], row['item'], row['rating'], ' '.join(row['review'])])
        except KeyError as e:
            rows.append([row['user'], row['item'], row['rating'], ' '])
frame = pd.DataFrame(rows, columns=frame_header)
print (frame)

#Convertimos nuestro DataFrame en un CSV

frame.to_csv('outpout.csv', encoding='utf-8')
