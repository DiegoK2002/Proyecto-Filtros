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

###################################MÓDULOS Y FUNCIONES IMPORTADAS###################################

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog 

from PIL import ImageTk, Image
import numpy as np

from matplotlib import pyplot as plt

import cv2

import os

###################################CREAR VENTANA###################################################

# Se selecciona el titulo de la ventana y sus dimensiones 
ventana = tk.Tk()
ventana.title("Programa de filtros")
ventana.geometry("1280x720")

# Se le indica al usuario que el programa está cargando y así hacerle saber que el programa
# no está congelado o no haciendo nada
etiqueta_carga = ttk.Label(text="Cargando filtros...")
etiqueta_carga.place(x = 440, y = 350)
etiqueta_carga.config(font = ('',20))

###################################IMAGEN A USAR###################################################

# Esta función se ejecuta al iniciar el programa, con ella, el usuario puede seleccionar una
# imagen de su galeria y cargarla al programa.

# Entrada: Imagen
# Salida: Directorio

def cargar(): 
    Imagen = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Selecciona una imagen", 
                                          filetypes = (("Imagenes JPG", 
                                                        "*.jpg*"),
                                                       ("Imagenes BMP", 
                                                        "*.bmp*"),
                                                       ("Imagenes JPEG", 
                                                        "*.jpeg*"),
                                                       ("Todos los archivos", 
                                                        "*.*"))) 
    return Imagen

# direct será el directorio de la imagen
direct = cargar()
# imag será la imagen abierta desde el directorio
imag = Image.open(direct)
# Cambiar tamaño de imagen
im = imag.resize((800, 540), Image.Resampling.LANCZOS)

###################################MOSTRAR IMAGEN EN VENTANA######################################

# En este proceso la imagen se muestra en la ventana de 1280x720 antes creada
# esta se mostrará en las posiciones x=400, y=100
mostrar = ImageTk.PhotoImage(im)
panel = ttk.Label(ventana, image=mostrar)
panel.place(x=400, y=100 )

###################################FUNCIONES DE CONTROL###########################################

# Esta función permitirá al usuario ingresar una nueva imagen si esta se quiere cambiar.
# Obtiene la nueva dirección de la imagen y reemplaza la anterior con la función global.

# Entrada: Imagen
# Salida: Directorio

