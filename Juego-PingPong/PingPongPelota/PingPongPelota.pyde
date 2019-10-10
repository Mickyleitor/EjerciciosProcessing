
# Variables para la posicion de nuestra pelota
posicionPelotaX = 0
posicionPelotaY = 0

# Variables para el movimiento de la pelota
# este incremento se sumará o restará a la pelota
# dando un efecto de movimiento a la pelota
incrementoX = 5
incrementoY = 5

def setup() :
    # Nuestra programa será de 800 px por 800 px
    size(800,800)
    # ¿Mas cosas que podríamos hacer aquí?
    # Ejemplo: dar un valor aleatorio a la pelota
    # al inicio del programa
    
    
def draw() :
    # Exportamos nuestras variables globales
    # para que se puedan usar dentro de draw()
    global posicionPelotaX, posicionPelotaY, incrementoX, incrementoY
    
    # ¿La posición X de la pelota es mayor nuestro width? (Limite derecho)
    if (posicionPelotaX > width) :
        # Si lo supera, el incremento será negativo
        # equivalente a que la pelota vaya hacia la izquierda
        incrementoX = -5
    
    # ¿La posición X de la pelota es menor 0? (Limite izquierdo)
    if (posicionPelotaX < 0) :
        # Si es menor, el incremento será positivo
        # equivalente a que la pelota vaya hacia la derecha
        incrementoX = 5
        
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
        
    # Aqui sumamos los incrementos de X e Y a las posiciones
    # OJO POR QUE SON INCREMENTOS DEL VALOR ACTUAL.
    posicionPelotaX = posicionPelotaX + incrementoX
    posicionPelotaY = posicionPelotaY + incrementoY
    
    # Vaciamos fondo
    background(0)
    # Creamos pelota con funcion ellipse
    ellipse(posicionPelotaX,posicionPelotaY,10,10)
    
    
