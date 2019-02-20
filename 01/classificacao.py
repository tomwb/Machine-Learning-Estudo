# variavel = [gordo, pernas curtas, late]
porco1 = 	[1, 1, 0]
porco2 = 	[1, 1, 0]
porco3 = 	[1, 1, 0]
cachorro1 = [1, 1, 1]
cachorro2 = [0, 1, 1]
cachorro3 = [0, 1, 1]

dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]

marcacoes = [1, 1, 1, -1, -1, -1]

from sklearn.naive_bayes import MultinomialNB

modelo = MultinomialNB()
modelo.fit(dados, marcacoes)

misterioso  = [1, 1, 1]
misterioso2 = [1, 0, 0]
misterioso3 = [0, 0, 1]

testes = [misterioso, misterioso2, misterioso3]
marcacoes_teste = [-1, 1, -1]

resultados = modelo.predict(testes)
print(resultados)
diferencas = resultados - marcacoes_teste
print(diferencas)

acertos = [d for d in diferencas if d==0]
total_de_acertos = len(acertos)
total_de_elementos = len(testes)

taxa_de_acertos = 100 * total_de_acertos / total_de_elementos
print(taxa_de_acertos)