import tkinter
import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

#Funcion que activa el boton y muestra la imagen a blanco y negro
def textoCaja(textoEntrada):
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
                              text = "Comenzar",
                              padx = 25, pady = 15,
                              command = lambda: textoCaja(textoEntrada))
botonEntrada.grid(row = 3, column = 0)

botonEcualizacion = tkinter.Button(ventana,
                                   text = "Ecualizar",
                                   padx = 25, pady = 15,
                                   )
botonEcualizacion.grid(row = 3, column = 1)

botonFiltro = tkinter.Button(ventana,
                             text = "Aplicar filtro \n(Gaussiano)",
                             padx = 25, pady = 15,
                             )
botonFiltro.grid(row = 3, column = 2)


ventana.mainloop()


 
 