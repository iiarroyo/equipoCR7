import numpy as np
import cv2
import matplotlib.pyplot as plt

def equalize(image,verbose=False):
    '''
    Recibe imagen (numpy.ndarray) y bandera verbose
    Regresa imagen equalizada
        Puede imprimir comparacion de 
        histograma e imagen
    '''
    image_eq = cv2.equalizeHist(image)
    if verbose:
        # calcula histograma de img
        h = [0]*256
        for value in range(256):
            h[value] = (image==value).sum()
        
        #calcula histograma de img equalizada
        h_eq = [0]*256
        for value in range(256):
            h_eq[value] = (image_eq==value).sum()
        
        #impresion de comparacion de imagen
        res_img = np.hstack((image,image_eq))
        plt.imshow(res_img,cmap='gray')
        plt.title("Imagen original vs equalizada")
        plt.show()
        
        #impresion histograma original
        plt.bar(range(256),h)
        plt.title("Histograma original")
        plt.show()

        #impresion histograma equalizado
        plt.bar(range(256),h_eq)
        plt.title("Histograma equalizado")
        plt.show()
        

    return image_eq

if __name__ == "__main__" :
    image = cv2.imread("persona.jpg",cv2.IMREAD_GRAYSCALE)
    res = equalize(image,verbose=True)
