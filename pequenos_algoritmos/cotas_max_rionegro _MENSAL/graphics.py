import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os
dateparse = lambda dates: pd.datetime.strptime(dates, '%m/%Y')
df = pd.read_csv('dataBase.csv', sep = ",", skip_blank_lines=False, index_col='mom', infer_datetime_format = dateparse)
v1 = []
v2 = []
for i in range(1961,2015):
    for j in range(1,13):
        v1.append(j)
        v2.append(i)
df['ano'] = v2
df['mes'] = v1
#print(df)
aux = []
for i in range(1961,19881):
    aux.append(i)
grid = sns.FacetGrid(df, col = "ano", col_order = aux,col_wrap=5)
bp = grid.map(sns.barplot, "ano", "cheiaa", "mes")
bp.add_legend()
direct = os.getcwd()
sns.plt.savefig(direct + '/teste3.pdf')
                    
"""
sns.barplot(x = df.ano['1/1961':'12/1970']-1900, hue = df.mes['1/1961':'12/1970'], y = df.cheiaa['1/1961':'12/1970'], palette = 'Greys')
direct = os.getcwd()
sns.plt.savefig(direct + '/teste3.pdf')

"""
