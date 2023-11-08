import cv2


# Crea nuestro body classifier
clasificador_cuerpo= cv2.CascadeClassifier("haarcascade_fullbody.xml")
# Inicializa video capture para el archivo de video
cap = cv2.VideoCapture('walking.avi')

# Pasa el bucle ya que el video se haya cargado correctamente


while True:
    
    # Lee el primer cuadro
    frame = cap.read()

    # Convierte cada cuadro en escala de grises
    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cuerpo = clasificador_cuerpo.detectMultiScale(gray,1.2,3)
    # Pasa los cuadros a nuestro body classifier
    for (x,y,w,h) in cuerpo:
  ##obtiene las dimensiones del mismo algoritmo
       cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

       # Corta la imagen para guardar la imagen del rostro.
       color = frame[y:y+h, x:x+w]
       
    # Extrae los cuadros delimitadores de los cuerpos identificados
    

    if cv2.waitKey(1) == 32: #32 es la tecla espaciadora
        break
cv2.imshow(cap)
cap.release()
cv2.destroyAllWindows()
