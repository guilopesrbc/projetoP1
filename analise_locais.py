import pandas as pd
import matplotlib
matplotlib.use('TkAgg',force=True)
from matplotlib import pyplot as plt
#print("Switched to:",matplotlib.get_backend())
matplotlib.pyplot.show()

#para pegar a os microdados das vacinas aplicadas 
microdadosVacina = pd.read_csv("C:\\Users\\diogo\\Downloads\\vacinados.csv", sep=";", encoding='utf-8')

microdadosVacina.head() #para ver as 5 primeiras linhas dos dados


#separando para trabalhar apenas com as colunas de local de vacinaçao e a dose aplicada
colunasSelecionadas_LocaisVacinas = ['local_vacinacao']
colunasSelecionadas_DosesVacinas = ['dose']
microdadosVacina_Locais = microdadosVacina.filter(items = colunasSelecionadas_LocaisVacinas)
microdadosVacina_Doses = microdadosVacina.filter(items = colunasSelecionadas_DosesVacinas)

#fazendo a contagem para ver quantos locais de vacinaçao tem e quantas doses foram aplicadas em cada local - foram 311 locais diferentes
#print(microdadosVacina_Locais.value_counts())
#print(microdadosVacina_Doses.value_counts())

#grafico de histograma ta dando erro, ele ta printando no oterminal e nao ta saindo o grafico
#print(microdadosVacina_Doses.hist())

#descobrindo a porcentagem de quantas pessoas tomaram cada dose
print(microdadosVacina_Doses.value_counts())
distInDoses = microdadosVacina_Doses.value_counts()
percentInDoses = [100*x/distInDoses.sum() for x in distInDoses]
print(percentInDoses)