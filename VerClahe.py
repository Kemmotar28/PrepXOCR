#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 09:50:07 2024

@author: seretur
"""

import cv2
# import imutils
import numpy as np
# from tkinter import *
from tkinter import filedialog

def elegir_ruta():
    ruta_archivo = filedialog.askopenfilename(
        title="Seleccionar imagen JPG",
        filetypes=[("Archivos JPG", "*.jpg")])
    if ruta_archivo:
        return ruta_archivo
    else:
        return "none"

ruta=elegir_ruta()

imagen=cv2.imread(ruta,cv2.IMREAD_GRAYSCALE)
# imagen=abrir_imagen()
clahe=cv2.createCLAHE(clipLimit=5)

imagen2=clahe.apply(imagen)
pospunto=ruta.find('.')
nombre=ruta[:pospunto]+'2.png'

res=np.hstack((imagen,imagen2))
cv2.imwrite(nombre,res)

