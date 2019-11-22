posicionBotonX = 300
posicionBotonY = 300
anchoBoton = 200
altoBoton = 100

def setup() :
    size(800,800)
    

def draw() :
    background(0)  
    if sobreBoton() :
        # Si el raton esta sobre el recuadro y está pulsando el boton izquierdo,
        # mover el recuadro hasta donde esté el mouse y rellenarlo con fill(color(200))
        # Si no, rellenar con fill(color(128))
        
        ## RELLENAR AQUI
        pass
    else :
        fill(color(255))
    
    rect(posicionBotonX,posicionBotonY,anchoBoton,altoBoton)
    
    # Fin del draw()

def sobreBoton() :
    if ( (mouseX > posicionBotonX) and (mouseX < posicionBotonX + anchoBoton)) :
        if ((mouseY > posicionBotonY) and (mouseY < posicionBotonY + altoBoton)) :
            return True
        else :
            return False
    else :
        return False
