#!/usr/bin/env python
# coding: utf-8

# # Análise dos Microdados da Vacina do Covid-19

# In[2]:


import pandas as pd
import matplotlib

#para pegar a os microdados das vacinas aplicadas 
microdadosVacina = pd.read_csv("C:\\Users\\diogo\\Downloads\\vacinados.csv", sep=";", encoding='utf-8')
microdadosVacina


# In[5]:


microdadosVacina = microdadosVacina.drop(columns=['cpf','nome','grupo','vacina','lote','data_vacinacao','sexo',])
microdadosVacina.head()


# In[6]:


#tirando os valores
micro = microdadosVacina.dropna()


# In[7]:


#separando para trabalhar apenas com as colunas de local de vacinaçao e a dose aplicada
colunasSelecionadas_LocaisVacinas = ['local_vacinacao']
colunasSelecionadas_DosesVacinas = ['dose']
microdadosVacina_Locais = microdadosVacina.filter(items = colunasSelecionadas_LocaisVacinas)
microdadosVacina_Doses = microdadosVacina.filter(items = colunasSelecionadas_DosesVacinas)


# In[8]:


#fazendo a contagem para ver quantos locais de vacinaçao tem e quantas doses foram aplicadas em cada local
microdadosVacina_Locais.value_counts()


# In[9]:


#fazendo a contagem da distribuiçao de quantas vacinas foram aplicadas de cada dose
microdadosVacina_Doses.value_counts()


# In[13]:


#grafico de histograma da quantidade de doses
microdadosVacina_Doses.hist()


# In[15]:


#descobrindo a porcentagem de quantas pessoas tomaram cada dose
distInDoses = microdadosVacina_Doses.value_counts()
percentInDoses = [100*x/distInDoses.sum() for x in distInDoses]
print(percentInDoses)


# In[2]:





# In[2]:





# In[2]:





# In[ ]:




