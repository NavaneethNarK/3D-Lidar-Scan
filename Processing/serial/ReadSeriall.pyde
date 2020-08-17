add_library('serial')
f=open('C:/Users/Navaneeth Narayan K/Desktop/computer/final/Processing/serial/test.txt','w') 
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
    pass
     
def serialEvent(vt):
    inString = vt.readString()
    f.write(inString)
    print inString
    stroke(255)

    strokeWeight(2)
    point(int(inString[0])*10,int(inString[2])*10,int(inString[4])*10)
    print(int(inString[0])*10)
