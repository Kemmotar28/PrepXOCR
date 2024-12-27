import cv2
import easyocr
import os
import os.path
from os import path
import sys

# Determinaciòn de la ruta de trabajo (por parámetro o defecto)
cv2.__version__
# rutaActual=os.getcwd()
rutaActual="/home/seretur/Documentos/UNSa/reglamentos/"
if len(sys.argv)>1:
    rutaVer=sys.argv[1]
    if path.exists(rutaVer):
        rutaActual=rutaVer
    print(rutaVer)
os.chdir(rutaActual)

# pngs es la lista de nombres de archivos de imagen en el directorio
pngs=[]

#Obtener la lista de archivos jpg en el directorio
entradas=os.scandir(rutaActual)
for entrada in entradas:
    nombre=entrada.name
    if (nombre.endswith("png") or nombre.endswith(".PNG")):
                pngs.append(entrada.name)

print("Imágenes encontradas: ",len(pngs))
print("Primera: ",pngs[0])

reader=easyocr.Reader(["es"], gpu=False)

cadena=""
pg=1

for hoja in pngs:
    resultado=reader.readtext(hoja,paragraph=True)
    print("revisada página",pg)
    pg=pg+1


nombretexto=rutaActual+'.txt'

print("Por grabar en ",nombretexto, "una cadena de ",len(cadena))

archivo=open(nombretexto,"w")
for res in resultado:
    print("texto entendido: ", res[1])
    archivo.write(res[1])
    archivo.write("\n")


archivo.close()