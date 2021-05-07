# equipoCR7

Pre procesamiento de imagen para filtro de "celular" con 2 fases (equalizacion de histograma y convolucion con filtro gausiano) e interfaz gráfica

>*Integrantes*:
>
>- Israel Arroyo A01706190
>- Miguel Luna A01706424
>- Kevin Joan Delgado A01706328

## Correr proyecto

Para ejecutar el programa se necesitan las siguientes librerias de python:

- tkinter
- numpy
- opencv-python
- matplotlib

El programa principal es *interfaz.py*. Cuando este se corre se utilizan las funciones de convolución y ecualizacion para lanzar la interfaz grafica de tkinter.
Los archivos *convloucion_proyecto.py* y *hist.py* se pueden correr por separado para probar casos de prueba.

## Equalizacion de histograma

Con esta primera fase se mejora la calidad de detalles de una fotografía. Si se corre el archivo *hist.py*, se observan los siguientes resultados:
![Imagen 1](/images/original_equalized.png)

Pues al separar la distribución de valores en el histograma, se mejora el contraste.(Mordvintsev, A. & Abid K., 2013)

## Filtro de blur

Con esta fase se aplica la convloucion con el filtro de blur de Gauss. Se declararon varios filtros para casos de prueba, además del blur de Gauss.
Para añadir estilos, la funcion *convolucion* recibe el nombre del *cmap* deseado, para lograr algún efecto deseado.

## Interfaz

La interfaz diseñada permite observar los cambios en una misma imagen.

En la caja de texto se ingresa el nombre del archivo a modificar. Después, se presiona el botón de comenzar para cargar la imagen e imprimirla en pantalla.

Los botones de ecualizar y aplicar filtro de Gauss hacen lo discutido anteriormente.

Al final, se puede aplicar un estilo diferente, después de haber equalizado o aplicado el filtro. Con esto, se cambian aspectos de color de la imagen. Se pueden escoger 3 estilos diferentes

![Imagen 1](/images/interfaz.png)

## Referencias
Mordvintsev, A. & Abid K. (2013). Histograms - 2: Histogram Equalization. 6 de mayo, 2021, de OpenCV-Python Tutorials Sitio web: <https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_histograms/py_histogram_equalization/py_histogram_equalization.html>
