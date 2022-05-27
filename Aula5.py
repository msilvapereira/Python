    # Objetivos da aula

# 1. Aprender sobre conjuntos
# 2. Aprender a manipular conjuntos
# 3. Aplicabilidade de conjuntos

conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8, 9}

conjunto_uniao = conjunto1.union(conjunto2) # reune tudo que tem no conjunto 1 com o que tem no conjunto 2
print('União: {}'.format(conjunto_uniao)) # imprime a união dos conjuntos

conjunto_interseccao = conjunto1.intersection(conjunto2) # irá mostrar a intersecção do conjunto e do conjunto2
print('Itersecção: {}'.format(conjunto_interseccao)) # imprime a intersecção

conjunto_diferenca1 = conjunto1.difference(conjunto2) # irá mostrar a diferença entre o conjunto 2 e do conjunto 1
conjunto_diferenca2 = conjunto2.difference(conjunto1)
print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca1)) #imprime a diferença
print('Diferença entre 2 e 1: {}'.format(conjunto_diferenca2))
conjunto_diff_simetrica = conjunto1.symmetric_difference(conjunto2)
print('Diferença simétrica: {}'.format(conjunto_diff_simetrica)) 

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
#conjunto_subset = conjunto_a.issubset(conjunto_b) #ele diz se o conjunto A é um subset do conjunto B, portanto retorna 'True' pq o 1, 2 e 3 esta dentro do conjunto B
conjunto_subset = conjunto_a.issubset(conjunto_b) #false, faltou o 4 e o 5 dentro do conjunto A para que ele seja um subset
print('A é subconjunto de B: {}'.format(conjunto_subset)) 
conjunto_superset = conjunto_b.issuperset(conjunto_a) 
print('B é um superconjunto de A: {}' .format(conjunto_superset)) #imprime 'True', pois o B tem os elementos do conjunto A oq faz dele um superset do conjunto A, o importante é que ele tenha os mesmos elementos do conjunto A

#convertendo uma lista para um conjunto

lista = ['cachorro', 'gato', 'gato', 'elefante']
conjunto_animais = set(lista) #conversão da lista. Obs: se você tem uma lista e quer tirar duplicidades a melhor opção é converte-la em conjuntos
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais) #converte novamente em lista

#conjunto = {1, 2, 3, 4}
#conjunto.add(5) # usado para adicionar elementos ao conjunto
#conjunto.discard(2) # remove um elemento do conjunto 
#print(conjunto)