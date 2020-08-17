x=[]
y=[]
z=[]
a=0
s=0
d=0
f=0
def setup():
    global x,y,z
    size(500,400,P3D)
    background(0)
    noFill()
    stroke(255)
    for i in range(400):
        x.append(int(random(-150,150)))
        y.append(int(random(-150,150)))
        z.append(int(random(-150,150)))
def draw():
    global x,y,z,a,s,d,f
    background(0)
    translate(width/2,height/2,f)
    rotateY(s)
    rotateX(a)
    rotateZ(d)    
    strokeWeight(2)
    for i in range(400):
        point(x[i],y[i],z[i])
    
    if keyPressed==True and key=='a':
        a+=0.01
    elif keyPressed==True and key=='q':
        a-=0.01
    if keyPressed==True and key=='w':
        s+=0.01
    elif keyPressed==True and key=='s':
        s-=0.01
    if keyPressed==True and key=='e':
        d+=0.01
    elif keyPressed==True and key=='d':
        d-=0.01
    if keyPressed==True and key=='f':
        f+=1
    elif keyPressed==True and key=='r':
        f-=1
