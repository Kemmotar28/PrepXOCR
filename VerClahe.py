#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 09:50:07 2024

@author: seretur
"""

import cv2
# import imutils
import numpy as np
from tkinter import *
from tkinter import filedialog


def elegir_ruta():
    raiz=Tk()
    raiz.withdraw
    global ruta;
    ruta_archivo = filedialog.askopenfilename(
        title="Seleccionar imagen JPG",
        filetypes=[("Archivos JPG", "*.jpg")])
    ruta=ruta_archivo
    raiz.destroy()


ruta=None
elegir_ruta()

# cargar la imagen a tratar
imagen=cv2.imread(ruta,cv2.IMREAD_GRAYSCALE)

# Aplicar CLAHE, queda en imagen2
clahe=cv2.createCLAHE(clipLimit=5)
imagen2=clahe.apply(imagen)

# máscara de desenfoque sobre imagen2, queda en sharpened

kernel = np.array([[0, -1, 0],[-1, 5, -1],[0, -1, 0]])
sharpened = cv2.filter2D(imagen2, -1, kernel)

# definir el nombre de archivo
pospunto=ruta.find('.')
nombre=ruta[:pospunto]+'2.png'

# Juntar la imagen original y la última y guardarlas
res=np.hstack((imagen,sharpened))
cv2.imwrite(nombre,res)
cv2.waitKey()
cv2.destroyAllWindows()

