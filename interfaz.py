import tkinter
import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from hist import equalize
from convolucion_proyecto import convolucion

imageLoad = []
            
filtro = np.array([[-1,0,1],
                      [-2,0,2],
                      [-1,0,1]])
    
filtro2 = np.array([[0,0,0,5,0,0,0],
                         [0,5,18,32,18,5,0],
                         [0,18,64,100,64,18,0],
                         [5,32,100,100,100,32,5],
                         [0,18,64,100,64,18,0],
                         [0,5,18,32,18,5,0],
                         [0,0,0,5,0,0,0]])
     
filtro3 = np.array([[-1,-1,-1],
                        [-1,8,-1],
                        [-1,-1,-1]])
 
 
#Funcion que activa el boton y muestra la imagen a blanco y negro
def textoCaja(textoEntrada):
    global imageLoad
    imageLoad = cv2.imread(str(textoEntrada.get()))
   
    if len(imageLoad.shape) == 3:
        print("Found 3 Channels : {}".format(imageLoad.shape))
        imageLoad = cv2.cvtColor(imageLoad, cv2.COLOR_BGR2GRAY)
    else:
        print("Image Shape : {}".format(imageLoad.shape))
    
    fig = plt.figure()
    ax = fig.add_subplot(111)  
    ax.axis('off')
    ax.imshow(imageLoad,cmap='gray') 
    canvas = FigureCanvasTkAgg(fig, ventana) 
    canvas.get_tk_widget().grid(row=5, column=0, columnspan = 3)
    canvas.draw_idle()      

def ecualizar():
    global imageLoad
    imageLoad = equalize(imageLoad)
    fig = plt.figure()
    ax = fig.add_subplot(111)  
    ax.axis('off')
    ax.imshow(imageLoad, cmap='gray') 
    canvas = FigureCanvasTkAgg(fig, ventana) 
    canvas.get_tk_widget().grid(row=5, column=0, columnspan = 3)
    canvas.draw_idle()
    
def conv():
    global imageLoad
    global filtro2
    fig = plt.figure()
    ax = fig.add_subplot(111)  
    ax.axis('off')
    ax.imshow(convolucion(imageLoad, filtro2), cmap='gray') 
    canvas = FigureCanvasTkAgg(fig, ventana) 
    canvas.get_tk_widget().grid(row=5, column=0, columnspan = 3)
    canvas.draw_idle()
    
#Creacion de la ventana de Tkinter
ventana = tkinter.Tk()
ventana.geometry("1010x800")

#Definicion de componentes de la interfaz como titulo, botones y carteles
titulo = tkinter.Label(ventana,
                       text = "Proyecto de Herramientas computacionales: el arte de la programación ",
                       font = "Helvetica 20",
                       justify = "center")
titulo.grid(pady = 20, row = 0, column = 0, columnspan = 3)

textoEntrada = tkinter.Entry(ventana,
                             font = ("Helvetica 20"))

textoEntrada.grid(pady = 20, row = 1, column = 0, columnspan = 3)

botonEntrada = tkinter.Button(ventana,
                              text = "1. Comenzar",
                              padx = 25, pady = 15,
                              command = lambda: textoCaja(textoEntrada))
botonEntrada.grid(row = 3, column = 0)

botonEcualizacion = tkinter.Button(ventana,
                                   text = "2. Ecualizar",
                                   padx = 25, pady = 15,
                                   command = lambda: ecualizar()
                                   )
botonEcualizacion.grid(row = 3, column = 1)

botonFiltro = tkinter.Button(ventana,
                             text = "3. Aplicar filtro \n(Gaussiano)",
                             padx = 25, pady = 15,
                             command = conv)
botonFiltro.grid(row = 3, column = 2)


ventana.mainloop()


 
 