def cargar_nuevo(): 
    Imagen = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Selecciona una imagen", 
                                          filetypes = (("Imagenes JPG", 
                                                        "*.jpg"),
                                                       ("Imagenes BMP", 
                                                        "*.bmp*"),
                                                       ("Imagenes JPEG", 
                                                        "*.jpeg*"),
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

# Con esta funcion la imagen se mostrará sin ningún tipo de edición.
# En el caso de que a la imagen se le haya aplicado un filtro y se haya guardado, 
# esta se mostrará con el filtro.
# Ya que esa sería la imagen "original" de ese archivo.

# Entrada = Directorio
# Salida = Imagen

def original(): 
    pit = Image.open(direct).resize((800, 540), 
                                    Image.Resampling.LANCZOS) #Entrada
    pi = ImageTk.PhotoImage(pit) #Salida
    panel.config(image=pi)
    panel.place.config(x=400, y=100 )
    return panel

# Esta función permitirá al usuario guardar la imagen que se está mostrando en pantalla
# Le pedirá al usuario un directorio donde guardar la imagen y a este le agregará '.jpg'

# Entrada = Directorio
# Salida = Imagen modificada

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



# Función para buscar en el equipo el archivo que trae por defecto opencv
# para detectar la cara de los gatos. 
# Si no se encuentra dicho archivo, el filtro de retrato tirará error.
# El archivo dog_face.xml debe descargarse desde el siguiente link:
# https://github.com/metinozkan/DogAndCat-Face-Opencv

# Entrada = El nombre del archivo.
# Salida = La ruta del archivo.

def findfile(name, path):
    for dirpath, dirname, filename in os.walk(path):
        if name in filename:
            return os.path.join(dirpath, name)

gato = findfile(r"haarcascade_frontalcatface_extended.xml", "/")   
perro = findfile(r"dog_face.xml", "/")


# Hace que el mensaje 'cargando' desaparezca
etiqueta_carga.place_forget()

###################################FUNCIONES DE FILTROS##########################################

# Escala de grises
# Efecto que le da a la imagen solo tonalidades de distintos grises.

# Entrada: Directorio
# Salida: Imagen con filtro aplicado

def gris(): 
  imagen =  np.array(Image.open(direct))
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
  pic = Image.fromarray(result)
  pit = pic.resize((800, 540), 
                   Image.Resampling.LANCZOS)
  global imag
  imag = pit
  pi = ImageTk.PhotoImage(pit)
  panel.config(image=pi)
  panel.place.config(x=400, y=100 )
  return panel

# Sepia
# Efecto que le da a la imagen un tono amarillezco.

# Entrada: Directorio
# Salida: Imagen con filtro aplicado

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

# Pixelado
# Bajará la resolución de la imagen haciendo que los pixeles de esta sean más visibles.

# Entrada: Directorio
# Salida: Imagen con filtro aplicado

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

# Reflejo horizontal
# “Copiará” toda la parte izquierda de la imagen (comenzando desde el centro) y 
# la “pegará” a la derecha de esta, para luego hacer un reflejado de la parte “copiada” 
# como si fuera un espejo.

# Entrada: Directorio
# Salida: Imagen con filtro aplicado

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

# Retrato gato  
# Este filtro generaría una pequeña imagen con solo la cara del animal en la fotografía.

# Entrada: Directorio
# Salida: Imagen con filtro aplicado  

def retrato_gato(): 
        img = cv2.imread(direct)
        # Pasa la imagen a gris
        gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Se determina el archivo para detectar el rostro
        gato_cascade = cv2.CascadeClassifier(gato)
        # Detectar cara
        caras = gato_cascade.detectMultiScale(gris, 1.1, 4)
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

# Retrato perro
# Este filtro generaría una pequeña imagen con solo la cara del animal en la fotografía.

# Entrada: Directorio
# Salida: Imagen con filtro aplicado

def retrato_perro(): 
        img = cv2.imread(direct)
        # Pasa la imagen a gris
        gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Se determina el archivo para detectar el rostro
        gato_cascade = cv2.CascadeClassifier(perro)
        # Detectar cara
        caras = gato_cascade.detectMultiScale(gris, 1.1, 4)
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
    
# Esta función elimina el botón de retrato y muestra 2 botones en pantalla
# Uno como botón que ejecutará la función de retrato con el archivo de
# reconocimiento de gatos y otro botón que ejecutará la función de retrato 
# con el archivo de perros

# Entrada: ''
# Salida: 2 botones en pantalla
    
def retrato():
    boton_retrato.place_forget()
    
    boton_retrato_gato = ttk.Button(text="Retrato gato", 
                               command=retrato_gato)
    boton_retrato_gato.place(x=230, 
                        y=280, 
                        width = 110)

    boton_retrato_perro = ttk.Button(text="Retrato perro", 
                               command=retrato_perro)
    boton_retrato_perro.place(x=70, 
                        y=280, 
                        width = 110)
    return

# Borde cuadrado
# Genera un tipo de “margen” dentro de la imagen de un color sólido, en este caso
# con forma cuadrada al rededor de la imagen

# Entrada: Directorio
# Salida: Imagen con filtro aplicado
    
def borde_cuadrado():
    im = cv2.imread(direct)
    fila, columna = im.shape[:2]
    fondo = im[fila-2:fila, 0:columna]
    medio = cv2.mean(fondo)[0]
    bordetamaño = 20
    borde = cv2.copyMakeBorder(
        im,
        top=bordetamaño,
        bottom=bordetamaño,
        left=bordetamaño,
        right=bordetamaño,
        borderType=cv2.BORDER_CONSTANT,
        value=[medio, medio, medio])
    image_salida = cv2.cvtColor(borde, cv2.COLOR_BGR2RGB)
    pic = Image.fromarray(image_salida)    
    pit = pic.resize((800, 540), Image.Resampling.LANCZOS)
    global imag
    imag = pit
    pi = ImageTk.PhotoImage(pit)
    panel.config(image=pi)
    panel.place.config(x=400, y=100 )
    return panel   
    
# Esta función elimina el botón de bordes y muestra 3 botones en pantalla
# Los 3 botones serán para una forma diferente de borde.
# Uno será cuadrado, otro circular y otro en forma de rómbo

# Entrada: ''
# Salida: 3 botones en pantalla

def borde():
     boton_borde.place_forget()
     boton_borde_circular = ttk.Button(text="Borde circular", 
                                state=tk.DISABLED)
     boton_borde_circular.place(x=30, 
                         y=330, 
                         width = 110)
     boton_borde_cuadrado = ttk.Button(text="Borde cuadrado", 
                                command=borde_cuadrado)
     boton_borde_cuadrado.place(x=150, 
                         y=330, 
                         width = 110)
     boton_borde_rombico = ttk.Button(text="Borde rómbico", 
                                state=tk.DISABLED)
     boton_borde_rombico.place(x=270, 
                         y=330, 
                         width = 110)
     
# Profundidad de campo para gatos
# Hace que la imagen desenfoque lo que está más lejos para así dar la 
# impresión de que la imagen no es plana.
# En este caso detectará el rostro de un gato usando el archivo 'gato'

# Entrada: Directorio
# Salida: Imagen con filtro aplicado     
     
def profundidad_gato():
    def borr_img(img, factor = 45):
       ancho = int(img.shape[1] / factor)
       alto = int(img.shape[0] / factor)
       if ancho % 2 == 0: ancho = ancho - 1
       if alto % 2 == 0: alto = alto - 1
       img_borrosa = cv2.GaussianBlur(img, (ancho, alto), 0)
       return img_borrosa

    img = cv2.imread(direct)
    img_borrosa = borr_img(img, factor = 45)
     
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detector_cara = cv2.CascadeClassifier(gato)
    caras = detector_cara.detectMultiScale(gris, 1.1, 4)
     
    for x, y, w, h in caras:
       cara_detectada = img[int(y):int(y+h), int(x):int(x+w)]
       img_borrosa[y:y+h, x:x+w] = cara_detectada
         
    
    image_salida = cv2.cvtColor(img_borrosa, cv2.COLOR_BGR2RGB)
    cara = Image.fromarray(image_salida)    
    pit = cara.resize((800, 540), Image.Resampling.LANCZOS)
    global imag
    imag = pit
    pi = ImageTk.PhotoImage(pit)
    panel.config(image=pi)
    panel.place.config(x=400, y=100 )
    return panel  
     
# Profundidad de campo para perros
# Hace que la imagen desenfoque lo que está más lejos para así dar la 
# impresión de que la imagen no es plana.
# En este caso detectará el rostro de un gato usando el archivo 'perro'

# Entrada: Directorio
# Salida: Imagen con filtro aplicado 

def profundidad_perro():
    def borr_img(img, factor = 45):
       ancho = int(img.shape[1] / factor)
       alto = int(img.shape[0] / factor)
       if ancho % 2 == 0: 
           ancho = ancho - 1
       if alto % 2 == 0: 
           alto = alto - 1
       img_borrosa = cv2.GaussianBlur(img, (ancho, alto), 0)
       return img_borrosa

    img = cv2.imread(direct)
    img_borrosa = borr_img(img, factor = 45)
     
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    detector_cara = cv2.CascadeClassifier(perro)
    caras = detector_cara.detectMultiScale(gris, 1.1, 4)
     
    for x, y, w, h in caras:
       cara_detectada = img[int(y):int(y+h), int(x):int(x+w)]
       img_borrosa[y:y+h, x:x+w] = cara_detectada
         
    
    image_salida = cv2.cvtColor(img_borrosa, cv2.COLOR_BGR2RGB)
    cara = Image.fromarray(image_salida)    
    pit = cara.resize((800, 540), Image.Resampling.LANCZOS)
    global imag
    imag = pit
    pi = ImageTk.PhotoImage(pit)
    panel.config(image=pi)
    panel.place.config(x=400, y=100 )
    return panel 


# Esta función elimina el botón de profundidad y muestra 2 botones en pantalla
# Uno como botón que ejecutará la función de profundidad con el archivo de
# reconocimiento de gatos y otro botón que ejecutará la función de profundidad 
# con el archivo de perros

# Entrada: ''
# Salida: 2 botones en pantalla

def profundidad():
       boton_profundidad.place_forget()
       
       boton_retrato_gato = ttk.Button(text="Profundidad gato", 
                                  command=profundidad_gato)
       boton_retrato_gato.place(x=230, 
                           y=380, 
                           width = 110)

       boton_retrato_perro = ttk.Button(text="profundidad perro", 
                                  command=profundidad_perro)
       boton_retrato_perro.place(x=70, 
                           y=380, 
                           width = 110)


###################################TEXTO EN PANTALLA###########################################

# Primero se elije el texto y luego se pone en pantalla con coordenadas x e y
etiqueta_filtro = ttk.Label(text="Seleccione un filtro a aplicar:")
etiqueta_filtro.place(x=125, y=40)

etiqueta_nota = ttk.Label(text="ATENCIÓN: -Al aplicar un filtro puede \
tardarse unos momentos o incluso mostrar 'el programa no responde', \
en ese caso solo hay que esperar.")
etiqueta_nota.place(x=125, y=660)

etiqueta_nota_3 = ttk.Label(text="-El programa actualmente funciona con \
imagenes .jpg y .bmp, cualquier otro formato hará que los filtros \
no se apliquen.")
etiqueta_nota_3.place(x=190, 
                      y=677)

###################################BOTONES PARA APLICAR FILTROS###################################

# Botones a los que el usuario podrá "clickear" y así aplicar la función
# de algún filtro disponible.
# Se pondrán en pantalla con las coordenadas x e y ; Se seleccionara su grosor con width.
# Aquellos botones que usen state=tk.DISABLED están deshabilitados y tienen la función
# de mostrarle al usuario lo que podría estar proximamente disponible en el programa.

# Este botón aplica el filtro de escala de grises
boton_gris = ttk.Button(text="Escala de grises", 
                        command=gris, )
boton_gris.place(x=150, 
                 y=80, 
                 width = 110)

# Este botón aplica el filtro de sepía
boton_sepia = ttk.Button(text="Sepia", 
                         command=sepia)
boton_sepia.place(x=150, 
                  y=130, 
                  width = 110)

# Este botón aplica el filtro para pixelar la imagen
boton_pixel = ttk.Button(text="Pixelamiento", 
                         command=pixelado)
boton_pixel.place(x=150, 
                  y=180, 
                  width = 110)

# Este botón aplica el filtro para reflejar la parte izquierda de la imagen
boton_reflejo = ttk.Button(text="Reflejo horizontal", 
                           command=reflejo_horizontal)
boton_reflejo.place(x=150, 
                    y=230, 
                    width = 110)

# Este botón hará aparecer los botónes de retrato para gato y perro
boton_retrato = ttk.Button(text="Retrato", 
                           command=retrato)
boton_retrato.place(x=150, 
                    y=280, 
                    width = 110)

# Este botón hará aparecer los botónes de borde cuadrado, circular y rómbico
boton_borde = ttk.Button(text="Bordes", 
                           command=borde)
boton_borde.place(x=150, 
                    y=330, 
                    width = 110)

# Este botón hará aparecer los botónes de profundidad para gato y perro
boton_profundidad = ttk.Button(text="Profundidad", 
                           command=profundidad)
boton_profundidad.place(x=150, 
                    y=380, 
                    width = 110)

# Botón deshabilitado.
# Tendrá la función de aplicar el filtro para saturar la imagen
boton_saturacion = ttk.Button(text="Saturación", 
                           state=tk.DISABLED)
boton_saturacion.place(x=150, 
                    y=430, 
                    width = 110)

# Botón deshabilitado.
# Tendrá la función de aplicar el filtro para mezclar 2 imágenes
boton_mezclar = ttk.Button(text="Mezclar imágenes", 
                           state=tk.DISABLED)
boton_mezclar.place(x=150, 
                    y=480, 
                    width = 110)

# Botón deshabilitado.
# Tendrá la función de hacer que el usuario seleccione un accesorio desde el explorador
# de archivos y aplicarlo a la imagen
boton_accesorio = ttk.Button(text="Colocar accesorio", 
                            state=tk.DISABLED)
boton_accesorio.place(x=150, 
                    y=530, 
                    width = 110)

# Botón deshabilitado.
# Tendrá la función de aplicar el filtro para enfocar la imagen
boton_enfocar = ttk.Button(text="Enfocar", 
                           state=tk.DISABLED)
boton_enfocar.place(x=150, 
                    y=580, 
                    width = 110)

###################################BOTONES CONTROL DE USUARIO#####################################

# Botones a los que el usuario podrá "clickear" y así utilizar las funciones
# de control
# Se pondrán en pantalla con las coordenadas x e y ; Se seleccionara su grosor con width.

# Este botón ejecutará la función para cargar una nueva imagen al programa, una
# vez seleccionada una anterior
boton_cargar = ttk.Button(text="Cargar imagen", 
                          command=cargar_nuevo)
boton_cargar.place(x=400, 
                   y=30, 
                   width = 110)

# Este botón ejecutará la función para guardar la imagen ya editada
# abriendo el explorador de archivos.
boton_guardar = ttk.Button(text="Guardar imagen", 
                           command=guardar)
boton_guardar.place(x=550, 
                    y=30, 
                    width = 110)

# Este botón ejecutará la función para mostrar la imagen sin ninguna modificación.
boton_original = ttk.Button(text="Mostrar imagen original", 
                            command=original)
boton_original.place(x=1000, 
                     y=30, 
                     width = 200)

# Mostrara la ventana creada al inicio
ventana.mainloop()