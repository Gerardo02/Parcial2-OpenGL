from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *
from Carrito import *
from Escenario import *

carrito = Carrito()
escenario = Escenario()

class Dibujar:

    def start(self):
        glColor3f(0.0, 0.7, 0.0)
        glBegin(GL_POLYGON)
        for x in range(360):
            angulo = x * 3.14159 / 180.0
            glVertex3f(cos(angulo) * 0.10 - 0.72 ,sin(angulo) * 0.05 + 0.73,0.0)
        glEnd()


    def dibujar(self):
        global escenario
        global carrito

        escenario.caminos()
        escenario.paredes3()
        escenario.paredes2()
        
        carrito.dibujarObstaculo()
        carrito.dibujarCarrito()
