# convolucion_persona.py
# Versión 2
# Herramientas computacionales: El arte de la programación

import numpy as np
import cv2
import matplotlib.pyplot as plt

def suma_matrices(matriz,kernel):
    """multiplicar la matriz cortada y la de kernel para devolver la suma"""

    m_row, m_col = matriz.shape                       #asignar el tamaño de la matriz (en filas y columnas)
    k_row, k_col = kernel.shape                       #asignar el tamaño del kernel (en filas y columnas)
    resultado = 0                                   #instanciar la resultante en ceros

    for row in range (m_row):                                #recorrer filas de la matriz
        for col in range (m_col):                            #recorrer columnas de la matriz
            resultado+= matriz[row,col] * kernel[row,col]       #acumular el resultado de cada una de las multiplicaciones entre las filas y columnas de la matriz y el kernel
    return resultado                                         #devolver resultante
 
def convolucion(imagen, kernel):
    """Aplicar la convolución según la imagen, al ser de 3 canales o dimensiones, se cambiaran a dos canales"""
    
    if len(imagen.shape) == 3:
        print("Found 3 Channels : {}".format(imagen.shape)) 
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        print("Converted to Gray Channel. Size : {}".format(imagen.shape)) 
    else:
        print("Imagen Shape : {}".format(imagen.shape))
 
    imagen_row, imagen_col = imagen.shape #asignar el alto y ancho de la imagen
    kernel_row, kernel_col = kernel.shape #asignar el alto y ancho del filtro
    
    output_x = (imagen_col - (kernel_col / 2) * 2) + 1 #asigna el ancho del output
    output_y = (imagen_row - (kernel_row / 2) * 2) + 1 #asigna el alto del output
    
    output_x_int = int (output_x) #cambiar los valores a enteros
    output_y_int = int (output_y) #cambiar los valores a enteros
    
    output = np.zeros([output_y_int, output_x_int]) #matriz donde se guardan las resultantes de las coordenadas
 
    for row in range(output_y_int): #recorrer las filas de la imagen
        for col in range(output_x_int): #recorrer las columnas de la imagen
            output[row,col] = suma_matrices(imagen[row:row + kernel_row,
                                                   col:col + kernel_col],kernel) #relizar la suma entre las filas de la matriz con la del kernel y lo mismo con las columnas
 
    print("Output Imagen size : {}".format(output.shape)) #Tamaño de la imagen final
 
    return output
    
def print_imagen(imagen,titulo,estilo):
    """Función que imprime la imagen, cmap permite obtener una gran cantidad de matices"""
    
    plt.imshow(imagen, cmap = estilo)
    plt.title(titulo)
    plt.show()


if __name__ == '__main__':
    imagen = cv2.imread("persona.jpg")
    
    filtro = np.array([[-1,0,1],
                      [-2,0,2],
                      [-1,0,1]])
    
    filtro2 = np.array([
                         [0,0,0,5,0,0,0],
                         [0,5,18,32,18,5,0],
                         [0,18,64,100,64,18,0],
                         [5,32,100,100,100,32,5],
                         [0,18,64,100,64,18,0],
                         [0,5,18,32,18,5,0],
                         [0,0,0,5,0,0,0]])
    
    filtro3 = np.array([[-1,-1,-1],
                        [-1,8,-1],
                        [-1,-1,-1]])
    

    print_imagen(convolucion(imagen,filtro),"Sobel Edge Filter (Winter)", "winter")
    print_imagen(convolucion(imagen,filtro2),"Gaussian Blur Filter (Hot)", "hot")
    print_imagen(convolucion(imagen,filtro3),"Laplacian Operator Filter (Cool)", "cool")
    
