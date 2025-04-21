# FUNDAMENTOS DE COMPUTACIÓN Y PROGRAMACIÓN PARA INGENIERÍA
# SECCIÓN DEL CURSO: 1-G-2
# PROFESOR DE TEORÍA:  LUIS CORRAL RODRÍGUEZ
# PROFESOR DE LABORATORIO: PABLO LORCA ORLOFF
# GRUPO: 3
# INTEGRANTES:
# 1. Diego Kohle Núñez 21.008.705-2
# 2. Lucas Maza Camilla 21.042.675-2
# 3. Ignacio Pérez Henríquez 20.721.597-k
# 4. Gonzalo Ramírez Abarca 21.029.895-9
# DESCRIPCIÓN DEL PROGRAMA: Un programa simple de aplicación de filtros a 
# una imagen seleccionada por el usuario.

# <EL PROGRAMA EMPIEZA A PARTIR DE AQUÍ>

#Modulos y funciones importadas

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog 

from PIL import ImageTk, Image, ImageOps
import numpy as np

from matplotlib import pyplot as plt
import matplotlib.image as mpimg

import cv2

#Crear ventana
ventana = tk.Tk()
ventana.title("Programa de filtros")
ventana.geometry("1280x720")

#Imagen a usar
def cargar(): #Entrada
    Imagen = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Selecciona una imagen", 
                                          filetypes = (("Imagenes JPG", 
                                                        "*.jpg*"),
                                                       ("Imagenes BMP", 
                                                        "*.bmp*"),
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

def cargar_nuevo(): #Entrada
    Imagen = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Selecciona una imagen", 
                                          filetypes = (("Imagenes JPG", 
                                                        "*.jpg"),
                                                       ("Imagenes BMP", 
                                                        "*.bmp*"),
                                                        ("Todos los archivos", 
                                                        "*.*"))) 
    direct_2 = Imagen
    imag_2 = Image.open(Imagen)
    pit = imag_2.resize((800, 540), 
                        Image.Resampling.LANCZOS)
    global direct
    direct = direct_2
    pi = ImageTk.PhotoImage(pit) #Salida
    panel.config(image=pi)
    panel.place.config(x=400, y=100 )
    return imag and direct

def original(): 
    pit = Image.open(direct).resize((800, 540), 
                                    Image.Resampling.LANCZOS) #Entrada
    pi = ImageTk.PhotoImage(pit) #Salida
    panel.config(image=pi)
    panel.place.config(x=400, y=100 )
    return panel

def guardar(): #Entrada
    guardar = filedialog.asksaveasfilename(initialdir = "/",
                                        title = "Guardar como",
                                        filetypes = (("Imagenes",
                                                      "*.jpg*"),
                                                      ("todos los archivos",
                                                      "*.*")))
    guardar = guardar + '.jpg'
    imag.save(guardar) #Salida
    return


#Funciones de filtros

#Escala de grises
def gris(): 
  imagen =  np.array(Image.open(direct)) #Entrada
  filtro = []
  for i in imagen:
      for r,g,b in i:
          rojo = r*00.393
          verde = g*0.5870
          azul = b*0.1140
          numero = [int(rojo + verde + azul)]
          filtro.append(numero)
  result = np.reshape(filtro, 
                      imagen.shape[:2])
  pic = Image.fromarray(result) #Salida
  pit = pic.resize((800, 540), 
                   Image.Resampling.LANCZOS)
  global imag
  imag = pit
  pi = ImageTk.PhotoImage(pit)
  panel.config(image=pi)
  panel.place.config(x=400, y=100 )
  return panel

#Sepia
def sepia():
    matriz = np.array(Image.open(direct)) #Entrada
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
    pic = Image.fromarray(matriz) #Salida
    pit = pic.resize((800, 540), Image.Resampling.LANCZOS)
    global imag
    imag = pic
    pi = ImageTk.PhotoImage(pit)
    panel.config(image=pi)
    panel.place.config(x=400, y=100 )
    return panel       

