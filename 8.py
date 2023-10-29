import pandas as pd

dataFrame = pd.read_csv('algumarquivo.csv')

semValor = dataFrame.isna()

if semValor == True:
    dataFramePreenchido = dataFrame.fillna(0)