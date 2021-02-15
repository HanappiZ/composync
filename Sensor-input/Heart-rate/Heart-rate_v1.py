import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

#create the IC2 bus

i2c = busio.I2C(board.SCL, board.SDA)

#ADC object
ads = ADS.ADS1115(i2c)

#Single ended input on channels
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)
chan3 = AnalogIn(ads, ADS.P3)

if __name__ == '__main__':
    #initialize
    GAIN = 2/3
    curState = 0
    thresh = 525
    P = 512
    T = 512
    stateChanged = 0
    sampleCounter = 0
    lastBeatTime = 0
    firstBeat = True
    secondBeat = False
    Pulse = False
    IBI = 600
    rate = [0]*10
    amp = 100
    
    lastTime = int(time.time()*1000)
    
    #Main Loop
    
    while True:
        #read from ADC
        Signal = chan3.value
        curTime = int(time.time()*1000)
        
        sampleCounter += curTime - lastTime;
        lastTime = curTime
        N = sampleCounter - lastBeatTime;
        
        ##find the peak
        if Signal < thresh and N > (IBI/5.0)+3.0 :
            if Signal < T :
                T = Signal;
                
        if Signal > thresh and Signal > P:
            P = Signal;
        
        #signal surges up in value everytime thereis a pulse
        
        if N > 250 :
            if (Signal > thresh) and (Pulse == False) and (N > (IBI/5.0)*3.0) :
                Pulse = True;
                IBI = sampleCounte - lastBeatTime;
                lastBeatTime = sampleCounter;
                
                if secondBeat :
                    secondBeat = False;
                    for i in range (0,10):
                        rate[i] = IBI;
                
                if firstBeat :
                    firstBeat = False;
                    secondBeat = True;
                    continue
                #keep a running total of the last 10 IBI values
                runningTotal = 0;
                
                for i in range(0,9):
                    rate[i] = rate [i+1],
                    runningTotal += rate[i];
                    rate[9] = IBI;
                    runningTotal += rate[9]
                    runningTotal /= 10;
                    BPM = 60000/runningTotal
                    print('BPM: {}'.format(BPM))
                    
                if Signal < thresh and Pulse == True :
                    
                    Pulse = False;
                    amp = P - T;
                    thresh = amp/2 + T;
                    P = thresh;
                    T = thresh,
                if N > 2500 :
                    thresh = 512;
                    P = 512;
                    T = 512;
                    lastBeatTime = sampleCounter;
                    firstBeat = True;
                    secondBeat = False;
                    print("no beats found")
                time.sleep(0.005)