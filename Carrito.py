from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *
from Escenario import *

escenario = Escenario()

class Carrito:

    def actualizar(self, window):

        

        estadoIzq = glfw.get_key(window, glfw.KEY_LEFT)
        estadoDer = glfw.get_key(window, glfw.KEY_RIGHT)
        estadoArriba = glfw.get_key(window, glfw.KEY_UP)
        estadoAbajo = glfw.get_key(window, glfw.KEY_DOWN)

        if estadoIzq == glfw.PRESS:
            escenario.xCarrito -=  0.0035
        if estadoDer == glfw.PRESS:
            escenario.xCarrito +=  0.0035
        if estadoAbajo == glfw.PRESS:
            escenario.yCarrito -= 0.0035
        if estadoArriba == glfw.PRESS:
            escenario.yCarrito += 0.0035
        

    def dibujarCarrito(self):


        glPushMatrix()
        glTranslate(escenario.xCarrito, escenario.yCarrito, 0.0)
        glBegin(GL_TRIANGLES)
        if escenario.colisionando == True:
            glColor3f(0.4,0.8,0.1)
        else:
            glColor3f(0.0,0.0,0.0)

        glVertex3f(0.0,0.015,0.0)
        glVertex3f(-0.015,-0.015,0.0)
        glVertex3f(0.015,-0.015,0.0)
        

        glEnd()
        glPopMatrix()

    def dibujarObstaculo(self):


        glPushMatrix()
        glTranslate(escenario.xObstaculo, escenario.yObstaculo, 0.0)
        glBegin(GL_QUADS)
        glColor3f(0.8,1.0,1.1)
        glVertex3f(-0.15,0.15,0.0)
        glVertex3f(0.00, 0.15,0.0)
        glVertex3f(0.00,-0.15,0.0)
        glVertex3f(-0.15, -0.15,0.0) 
        glEnd()
        glPopMatrix()

    def checar_colisiones(self):

            #los laditos--------------------
            #Si extreDerechaCarrito > extreIzqObstaculo
            #Y extreDerechaCarrito < extreIzqObstacu


        if escenario.xCarrito +0.05 > escenario.xObstaculo -0.15 and  escenario.xCarrito -0.05 < escenario.xObstaculo and escenario.yCarrito +0.05 > escenario.yObstaculo - 0.15 and escenario.yCarrito - 0.05< escenario.yObstaculo + 0.15:
            escenario.colisionando = True
        else:
            escenario.colisionando = False
        #eje y ----------------------------------
        #si ext superiorCarrirto > ExtrInferior obstaculo
        #y extremoinferiorcarrito <extresmsuperior obstaculo
    

        
