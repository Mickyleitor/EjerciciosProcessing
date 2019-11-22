posicionBotonX = 300
posicionBotonY = 300
anchoBoton = 200
altoBoton = 100

def setup() :
    size(800,800)
    

def draw() :
    background(0)
    # Utilizar la funcion sobreBoton() para ver si el raton está sobre el recuadro.
    # Si esta sobre el recuadro, rellenar con fill(color(128))
    # Si no esta sobre el recuadro, rellenar con fill(color(255))
    
    ## RELLENAR AQUI
    
    # Dibujar recuadro con rect(...) y los parametros definidos arriba del todo
    
    ## RELLENAR AQUI
    
    # Fin del draw()

def sobreBoton() :
    if ( (mouseX > posicionBotonX) and (mouseX < posicionBotonX + anchoBoton)) :
        if ((mouseY > posicionBotonY) and (mouseY < posicionBotonY + altoBoton)) :
            return True
        else :
            return False
    else :
        return False
