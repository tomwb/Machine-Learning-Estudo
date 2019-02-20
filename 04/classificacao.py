from collections import Counter
import pandas as pd

df = pd.read_csv('04/busca.csv')

X_df = df[['home', 'busca', 'logado']]
Y_df = df['comprou']

Xdummies_df = pd.get_dummies(X_df)
Ydummies_df = Y_df

X = Xdummies_df.values
Y = Ydummies_df.values

porcentagem_de_treino = 0.8
tamanho_de_treino = int(porcentagem_de_treino * len(Y))
tamanho_de_teste = int(len(Y) - tamanho_de_treino)

treino_dados = X[:tamanho_de_treino]
treino_marcacoes = Y[:tamanho_de_treino]

teste_dados = X[-tamanho_de_teste:]
teste_marcacoes = Y[-tamanho_de_teste:]

from sklearn.naive_bayes import MultinomialNB
modelo = MultinomialNB()
modelo.fit(treino_dados, treino_marcacoes)

resultado = modelo.predict(teste_dados)
acertos = (resultado == teste_marcacoes)
 
total_de_acertos = sum(acertos)
total_de_elementos = len(teste_dados)
taxa_de_acerto = 100.0 * total_de_acertos / total_de_elementos

print("Taxa de acerto do algoritimo: %f" %taxa_de_acerto)
print(resultado)

# a eficacia do algoritimo que chuta tudo 0 ou 1
acerto_base = max(Counter(teste_marcacoes).values())
taxa_de_acerto_base = 100.0 * acerto_base / len(teste_marcacoes)
print("Taxa de acerto base: %f" % taxa_de_acerto_base)