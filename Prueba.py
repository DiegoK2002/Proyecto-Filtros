
#Modulos y funciones importadas

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog 

from PIL import ImageTk, Image, ImageOps
import numpy as np

from matplotlib import pyplot as plt
import matplotlib.image as mpimg

#Crear ventana
ventana = tk.Tk()
ventana.title("Programa de filtros")
ventana.geometry("1280x720")

#Imagen a usar
def cargar(): 
    Imagen = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Selecciona una imagen", 
                                          filetypes = (("Imagenes", 
                                                        "*.jpg*"), 
                                                       ("Todos los archivos", 
                                                        "*.*"))) 
    return Imagen

direct = cargar()
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

#Funciones de control

def cargar_nuevo(): 
    Imagen = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Selecciona una imagen", 
                                          filetypes = (("Imagenes", 
                                                        "*.jpg*"), 
                                                        ("Todos los archivos", 
                                                        "*.*"))) 
    direct = Imagen
    imag = Image.open(Imagen)
    pit = imag.resize((800, 540), Image.Resampling.LANCZOS)
    pi = ImageTk.PhotoImage(pit)
    panel.config(image=pi)
    panel.place.config(x=400, y=100 )
    return imag and direct

def original():
    pit = imag.resize((800, 540), Image.Resampling.LANCZOS)
    pi = ImageTk.PhotoImage(pit)
    panel.config(image=pi)
    panel.place.config(x=400, y=100 )
    return panel

def guardar():
        guardar = filedialog.asksaveasfilename(initialdir = "/",
                                               title = "Guardar como",
                                               filetypes = (("Imagenes",
                                                             "*.jpg*"),
                                                             ("todos los archivos",
                                                              "*.*")), 
                                               defaultextension = ("Imagenes",
                                                             "*.jpg*"))
        imag.save(guardar)
        return     


 
#Funciones de filtros

#Escala de grises
def gris():
  imagen =  np.array(imag) 
  filtro = []
  for i in imagen:
      for r,g,b in i:
          rojo = r*00.393
          verde = g*0.5870
          azul = b*0.1140
          numero = [int(rojo + verde + azul)]
          filtro.append(numero)
  result = np.reshape(filtro, imagen.shape[:2])
  pic = Image.fromarray(result)
  pit = pic.resize((800, 540), Image.Resampling.LANCZOS)
  pi = ImageTk.PhotoImage(pit)
  panel.config(image=pi)
  panel.place.config(x=400, y=100 )
  return panel

#Sepia
def sepia():
    matriz = np.array(imag)
    ancho = len(matriz[0])
    alto = len(matriz)
    for y in range(alto):
        for x in range(ancho):
            pixel = matriz[y][x]
            original_rojo = pixel[0]
            original_verde = pixel[1]
            original_azul = pixel[2]
            sepia_rojo = round(0.393*original_rojo +
                               0.769*original_verde+0.189*original_azul)
            sepia_verde = round(0.349*original_rojo +
                                0.686*original_verde+0.168*original_azul)
            sepia_azul = round(0.272*original_rojo +
                               0.534*original_verde+0.131*original_azul)
            pixel_sepia = [sepia_rojo, sepia_verde, sepia_azul]
            for indice in range(len(pixel_sepia)):
                if pixel_sepia[indice] < 0:
                    pixel_sepia[indice] = 0
                elif pixel_sepia[indice] > 255:
                    pixel_sepia[indice] = 255
            matriz[y][x] = pixel_sepia
    pic = Image.fromarray(matriz)
    pit = pic.resize((800, 540), Image.Resampling.LANCZOS)
    pi = ImageTk.PhotoImage(pit)
    panel.config(image=pi)
    panel.place.config(x=400, y=100 )
    return panel       

def pixelado():
    Imagen = direct
    arr = plt.imread(Imagen)
    filas = len(arr)
    columnas = len(arr[0])
    [[ arr[int(filas * r / 10)][int(columnas * c / 10)]  
                 for c in range(10)] for r in range(10)]
    arr_2 = Image.fromarray(arr)
    pit = arr_2.resize((128, 128), Image.BILINEAR)
    pict = pit.resize((800, 540), Image.NEAREST)
    pi = ImageTk.PhotoImage(pict)
    panel.config(image=pi)
    panel.place.config(x=400, y=100 )
    return panel



with Image.open(direct) as im:
    old_size = im.size
    new_size = (800, 800)

if new_size > old_size:
    if old_size[0] % 2 == 0:
        add_left = add_right = (new_size[0] - old_size[0]) // 2
    else:
        add_left = (new_size[0] - old_size[0]) // 2
        add_right = ((new_size[0] - old_size[0]) // 2) + 1

    if old_size[1] % 2 == 0:
        add_top = add_bottom = (new_size[1] - old_size[1]) // 2
    else:
        add_top = (new_size[1] - old_size[1]) // 2
        add_bottom = ((new_size[1] - old_size[1]) // 2) + 1
left = 0 - add_left
top = 0 - add_top
right = old_size[0] + add_right
bottom = old_size[1] + add_bottom
im = im.crop((left, top, right, bottom))
np.imshow(im)
pi = ImageTk.PhotoImage(im)
panel.config(image=pi)
panel.place.config(x=400, y=100 )
l

def reflejo_horizontal():
    matriz = np.array(imag)
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
    pi = ImageTk.PhotoImage(pit)
    panel.config(image=pi)
    panel.place.config(x=400, y=100 )
    return panel     

    

#Texto en pantalla
etiqueta_filtro = ttk.Label(text="Seleccione un filtro a aplicar:")
etiqueta_filtro.place(x=125, y=90)

etiqueta_proximo = ttk.Label(text="(No funcional aún)")
etiqueta_proximo.place(x=398, y=10)

etiqueta_proximo_2 = ttk.Label(text="(No funcional aún)")
etiqueta_proximo_2.place(x=548, y=10)

etiqueta_nota = ttk.Label(text="ATENCIÓN: -Al aplicar un filtro puede tardarse unos momentos o incluso mostrar 'el programa no responde', en ese caso solo hay que esperar.")
etiqueta_nota.place(x=125, y=660)

etiqueta_nota_3 = ttk.Label(text="-El programa actualmente SOLO funciona con imagenes .jpg, cualquier otro formato hará que los filtros no se apliquen.")
etiqueta_nota_3.place(x=190, y=677)

#Botones para aplicar filtros
boton_gris = ttk.Button(text="Escala de grises", command=gris, )
boton_gris.place(x=150, y=130, width = 105)

boton_sepia = ttk.Button(text="Sepia", command=sepia)
boton_sepia.place(x=150, y=180, width = 105)

boton_pixel = ttk.Button(text="Pixelamiento", command=pixelado)
boton_pixel.place(x=150, y=230, width = 105)

boton_cuadrado = ttk.Button(text="Borde cuadrado", command=borde_cuadrado)
boton_cuadrado.place(x=150, y=280, width = 105)

boton_reflejo = ttk.Button(text="Reflejo horizontal", command=reflejo_horizontal)
boton_reflejo.place(x=150, y=330, width = 105)

#Botones control usuario
boton_cargar = ttk.Button(text="Cargar imagen", command=cargar_nuevo)
boton_cargar.place(x=400, y=30, width = 100)

boton_guardar = ttk.Button(text="Guardar imagen", command=guardar)
boton_guardar.place(x=550, y=30, width = 100)

boton_original = ttk.Button(text="Mostrar imagen original", command=original)
boton_original.place(x=1000, y=30, width = 200)

#Mostrar ventana
ventana.mainloop()