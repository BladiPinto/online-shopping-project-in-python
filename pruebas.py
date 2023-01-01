import csv
import pandas as pd
from csv import writer
'''
new = []
print("\n")
dressId = input("Ingresa el ID del Producto : ")
res=int(input("\nCuantas unidades desea eliminar ? :"))
with open('shopping.csv') as File:
    reader = csv.DictReader(File)
    for d in reader:
        if d["id"] == dressId:
            new.append(d["id"])
            new.append(d["nombre"])
            new.append(int(d["disponible"])-res)
            new.append(d["costo"])
            new.append(d["precio"])

with open ('outputfile.csv' , 'a' , newline ='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(new)
            f_object.close()
'''


df_s =  pd.read_csv('outputfile.csv')

b=df_s.drop_duplicates(df_s.columns[~df_s.columns.isin(['nombre','disponible','precio','costo'])],keep='last')
print(df_s)
print(b)

b.to_csv('shopping.csv',index=False)