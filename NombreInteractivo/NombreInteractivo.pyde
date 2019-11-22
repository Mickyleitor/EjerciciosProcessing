myNombreX1 = ( 20,20,40,60,80,100,100,100,160,160,160,200,240 )
myNombreX2 = ( 20,40,60,60,80,100,140,140,160,180,180,220,200 )
myNombreY1 = ( 60,20,40,20,20,20,20,60,20,40,40,20,20)
myNombreY2 = ( 20,40,20,60,60,60,20,60,60,20,60,40,60)

# Crear una variable "midesplazamientoX,midesplazamientoY" para
# y sumar este valor en line(...) para realizar desplazamiento del nombre
# a donde queramos

def setup() :
    size(800,800)
    

def draw() :
    background(255) 
    
    for i in range ( 0 , 13 ) :
        line(myNombreX1[i],myNombreY1[i],myNombreX2[i],myNombreY2[i])

    line(0,height/2,width,height/2)
    line(width/2,0,width/2,height)
    
    # Fin del draw()
