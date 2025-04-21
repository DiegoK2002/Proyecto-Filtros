import cv2


acc = cv2.imread(r'C:\Users\diego\Desktop\Filtros\gorro.png', cv2.IMREAD_UNCHANGED)
 
#Cargamos los clasificadores requeridos
face_cascade = cv2.CascadeClassifier(r'C:\Users\diego\AppData\Local\Programs\PythonCodingPack\Lib\site-packages\cv2\data\haarcascade_frontalcatface.xml')
 
#Utilizamos un fichero de imagen del disco duro
img = cv2.imread(r'C:\Users\diego\Desktop\Filtros\gato.jpg')
 
while(True):
    #Convertimos la imagen a blanco y negro
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #Buscamos las coordenadas de los rostros
    caras = face_cascade.detectMultiScale(gray, 1.3, 5)
    #Dibujamos un rectángulo en las coordenadas de cada rostro
    numCaras = 0
    for (x,y,w,h) in caras:
        cv2.rectangle(img,(x,y),(x+w,y+h),(125,255,0),2)
        numCaras = numCaras + 1
    #Mostramos la imagen
#    cv2.imshow('img',img)
    #Pulsando la tecla "q" salimos del programa
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

resized_image = img.resize(acc, width=w)
filas_image = resized_image.shape[0]
col_image = w    

porcion_alto = filas_image // 4
dif = 0

if y + porcion_alto - filas_image >= 0:
    n_frame = img[y + porcion_alto - filas_image : y + porcion_alto,
        x : x + col_image]
else:
    dif = abs(y + porcion_alto - filas_image) 
    n_frame = img[0 : y + porcion_alto,
        x : x + col_image]

mask = resized_image[:, :, 3]
mask_inv = cv2.bitwise_not(mask)

bg_black = cv2.bitwise_and(resized_image, resized_image, mask=mask)
bg_black = bg_black[dif:, :, 0:3]
bg_frame = cv2.bitwise_and(n_frame, n_frame, mask=mask_inv[dif:,:])

result = cv2.add(bg_black, bg_frame)
if y + porcion_alto - filas_image >= 0:
    img[y + porcion_alto - filas_image : y + porcion_alto, x : x + col_image] = result
else:
    img[0 : y + porcion_alto, x : x + col_image] = result
    cv2.imshow('img',img)
    k = cv2.waitKey(1) & 0xFF
img.release()
cv2.destroyAllWindows()


cv2.imshow('result',img)

print ("Número de caras detectadas: {}".format(numCaras))