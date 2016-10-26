from sklearn.neural_network import MLPRegressor as mlpr
import pandas as pd
dateparse = lambda dates: pd.datetime.strptime(dates, '%m/%Y')
df = pd.read_csv('dataBase.csv', sep = ",", skip_blank_lines=False, index_col='mom', infer_datetime_format = dateparse)



