posicionBotonX = 300
posicionBotonY = 300
anchoBoton = 200
altoBoton = 100

def setup() :
    size(800,800)
    

def draw() :
    background(0) 
    if sobreBoton() :
        if mousePressed :
            fill(color(255,0,0))
        else :
            fill(color(128))        
    else :
        # Si está el raton pulsado,
        # mover el boton a donde esté pulsado el boton
        
        ## RELLENAR AQUI
        pass
        
        # si no, rellenar con fill(color(255))
    
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
    
def moverBoton():
    global posicionBotonX,posicionBotonY
    # Actualizar posicion de boton con respecto a mouseX y mouseY
