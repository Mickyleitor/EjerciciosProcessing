myNombreX1 = ( 20,20,40,60,80,100,100,100,160,160,160,200,240 )
myNombreX2 = ( 20,40,60,60,80,100,140,140,160,180,180,220,200 )
myNombreY1 = ( 60,20,40,20,20,20,20,60,20,40,40,20,20)
myNombreY2 = ( 20,40,20,60,60,60,20,60,60,20,60,40,60)

##RELLENAR AQUI

def setup() :
    size(800,800)
    

def draw() :
    background(255) 
    
    # Con un bucle tipo for, recorrer nuestro array para dibujar
    # nuestro nombre con una sola linea de line(...)
    # Recordatorio:
    # for i in range ( 0 , numero_elementos ) :
    
    ## RELLENAR AQUI
    
    line(myNombreX1[0],myNombreY1[0],myNombreX2[0],myNombreY2[0])
    line(myNombreX1[1],myNombreY1[1],myNombreX2[1],myNombreY2[1])
    line(myNombreX1[2],myNombreY1[2],myNombreX2[2],myNombreY2[2])
    line(myNombreX1[3],myNombreY1[3],myNombreX2[3],myNombreY2[3])
    line(myNombreX1[4],myNombreY1[4],myNombreX2[4],myNombreY2[4])
    line(myNombreX1[5],myNombreY1[5],myNombreX2[5],myNombreY2[5])
    line(myNombreX1[6],myNombreY1[6],myNombreX2[6],myNombreY2[6])
    line(myNombreX1[7],myNombreY1[7],myNombreX2[7],myNombreY2[7])
    line(myNombreX1[8],myNombreY1[8],myNombreX2[8],myNombreY2[8])
    line(myNombreX1[9],myNombreY1[9],myNombreX2[9],myNombreY2[9])
    line(myNombreX1[10],myNombreY1[10],myNombreX2[10],myNombreY2[10])
    line(myNombreX1[11],myNombreY1[11],myNombreX2[11],myNombreY2[11])
    line(myNombreX1[12],myNombreY1[12],myNombreX2[12],myNombreY2[12])

    line(0,height/2,width,height/2)
    line(width/2,0,width/2,height)
    
    # Fin del draw()
