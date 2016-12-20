import pandas as pd
dateparse = lambda dates: pd.datetime.strptime(dates, '%m/%Y')
df = pd.read_csv('teste.csv', sep = ",", skip_blank_lines=False, index_col='mom', infer_datetime_format = dateparse)
"""
for i in range(1961,2015):
    for j in range(1,13):
        if(str(df.tmaxmed[str(j)+"/"+str(i)]) != "nan"):
            #print(df.tmaxmed[str(j)+"/"+str(i)])
            #print(True)
            pass
        else:
            print(i)
"""
vetA = []
ano = 1961
ind = [1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970,
       1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979,
       1981, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1992,
       1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001,
       2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
       2011, 2012, 2013]
while(ano<=2013):
    mes = 6
    vetB = []
    while(len(vetB)<12):
        try:
            if(str(df.tmaxmed[str(mes)+"/"+str(ano)]) != "nan"):
                aux = str(mes)+"/"+str(ano)
                vetB.append(aux)
                if(mes<12):
                    mes+=1
                else:
                    mes = 1
                    ano+=1
            else:
                if((mes>=6) and (mes<=12)):
                    ano+=1
                break
        except:
            ano+=1
            break
        
    if(len(vetB)==12):
        vetA.append(vetB)
cheia = []
nino12 = []
nino3 = []
nino34 =[]
nino4 = []
prec = []
tempMax = []
tempMin = []
result = []
for i in range(0,12):
    aux = []
    cheia.append(aux)
for i in range(0,12):
    aux = []
    nino12.append(aux)
for i in range(0,12):
    aux = []
    nino3.append(aux)
for i in range(0,12):
    aux = []
    nino34.append(aux)
for i in range(0,12):
    aux = []
    nino4.append(aux)
for i in range(0,12):
    aux = []
    prec.append(aux)
for i in range(0,12):
    aux = []
    tempMax.append(aux)
for i in range(0,12):
    aux = []
    tempMin.append(aux)

for i in range(0,48):
    result.append(float(df.cheia[vetA[i+1][0]]))
    for j in range(0,12):
        cheia[j].append(float(df.cheia[vetA[i][j]]))
for i in range(0,48):
    for j in range(0,12):
        nino12[j].append(float(df.nino12[vetA[i][j]]))
for i in range(0,48):
    for j in range(0,12):
        nino3[j].append(float(df.nino3[vetA[i][j]]))
for i in range(0,48):
    for j in range(0,12):
        nino34[j].append(float(df.nino34[vetA[i][j]]))
for i in range(0,48):
    for j in range(0,12):
        nino4[j].append(float(df.nino4[vetA[i][j]]))
for i in range(0,48):
    for j in range(0,12):
        prec[j].append(float(df.precacum[vetA[i][j]]))
for i in range(0,48):
    for j in range(0,12):
        tempMax[j].append(float(df.tmaxmed[vetA[i][j]]))
for i in range(0,48):
    for j in range(0,12):
        tempMin[j].append(float(df.tminmed[vetA[i][j]]))

print(cheia[0])

dic = {'cheia_6': cheia[0], 'cheia_7': cheia[1],
       'cheia_8': cheia[2], 'cheia_9': cheia[3],
       'cheia_10': cheia[4], 'cheia_11': cheia[5],
       'cheia_12': cheia[6], 'cheia_1': cheia[7],
       'cheia_2': cheia[8], 'cheia_3': cheia[9],
       'cheia_4': cheia[10], 'cheia_5': cheia[11],

       'nino12_6': nino12[0], 'nino12_7': nino12[1],
       'nino12_8': nino12[2], 'nino12_9': nino12[3],
       'nino12_10': nino12[4], 'nino12_11': nino12[5],
       'nino12_12': nino12[5], 'nino12_1': nino12[7],
       'nino12_2': nino12[8],'nino12_3': nino12[9],
       'nino12_4': nino12[10], 'nino12_5': nino12[11],

       'nino3_6': nino3[0], 'nino3_7': nino3[1],
       'nino3_8': nino3[2], 'nino3_9': nino3[3],
       'nino3_10': nino3[4], 'nino3_11': nino3[5],
       'nino3_12': nino3[6], 'nino3_1': nino3[7],
       'nino3_2': nino3[8], 'nino3_3': nino3[9],
       'nino3_4': nino3[10], 'nino3_5': nino3[11],

       'nino34_6': nino34[0], 'nino34_7': nino34[1],
       'nino34_8': nino34[2], 'nino34_9': nino34[3],
       'nino34_10': nino34[4], 'nino34_11': nino34[5],
       'nino34_12': nino34[6], 'nino34_1': nino34[7],
       'nino34_2': nino34[8], 'nino34_3': nino34[9],
       'nino34_4': nino34[10], 'nino34_5': nino34[11],

       'nino4_6': nino4[0], 'nino4_7': nino4[1],
       'nino4_8': nino4[2], 'nino4_9': nino4[3],
       'nino4_10': nino4[4], 'nino4_11': nino4[5],
       'nino4_12': nino4[6], 'nino4_1': nino4[7],
       'nino4_2': nino4[8], 'nino4_3': nino4[9],
       'nino4_4': nino4[10], 'nino4_5': nino4[11],

       'prec_6': prec[0], 'prec_7': prec[1],
       'prec_8': prec[2], 'prec_9': prec[3],
       'prec_10': prec[4], 'prec_11': prec[5],
       'prec_12': prec[6], 'prec_1': prec[7],
       'prec_2': prec[8], 'prec_3': prec[9],
       'prec_4': prec[10], 'prec_5': prec[11],

       'tempMax_6': tempMax[0], 'tempMax_7': tempMax[1],
       'tempMax_8': tempMax[2], 'tempMax_9': tempMax[3],
       'tempMax_10': tempMax[4], 'tempMax_11': tempMax[5],
       'tempMax_12': tempMax[6], 'tempMax_1': tempMax[7],
       'tempMax_2': tempMax[8], 'tempMax_3': tempMax[9],
       'tempMax_4': tempMax[10], 'tempMax_5': tempMax[11],

       'tempMin_6': tempMin[0], 'tempMin_7': tempMin[1],
       'tempMin_8': tempMin[2], 'tempMin_9': tempMin[3],
       'tempMin_10': tempMin[4], 'tempMin_11': tempMin[5],
       'tempMin_12': tempMin[6], 'tempMin_1': tempMin[7],
       'tempMin_2': tempMin[8], 'tempMin_3': tempMin[9],
       'tempMin_4': tempMin[10], 'tempMin_5': tempMin[11],

       'result': result

    }

#print(dic['prec_6'])

print(len(ind))
dv = pd.DataFrame(dic, index = ind)
dv.index.name = 'year'
dv.to_csv("dataBaseFinal.csv")

