myNombreX1 = ( 20,20,40,60,80,100,100,100,160,160,160,200,240 )
myNombreX2 = ( 20,40,60,60,80,100,140,140,160,180,180,220,200 )
myNombreY1 = ( 60,20,40,20,20,20,20,60,20,40,40,20,20)
myNombreY2 = ( 20,40,20,60,60,60,20,60,60,20,60,40,60)

desplazamientoX = 0
desplazamientoY = 0

def setup() :
    size(800,800)
    

def draw() :
    background(255)
    
    for i in range ( 0 , 13 ) :
        line(myNombreX1[i]+desplazamientoX,myNombreY1[i]+desplazamientoY,myNombreX2[i]+desplazamientoX,myNombreY2[i]+desplazamientoY)
        
    if mousePressed :
        moverNombre()

    line(0,height/2,width,height/2)
    line(width/2,0,width/2,height)
    
    # Fin del draw()
    
def moverNombre():
    global desplazamientoX,desplazamientoY
    # Actualizar posicion de nombre con respecto a mouseX y mouseY
    desplazamientoX = mouseX
    desplazamientoY = mouseY
