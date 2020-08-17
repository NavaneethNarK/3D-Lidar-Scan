add_library('serial')
f=open('C:/Users/Navaneeth Narayan K/Desktop/computer/final/Processing/combine/test.txt','w') 
inString='0 0 0'
a=0
state=True
temp=[]
def setup():
    size(500,500,P3D)
    background(0)
    #setup the serial port
    print Serial.list()
    portIndex = 0
    LF = 10
    print "Connecting to ", Serial.list()[portIndex]
    myPort = Serial(this,Serial.list()[portIndex], 9600)   # this seems to need a first argument referring to the sketch object (analagous to "this" argument in Java)
    myPort.bufferUntil(LF)
    myPort.write(1)
def draw():
    global inString,a,state,temp
    if inString!='done' and state:
        
        stroke(255)
        strokeWeight(2)
        point(int(inString[0])*10+100,int(inString[2])*10+100,int(inString[4])*10+100)
    else:
        state=False
        for i in temp:
            rotateX(a)
            point(temp[0],temp[1],temp[2])
            
        
            a+=0.01
    
def serialEvent(vt):
    global inString,temp
    inString = vt.readString()
    f.write(inString)
    temp.append(int(inString[0])*10+100,int(inString[2])*10+100,int(inString[4])*10+100)
    print inString
