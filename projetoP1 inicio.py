import pandas as pd
import random


p = 0.01

df = pd.read_csv(
    'vacinados.csv',
    header=0,
    encoding = "UTF-8",
    skiprows=lambda i: i > 0 and random.random() > p,
    sep=';'
)

df