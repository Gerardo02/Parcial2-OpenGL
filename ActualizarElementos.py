from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *
from Carrito import *

carrito = Carrito()

class ActualizarElementos:
    def actualizar(self, window):
        global carrito

        carrito.actualizar(window)
        
        carrito.checar_colisiones()