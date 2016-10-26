class pcptron():
    def __init__(self):
        self.listWeigth = []
        self.bias = 0
        self.listInput01 = []
        self.listInput02 = []
        self.listInput = []
        self.output01 = 0
        self.output02 = 0
        self.listOutput = []
        self.limit = 0
        self.learningRate = 0
        self.output = 0
        self.error = 0
        self.u = 0
        self.main()
    
    def calculateU(self, n):
        aux = 0
        for i in range(len(self.listInput[n])):
            aux = aux + (self.listWeigth[i]*self.listInput[n][i])
        self.u = aux
    
    def f(self, u):
        if(u >= self.limit):
            return 1
        else:
            return 0
        
    def calculateOutput(self):
        self.output = self.f(self.u)
    
    def calculateError(self, n):
        self.error = (self.listOutput[n] - self.output)
    
    def adjustWeigth(self, n):
        for i in range(len(self.listInput[n])):
            self.listWeigth[i] = self.listWeigth[i] + self.learningRate * self.error * self.listInput[n][i]
                    
    def setValues(self):
        self.bias = -1
        self.limit = 0.5
        self.learningRate = 0.1
        self.output01 = 1
        self.output02 = 0
        self.output = 0
        self.error = -1
        self.u = 0
        self.listWeigth.append(-0.5441)
        self.listWeigth.append(0.5562)
        self.listWeigth.append(-0.4074)
        self.listInput01.append(self.bias)
        self.listInput01.append(2)
        self.listInput01.append(2)
        self.listInput02.append(self.bias)
        self.listInput02.append(4)
        self.listInput02.append(4)
        self.listInput.append(self.listInput01)
        self.listInput.append(self.listInput02)
        self.listOutput.append(self.output01)
        self.listOutput.append(self.output02)
        
    def main(self):        
        self.setValues()
        n = 0
        while(n < 2):
            self.calculateU(n)
            self.calculateOutput()
            self.calculateError(n)
            if(self.error != 0):
                self.adjustWeigth(n)
                print("Pesos: ",self.listWeigth)
                n = -1
            n = n + 1
            
p = pcptron
p()
