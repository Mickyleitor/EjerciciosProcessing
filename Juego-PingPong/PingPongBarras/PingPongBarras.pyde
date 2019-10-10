
# Variables para la posicion de nuestras barras
posicionBarraIzqY = 0
posicionBarraDerY = 0

def setup() :
    # Nuestra programa será de 800 px por 800 px
    size(800,800)
    # ¿Mas cosas que podríamos hacer aquí?
    # Ejemplo: dar un valor aleatorio a la pelota
    # al inicio del programa
    
    
def draw() :
    # Exportamos nuestras variables globales
    # para que se puedan usar dentro de draw()
    global posicionBarraIzqY, posicionBarraDerY
    
    # Comprobamos si se ha pulsado alguna tecla
    if (keyPressed == True) :
        # Si se ha pulsado W, mover la barra izquierda hacia arriba
        if( key == 'w') :
            posicionBarraIzqY = posicionBarraIzqY - 10
        # Si se ha pulsado S, mover la barra izquierda hacia abajo
        if( key == 's') :
            posicionBarraIzqY = posicionBarraIzqY + 10
        # Si se ha pulsado O, mover la barra derecha hacia arriba
        if( key == 'o') :
            posicionBarraDerY = posicionBarraDerY - 10
        # Si se ha pulsado L, mover la barra derecha hacia abajo
        if( key == 'l') :
            posicionBarraDerY = posicionBarraDerY + 10
    
    # Comprobamos los limites inferior y superior de la barra izquierda
    if (posicionBarraIzqY < 0 ) :
        posicionBarraIzqY = 0
    if (posicionBarraIzqY > height - 100) :
        posicionBarraIzqY = height - 100
    
    # Comprobamos los limites inferior y superior de la barra derecha
    if (posicionBarraDerY < 0 ) :
        posicionBarraDerY = 0
    if (posicionBarraDerY > height - 100) :
        posicionBarraDerY = height - 100
        
    
    # Vaciamos fondo
    background(0)
    # Creamos barra izquierda y derecha con funcion rect
    rect(20,posicionBarraIzqY,10,100)
    rect(width - 30,posicionBarraDerY,10,100)
    

    
    
