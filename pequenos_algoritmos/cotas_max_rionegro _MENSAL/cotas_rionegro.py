import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

class data:

    def __init__(self):
        self.df = pd.read_csv('max_rionegro.csv', delim_whitespace = True)
        self.frequency = []
        self.average = 0
        self.detour = 0
        self.variance = 0

class statistics:

    def __init__(self, df):
        self.df = df

    def annual_average(self, y):
        return self.df.ix[y - self.df.year[0]][1:13].mean()
    
    def monthly_average(self, m):
        return self.df[m].mean()

    def annual_max(self, y):
        y = y - self.df.year[0]
        return [self.df.ix[y][1:13].max(),self.df.ix[y].argmax()]

    def monthly_max(self, m):
        return [self.df[m].max(),self.df[m].argmax() + self.df.year[0]]

    def annual_average_max(self):
        vect = []
        for i in range (0,self.df.shape[0]):
            vect.append(self.df.ix[i].max())
        return np.average(vect)

    def detour(self, typeDate, n):
        if(typeDate == 'year'):
            return self.df.ix[n - self.df.year[0]][1:13].std()
        elif(typeDate == 'month'):
            return self.df[n].std()

    def frequency(self):
        vect = {}
        for i in range(0, self.df.shape[0]):
            if(vect.get(self.df.ix[i].argmax()) == None):
                vect[self.df.ix[i].argmax()] = 1
            else:
                vect[self.df.ix[i].argmax()] += 1
        return vect

    def list_annual_max(self):
        vet = []
        for i in range(self.df.shape[0]):
            vet.append(self.df.ix[i].max())
        return(vet)
    
    def anomaly(self, average, vect):
        vet = []
        for i in range(len(vect)):
            vet.append(vect[i]-average)
        return vet

class graphics:

    def __init__(self,type_graph,df,vect,nameGraph):
        self.type_graph = type_graph
        self.df = df
        self.vect = vect
        self.nameGraph = nameGraph

        if(type_graph == 'barplot'):
            self.barplot_freq()
        elif(type_graph == 'boxplot'):
            self.boxplot_freq()

    def barplot_freq(self):
        df_freq = pd.DataFrame()
        aux = list(self.vect.items())
        aux.sort()
        m = []
        f = []
        for i in range(0,len(aux)):
            m.append(aux[i][0])
            f.append(aux[i][1])
        df_freq['month'] = m
        df_freq['frequency'] = f
        sns.barplot(x = df_freq.month, y = df_freq.frequency, palette = 'Greys')
        direct = os.getcwd()
        sns.plt.savefig(direct + '/'+self.nameGraph+'.pdf')


ct = data()
st = statistics(ct.df)
"""
print("Max. anual 1903: ",st.annual_max(1903))
print("Med. anual 1903: ",st.annual_average(1903))
print("Desv. padrão 1903: ",st.detour('year',1903))
print()
print("Max. mensal jan: ",st.monthly_max(str(1)))
print("Med. mensal jan: ",st.monthly_average(str(1)))
print("Desv. padrão jan: ",st.detour('month',str(1)))
print()
print("Med. das max. anuais: ",st.annual_average_max())

#print("Anomalia da cheia")
vect1 = st.list_annual_max()
print("Anomalia das cheias: ",st.anomaly(st.annual_average_max(), vect1))
vect = st.frequency()
print("Freq. das max. anuais: ",vect)
gf = graphics('barplot',ct.df,vect,'f1')
gf = graphics('boxplot',ct.df,vect,'f2')
"""






