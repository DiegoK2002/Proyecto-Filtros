import tkinter as tk
from tkinter import ttk
from tkinter import filedialog 

from PIL import ImageTk, Image, ImageOps
import numpy as np

from matplotlib import pyplot as plt
import matplotlib.image as mpimg

def cargar(): 
    Imagen = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Selecciona una imagen", 
                                          filetypes = (("Imagenes", 
                                                        "*.jpg*"), 
                                                       ("Todos los archivos", 
                                                        "*.*"))) 
    return Imagen

ventana = tk.Tk()
ventana.title("Programa de filtros")
ventana.geometry("1280x720")
direct = ("C:/Users/diego/Desktop/Filtros/panda.jpg")
imag = Image.open(direct)
im = imag.resize((800, 540), Image.Resampling.LANCZOS)
mostrar = ImageTk.PhotoImage(im)
panel = ttk.Label(ventana, image=mostrar)
panel.place(x=400, y=100 )
#Cambiar tamaño de imagen
im = imag.resize((800, 540), Image.Resampling.LANCZOS)
# #Mostrar imagen en ventana
mostrar = ImageTk.PhotoImage(im)
panel = ttk.Label(ventana, image=mostrar)
panel.place(x=400, y=100 )


def reflejo_horizontal():
    image = Image.open(direct)
    matriz = np.array(image)
    ancho = len(matriz[0])
    alto = len(matriz)
    for y in range(alto):
        for x in range(int(ancho/2)):
            opuesto = ancho - x - 1
            indice = matriz[y] [opuesto]
            actual = matriz[y][x]
            matriz[y][opuesto] = actual 
            matriz[y][x] = indice
    pic = Image.fromarray(matriz)
    pit = pic.resize((800, 540), Image.Resampling.LANCZOS)
    global imag
    imag = pic
    plt.imshow(imag)
    pi = ImageTk.PhotoImage(pit)
    panel.config(image=pi)
    panel.place.config(x=400, y=100 )
    
    return 


def guardar():
    guardar = filedialog.asksaveasfilename(initialdir = "/",
                                        title = "Guardar como",
                                        filetypes = (("Imagenes",
                                                      "*.jpg*"),
                                                      ("todos los archivos",
                                                      "*.*")))
    global imag
    imag.save(guardar)
    return


boton_reflejo = ttk.Button(text="Reflejo horizontal", command=reflejo_horizontal)
boton_reflejo.place(x=150, y=330, width = 105)

boton_guardar = ttk.Button(text="Guardar imagen", command=guardar)
boton_guardar.place(x=550, y=30, width = 100)

ventana.mainloop()