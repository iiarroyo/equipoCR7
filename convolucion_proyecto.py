# convolucion_persona.py
# Versión 1
# Herramientas computacionales: El arte de la programación

import numpy as np
import cv2
import matplotlib.pyplot as plt

def suma_matrices(matriz,kernel):
    """multiplicar la matriz cortada y la de kernel para devolver la suma"""

    m_row, m_col = matriz.shape                   
    k_row, k_col = kernel.shape                       
    resultado = 0                               

    for row in range (m_row):                               
        for col in range (m_col):                       
            resultado+= matriz[row,col] * kernel[row,col]      
    return resultado                                       
 
def convolucion(imagen, kernel):
    """Aplicar la convolución según la imagen, al ser de 3 canales o dimensiones, se cambiaran a dos canales"""
    
    if len(imagen.shape) == 3:
        print("Found 3 Channels : {}".format(imagen.shape)) 
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        print("Converted to Gray Channel. Size : {}".format(imagen.shape)) 
    else:
        print("Imagen Shape : {}".format(imagen.shape)) 
 
    imagen_row, imagen_col = imagen.shape 
    kernel_row, kernel_col = kernel.shape 
    
    output_x = (imagen_col - (kernel_col / 2) * 2) + 1 
    output_y = (imagen_row - (kernel_row / 2) * 2) + 1 
    
    output_x_int = int (output_x) 
    output_y_int = int (output_y) 
    
    output = np.zeros([output_y_int, output_x_int])
 
    for row in range(output_y_int): 
        for col in range(output_x_int):
                output[row,col] = suma_matrices( 
                                    imagen[row:row + kernel_row, 
                                    col:col + kernel_col],kernel) 
 
    print("Output Imagen size : {}".format(output.shape)) 
 
    return output
    

if __name__ == '__main__':
    imagen = cv2.imread("persona.jpg")
    
    filtro = np.array([[-1,0,1],
                      [-2,0,2],
                      [-1,0,1]])
    

    resultado = convolucion(imagen,filtro)
    
    plt.imshow(resultado, cmap='gray')
    plt.title("Sobel Edge Filter (persona)")
    plt.show()