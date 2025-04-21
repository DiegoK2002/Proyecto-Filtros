#Modulos y funciones importadas

import tkinter as tk
from tkinter import ttk

from PIL import ImageTk, Image
import numpy as np

from matplotlib import pyplot as plt
import matplotlib.image as mpimg

imag = Image.open("C:/Users/diego/Desktop/Filtros/Prueba.jpg")
img = np.array(Image.open("C:/Users/diego/Desktop/Filtros/Prueba.jpg"))
        
#Crear ventana
ventana = tk.Tk()
ventana.title("Programa de filtros")
ventana.geometry("1280x720")
#Cambiar tamaño de imagen
im = imag.resize((800, 540), Image.Resampling.LANCZOS)
# #Mostrar imagen en ventana
mostrar = ImageTk.PhotoImage(im)
panel = ttk.Label(ventana, image=mostrar)
panel.place(x=400, y=100 )
    
#Filtros
#Escala de grises

def cambio():
    pic = Image.open("C:/Users/diego/Desktop/Filtros/27185.jpg")
    im = pic.resize((800, 540), Image.Resampling.LANCZOS)
    mostr = ImageTk.PhotoImage(im)
    panel.config(image=mostr)
    panel.place.config(x=400, y=100 )
    return panel

#Texto en pantalla
etiqueta_final = ttk.Label(text="Seleccione un filtro:")
etiqueta_final.place(x=20, y=40)

#Botones para aplicar filtros
boton_cobre = ttk.Button(text="Aplicar Cobre", command=cambio)
boton_cobre.place(x=20, y=80)

#Mostrar ventana
ventana.mainloop()