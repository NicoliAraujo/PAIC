import pandas as pd
import numpy as np
"""
def anomaly(average, vect):
    vet = []
    for i in range(len(vect)):
        vet.append(vect[i]/100-average)
    return vet

def anomaly1(average, vect):
    vet = []
    for i in range(len(vect)):
        vet.append(vect[i]-average)
    return vet

def average(df):
    return df.mean()

def anomalia(vect):
    s = 0
    for i in range(0,len(vect)):
        if(type(vect[i])==float):
            s = s + vect[i]
    media = s/len(vect)
    print(media)
    vet = []
    for i in range(len(vect)):
        if(type(vect[i])==float):
            vet.append(vect[i]-media)
        else:
            vet.append("")
    return vet


dic = {}
df = pd.read_csv('nino.csv', sep = "\t")
ind = list(df.MOM)
vet = []
for i in range(0,df.shape[0]):
   vet.append(df.NINO12[i].astype(np.float))
vet1 = []
for i in range(0,df.shape[0]):
   vet1.append(df.NINO12A[i].astype(np.float))
vet2 = []
for i in range(0,df.shape[0]):
   vet2.append(df.NINO3[i].astype(np.float))
vet3 = []
for i in range(0,df.shape[0]):
   vet3.append(df.NINO3A[i].astype(np.float))
vet4 = []
for i in range(0,df.shape[0]):
   vet4.append(df.NINO34[i].astype(np.float))
vet5 = []
for i in range(0,df.shape[0]):
   vet5.append(df.NINO34A[i].astype(np.float))
vet6 = []
for i in range(0,df.shape[0]):
   vet6.append(df.NINO34[i].astype(np.float))
vet7 = []
for i in range(0,df.shape[0]):
   vet7.append(df.NINO34A[i].astype(np.float))
vet8 = []
for i in range(0,df.shape[0]):
   vet8.append(df.CHEIA[i].astype(np.float)/100)
av = average(df.CHEIA)/100
vet9 = anomaly(av,df.CHEIA)

vet10 = []
for i in range(0,df.shape[0]):
    if((type(df.TEMPMINM[i]) == str) and (len(df.TEMPMINM[i])>0)):
        vet10.append(float(df.TEMPMINM[i].replace(",",".")))
    else:
        vet10.append("")
vet11 = anomalia(vet10)

vet12 = []
for i in range(0,df.shape[0]):
    if((type(df.TEMPMAXM[i]) == str) and (len(df.TEMPMAXM[i])>0)):
        vet12.append(float(df.TEMPMAXM[i].replace(",",".")))
    else:
        vet12.append("")
vet13 = anomalia(vet12)

vet14 = []
for i in range(0,df.shape[0]):
   vet14.append(df.PRECACUM[i].astype(np.float))
av = average(df.PRECACUM)
vet15 = anomaly1(av,df.PRECACUM)

dic = {'nino12':vet,'nino12a':vet1,'nino3':vet2,'nino3a':vet3,'nino34':vet4,
       'nino34a':vet5,'nino4':vet6,'nino4a':vet7,'cheia':vet8,'cheiaa':vet9,
       'tminmed':vet10,'tminmeda':vet11,'tmaxmed':vet12,'tmaxmeda':vet13,
       'precacum':vet14,'precacuma':vet15}
dv = pd.DataFrame(dic, index = ind)
dv.index.name = 'mom'
dv.to_csv("dataBase.csv")
"""
dateparse = lambda dates: pd.datetime.strptime(dates, '%m/%Y')
df = pd.read_csv('dataBase.csv', sep = ",", skip_blank_lines=False, index_col='mom', infer_datetime_format = dateparse)
print(df)

