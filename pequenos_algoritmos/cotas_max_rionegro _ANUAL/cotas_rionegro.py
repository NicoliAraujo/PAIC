import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class data:

    def __init__(self):
        self.years = []
        self.cotas = []
        self.mouth = []
        self.frequency = []
        self.average = 0
        self.detour = 0
        self.variance = 0

    def countFrequency(self, n):
        vetCont = []
        for i in range(0,n):
            vetCont.append(0)
        for i in range(0,len(self.mouth)):
            vetCont[self.mouth[i]] += 1
            self.frequency.append(vetCont[self.mouth[i]])

def groupsYears(x):
    vet = []
    n = len(x.cotas)//10
    m = len(x.cotas)- n*10
    for i in range(0,n):
        for j in range(0,10):
            vet.append(i)
    for i in range(0,m):
        vet.append(n)
    return vet

def file(x):
    file01 = open('cotas_rionegro.csv','r')
    line = file01.readline()
    while line:
        line = file01.readline().split()
        if(len(line)==3):
            x.years.append(int(line[0]))
            x.cotas.append(float(line[1]))
            x.mouth.append(int(line[2]))
            
x = data()
file(x)
x.average = np.mean(x.cotas)
x.detour = np.sqrt(x.cotas)
x.variance = np.var(x.cotas)
x.countFrequency(12)
v = groupsYears(x)
print(x.frequency)
print(x.mouth)
sns.barplot(x = x.mouth, y = x.frequency, palette = 'Greys')
#sns.boxplot(x = v, y = x.cotas, palette = 'Greys')
sns.plt.savefig('/home/paic-elloa-janderson/Documentos/Algoritmos_Python/frequencia5.pdf')
