# Crear 4 Arrays que contengan todos los X1,X2,Y1,Y2 para
# la funcion line(...)
# Ejemplo : myNombreX1 = { 20 , 10 , 50, 10 }
myNombreX1 = { 20,20,40,60,80,100,100,100,160,160,160,200,240 }
myNombreX2 = { 20,40,60,60,80,100,140,140,160,180,180,220,200 }
myNombreY1 = { 60,20,40,20,20,20,20,60,20,40,40,20,20}
myNombreY2 = { 20,40,20,60,60,60,20,60,60,20,60,40,60}

##RELLENAR AQUI

def setup() :
    size(800,800)
    

def draw() :
    background(255) 
    
    # Sustituir los valores fijos por los valores de los arrays 
    # en las funciones line
    # ejemplo, el primer line(...) sería line(myNombreX1[0],myNombreY1[0],myNombreX2[0],myNombreY2[0])
    
    line(20,60,20,20)
    line(20,20,40,40)
    line(40,40,60,20)
    line(60,20,60,60)
    line(80,20,80,60)
    line(100,20,100,60)
    line(100,20,140,20)
    line(100,60,140,60)
    line(160,20,160,60)
    line(160,40,180,20)
    line(160,40,180,60)
    line(200,20,220,40)
    line(240,20,200,60)
    
        
    line(0,height/2,width,height/2)
    line(width/2,0,width/2,height)
    
    # Fin del draw()
