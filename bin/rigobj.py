



class MyRig:

    freq = ''
    mode =''
    bandEdge = ''
    vfoMode = ''
    memoryMode = ''
    memoryCh = ''
    scanEdgeChP1 = ''
    scanEdgeChP2 = ''
    attenuator = ''
    afLevel = ''
    rfGain = ''
    squelchLevel = ''
    nrLevel = ''
    xvcrOnOff = ''
    xcvrId = ''

    def __init__(self):
        self.freq = ''
        self.mode = ''
        self.xcvrId = ''

    def setFreq(self, freq):
        self.freq = freq
        print('Freq :' + freq)
        

