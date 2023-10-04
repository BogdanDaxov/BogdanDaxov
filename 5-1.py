import RPi.GPIO as a
import time as b
def binar(n):
    return [int(bit) for bit in bin(n)[2:].zfill(8)]
def adc(k):
    a.output(dac,binar(k))
    return(k)
a.setmode(a.BCM)
dac =[8,11,7,1,0,5,12,6]
comp=14
tri=13
a.setup(dac ,a.OUT)
a.setup(tri,a.OUT,initial=a.HIGH)
a.setup(comp,a.IN)
try:
    while (True):
        for i in range(0,256):
            f=adc(i)
            b.sleep(0.0006)
            if a.input(comp)==1:
                print(binar(i)," V=",i/256*3.3)
                break
finally:
    a.output(dac,0)
    a.cleanup(dac)
    a.output(tri,0)
    a.cleanup(tri)