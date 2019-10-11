# Variables para la posicion de nuestra pelota
posicionPelotaX = 0
posicionPelotaY = 0

# Variables para el movimiento de la pelota
# este incremento se sumará o restará a la pelota
# dando un efecto de movimiento a la pelota
incrementoX = 5
incrementoY = 5

# Variables para la posicion de nuestras barras
posicionBarraIzqY = 0
posicionBarraDerY = 0

# Variables para la puntuación de los jugadores
puntuacionJugadorIzq = 0
puntuacionJugadorDer = 0

def setup() :
    # Nuestra programa será de 800 px por 800 px
    size(800,800)
    # ¿Mas cosas que podríamos hacer aquí?
    # Ejemplo: dar un valor aleatorio a la pelota
    # al inicio del programa
    
    
def draw() :
    # Exportamos nuestras variables globales
    # para que se puedan usar dentro de draw()
    global posicionBarraIzqY, posicionBarraDerY, posicionPelotaX, posicionPelotaY, incrementoX, incrementoY, puntuacionJugadorIzq, puntuacionJugadorDer
    
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
    
    
    # ¿La posición X de la pelota es mayor nuestro width? (Limite derecho)
    if (posicionPelotaX > width) :
        # Aumentamos puntuacion del jugador izquierdo
        # ya que la pelota ha marcado puntuacion por el lado derecho
        puntuacionJugadorIzq = puntuacionJugadorIzq + 1
        # Si lo supera, el incremento será negativo
        # equivalente a que la pelota vaya hacia la izquierda
        incrementoX = -5
        # Reseteamos la pelota al centro de la pantalla
        posicionPelotaX = width/2
        posicionPelotaY = height/2

    # ¿La posición X de la pelota es menor 0? (Limite izquierdo)
    if (posicionPelotaX < 0) :
        # Aumentamos puntuacion del jugador derecho
        # ya que la pelota ha marcado puntuacion por el lado izquierdo
        puntuacionJugadorDer = puntuacionJugadorDer + 1
        # Si es menor, el incremento será positivo
        # equivalente a que la pelota vaya hacia la derecha
        incrementoX = 5
        # Reseteamos la pelota al centro de la pantalla
        posicionPelotaX = width/2
        posicionPelotaY = height/2
        
        
    # ¿La posición Y de la pelota es mayor que nuestro height? (Limite inferior)
    if (posicionPelotaY > height) :
        # Si es mayor, el incremento será negativo
        # equivalente a que la pelota vaya hacia arriba
        incrementoY = -5
        
    # ¿La posición Y de la pelota es menor 0? (Limite superior)
    if (posicionPelotaY < 0) :
        # Si es menor, el incremento será positivo
        # equivalente a que la pelota vaya hacia abajo
        incrementoY = 5
    
    
    # Si la pelota está horizontalmente en la misma posicion o mas hacia la izquierda que la barra izquierda...
    if( posicionPelotaX < 30) :
        # Y ademas se encuentra entre el extremo superior < posicion Y pelota < extremo inferior de la barra izquierda..
        if (( posicionPelotaY > posicionBarraIzqY ) and (posicionPelotaY < posicionBarraIzqY + 100)) :
            # Invertir dirección hacia la derecha (X positiva)
            incrementoX = 5
                
    # Si la pelota está horizontalmente en la misma posicion o mas hacia la derecha que la barra derecha...
    if( posicionPelotaX > width - 30) :
        # Y ademas se encuentra entre el extremo superior < posicion Y pelota < extremo inferior de la barra derecha..
        if (( posicionPelotaY > posicionBarraDerY ) and (posicionPelotaY < posicionBarraDerY + 100)) :
            # Invertir dirección hacia la izquierda (X negativa)
            incrementoX = -5

    
    # Aqui sumamos los incrementos de X e Y a las posiciones
    # OJO POR QUE SON INCREMENTOS DEL VALOR ACTUAL.
    posicionPelotaX = posicionPelotaX + incrementoX
    posicionPelotaY = posicionPelotaY + incrementoY
    
    # Vaciamos fondo
    background(0)
    
    # Creamos barra izquierda y derecha con funcion rect
    rect(20,posicionBarraIzqY,10,100)
    rect(width - 30,posicionBarraDerY,10,100)
    
    # Creamos pelota con funcion ellipse
    ellipse(posicionPelotaX,posicionPelotaY,10,10)
    # Con esta función ponemos las letras bastante mas grandes de lo normal
    textSize(32)
    # Creamos los textos con las puntuaciones en el area que queramos
    text(puntuacionJugadorDer,width/2 + 100, height - 100)
    text(puntuacionJugadorIzq,width/2 - 100, height - 100)
