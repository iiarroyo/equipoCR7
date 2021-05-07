import tkinter
import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from hist import equalize
from convolucion_proyecto import convolucion

#Variables globales 
imageLoad = []            
filtro = np.array([[0,0,0,5,0,0,0],
                         [0,5,18,32,18,5,0],
                         [0,18,64,100,64,18,0],
                         [5,32,100,100,100,32,5],
                         [0,18,64,100,64,18,0],
                         [0,5,18,32,18,5,0],
                         [0,0,0,5,0,0,0]])
     
estilo = 'gray'
actual = " "
output = []

#Funcion que activa el boton y muestra la imagen a blanco y negro
def textoCaja(textoEntrada):
    global imageLoad
    global estilo
    global actual
    
    actual = "original"
    imageLoad = cv2.imread(str(textoEntrada.get()))
   
    if len(imageLoad.shape) == 3:
        imageLoad = cv2.cvtColor(imageLoad, cv2.COLOR_BGR2GRAY)
    
    fig = plt.figure()
    ax = fig.add_subplot(111)  
    ax.axis('off')
    ax.imshow(imageLoad,cmap=estilo) 
    canvas = FigureCanvasTkAgg(fig, ventana) 
    canvas.get_tk_widget().grid(row=5, column=0, columnspan = 3)
    canvas.draw_idle()      

#Funcion para ecualizar una
def ecualizar():
    global imageLoad
    global estilo
    global actual
    
    actual = "ecualizada"
    imageLoad = equalize(imageLoad)
    fig = plt.figure()
    ax = fig.add_subplot(111)  
    ax.axis('off')
    ax.imshow(imageLoad, cmap=estilo) 
    canvas = FigureCanvasTkAgg(fig, ventana) 
    canvas.get_tk_widget().grid(row=5, column=0, columnspan = 3)
    canvas.draw_idle()

#Funcion para hacer la convolucion de una imagen con un filtro gaussiano
def conv():
    global imageLoad
    global filtro
    global estilo
    global actual
    global output
    
    output = convolucion(imageLoad, filtro)
    actual = "conv"
    fig = plt.figure()
    ax = fig.add_subplot(111)  
    ax.axis('off')
    ax.imshow(output, cmap=estilo) 
    canvas = FigureCanvasTkAgg(fig, ventana) 
    canvas.get_tk_widget().grid(row=5, column=0, columnspan = 3)
    canvas.draw_idle()

#Funcion para cambiar el etilo de la imagen
def cambiarEstilo(style):
    global estilo
    global actual
    global output
    
    estilo = style
    
    if(actual == "original"):
        textoCaja(textoEntrada)
    elif(actual == "ecualizada"):
        ecualizar()
    elif(actual == "conv"):
        fig = plt.figure()
        ax = fig.add_subplot(111)  
        ax.axis('off')
        ax.imshow(output, cmap=estilo) 
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
                                   command = ecualizar
                                   )
botonEcualizacion.grid(row = 3, column = 1)

botonFiltro = tkinter.Button(ventana,
                             text = "3. Aplicar filtro \n(Gaussiano)",
                             padx = 25, pady = 15,
                             command = conv)
botonFiltro.grid(row = 3, column = 2)


botonEstilo1 = tkinter.Button(ventana,
                             text = "4. Aplicar estilo 'winter'",
                             padx = 25, pady = 15,
                             command = lambda: cambiarEstilo('winter'))
botonEstilo1.grid(row = 6, column = 0)

botonEstilo2 = tkinter.Button(ventana,
                             text = "5. Aplicar estilo 'hot'",
                             padx = 25, pady = 15,
                             command = lambda: cambiarEstilo('hot'))
botonEstilo2.grid(row = 6, column = 1)

botonEstilo3 = tkinter.Button(ventana,
                             text = "6. Aplicar estilo 'cool'",
                             padx = 25, pady = 15,
                             command = lambda: cambiarEstilo('cool'))
botonEstilo3.grid(row = 6, column = 2)

ventana.mainloop()


 
 