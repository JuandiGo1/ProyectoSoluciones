import numpy as np
import matplotlib.pyplot as plt
import sys

def main(rutaImg, escalaAumentoX,escalaAumentoY ):
    #Cargar la imagen original 
    original_image = plt.imread(rutaImg)

    #Definir los factores de escala para el aumento de resolución
    scale_x = escalaAumentoX
    scale_y = escalaAumentoY

    #Obtener el tamaño original de la imagen
    original_height, original_width, channels = original_image.shape

    #Calcular el nuevo tamaño de la imagen de alta resolución
    new_height = original_height * scale_y
    new_width = original_width * scale_x

    #Crear una matriz vacía para la nueva imagen de alta resolución
    high_res_image = np.zeros((new_height, new_width, channels), dtype=np.uint8)

    #Realizar la interpolación bilineal
    for y in range(new_height):
        for x in range(new_width):
            #Calcular las coordenadas correspondientes en la imagen original
            orig_x = x / scale_x
            orig_y = y / scale_y

            #Determinar los cuatro píxeles circundantes en la imagen original
            x0 = int(orig_x)
            x1 = min(x0 + 1, original_width - 1)
            y0 = int(orig_y)
            y1 = min(y0 + 1, original_height - 1)

            #Coeficientes para la interpolación bilineal, diferencias entre pixel original y el más cercano
            dx = orig_x - x0
            dy = orig_y - y0

            #Realizar la interpolación bilineal para cada canal de color
            for channel in range(channels):
                new_pixel = (1 - dx) * (1 - dy) * original_image[y0, x0, channel] + \
                                    dx * (1 - dy) * original_image[y0, x1, channel] + \
                                    (1 - dx) * dy * original_image[y1, x0, channel] + \
                                    dx * dy * original_image[y1, x1, channel]

                #Asignar el píxel interpolado a la nueva imagen
                high_res_image[y, x, channel] = int(new_pixel)

    #Guardar la imagen de alta resolución
    plt.imsave(rutaImg[:-4]+'_alta_resolucion.jpg', high_res_image)
    print("Cambio de resolucion: (",original_height,original_width,") --> (",new_height,new_width,")")


#main('pse.jpg', 5,5)

#Para ejecutar desde CMD
if __name__== "__main__":
    if len(sys.argv) != 4:
        print("Use: python bilineal.py imagen escalaAumentoX escalaAumentoY")
    else:
        rutaImg = sys.argv[1]
        escalaAumentoX = int(sys.argv[2])
        escalaAumentoY = int(sys.argv[3])
        main(rutaImg, escalaAumentoX, escalaAumentoY)