def pixelado():
    Imagen = direct #Entrada
    arr = plt.imread(Imagen)
    filas = len(arr)
    columnas = len(arr[0])
    [[ arr[int(filas * r / 10)][int(columnas * c / 10)]  
                 for c in range(10)] for r in range(10)]
    arr_2 = Image.fromarray(arr) #Salida
    pit = arr_2.resize((128, 128), Image.BILINEAR)
    pict = pit.resize((800, 540), Image.NEAREST)
    global imag
    imag = pict
    pi = ImageTk.PhotoImage(pict)
    panel.config(image=pi)
    panel.place.config(x=400, y=100 )
    return panel

def reflejo_horizontal():
    matriz = np.array(Image.open(direct)) #Entrada
    ancho = len(matriz[0])
    alto = len(matriz)
    for y in range(alto):
        for x in range(int(ancho/2)):
            opuesto = ancho - x - 1
            indice = matriz[y] [opuesto]
            actual = matriz[y][x]
            matriz[y][opuesto] = actual 
            matriz[y][x] = indice
    pic = Image.fromarray(matriz) #Salida
    pit = pic.resize((800, 540), Image.Resampling.LANCZOS)
    global imag
    imag = pit
    pi = ImageTk.PhotoImage(pit)
    panel.config(image=pi)
    panel.place.config(x=400, y=100 )
    return panel         

def retrato(): 
        img = cv2.imread(direct)
        gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cara_cascade = cv2.CascadeClassifier(r'haarcascade_frontalcatface_extended.xml')
        # Detectar cara
        caras = cara_cascade.detectMultiScale(gris, 1.1, 4)
        # Dibujar rectangulo alrededor de la cara y recortarla
        for (x, y, w, h) in caras:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
            caras = img[y:y + h, x:x + w]
            image_salida = cv2.cvtColor(caras, cv2.COLOR_BGR2RGB)
            cara = Image.fromarray(image_salida)    
        pit = cara.resize((170, 170), Image.Resampling.LANCZOS)
        global imag
        imag = pit
        pi = ImageTk.PhotoImage(pit)
        panel.config(image=pi)
        panel.place.config(x=400, y=100 )
        return panel       


#Texto en pantalla
etiqueta_filtro = ttk.Label(text="Seleccione un filtro a aplicar:")
etiqueta_filtro.place(x=125, y=90)

etiqueta_nota = ttk.Label(text="ATENCIÓN: -Al aplicar un filtro puede \
tardarse unos momentos o incluso mostrar 'el programa no responde', \
en ese caso solo hay que esperar.")
etiqueta_nota.place(x=125, y=660)

etiqueta_nota_3 = ttk.Label(text="-El programa actualmente funciona con \
imagenes .jpg y .bmp, cualquier otro formato hará que los filtros \
no se apliquen.")
etiqueta_nota_3.place(x=190, 
                      y=677)

#Botones para aplicar filtros
boton_gris = ttk.Button(text="Escala de grises", 
                        command=gris, )
boton_gris.place(x=150, 
                 y=130, 
                 width = 105)

boton_sepia = ttk.Button(text="Sepia", 
                         command=sepia)
boton_sepia.place(x=150, 
                  y=180, 
                  width = 105)

boton_pixel = ttk.Button(text="Pixelamiento", 
                         command=pixelado)
boton_pixel.place(x=150, 
                  y=230, 
                  width = 105)

boton_reflejo = ttk.Button(text="Reflejo horizontal", 
                           command=reflejo_horizontal)
boton_reflejo.place(x=150, 
                    y=280, 
                    width = 105)

boton_reflejo = ttk.Button(text="Retrato \n (En desarrollo)", 
                           command=retrato)
boton_reflejo.place(x=150, 
                    y=330, 
                    width = 105)

#Botones control usuario
boton_cargar = ttk.Button(text="Cargar imagen", 
                          command=cargar_nuevo)
boton_cargar.place(x=400, 
                   y=30, 
                   width = 100)

boton_guardar = ttk.Button(text="Guardar imagen", 
                           command=guardar)
boton_guardar.place(x=550, 
                    y=30, 
                    width = 100)

boton_original = ttk.Button(text="Mostrar imagen original", 
                            command=original)
boton_original.place(x=1000, 
                     y=30, 
                     width = 200)

#Mostrar ventana
ventana.mainloop()