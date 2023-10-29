import pandas as pd

dataFrame = pd.read_csv('algumarquivo.csv')

colunaEspecifica = dataFrame['Nome da coluna']

linhasFiltradas = dataFrame[dataFrame['salario'] > 1200]

