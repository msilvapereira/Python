    # Objetivos da aula

# 1. Aprender sobre listas
# 2. Aprender sobre tuplas
# 3. Aplicabilidade de listas e tuplas

#lista = [12, 10, 7, 5]
#lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']
#nova_lista = lista_animal * 3
#print(nova_lista)
#print(lista_animal) #imprime todos os componentes da lista
#print(lista_animal[1]) #usado quando se quer imprimir um componente só da lista, se diz a posição dele para o mesmo ser impresso na tela

#ordenando a lista

#lista.sort() #ordena a lista por ordem decrescente
#lista_animal.sort() #ordena a lista por ordem alfabética 
    #imprime a lista ordenada
#print(lista) 
#print(lista_animal)
#lista_animal.reverse() #faz o reverse da lista, ordena a lista de forma reversa, de rás para frente
#print(lista_animal) #imprime a lista organizada de forma reversa

    #é possível multiplicar uma lista

#Ex:

#lista_animal = ['gato', 'cachorro', 'elefante']
#nova_lista = lista_animal * 3
#print(nova_lista)

    #faz a soma dos itens da lista de numeros inteiros

#soma = 0
#for x in lista_animal:
#    print(lista)
#    soma = lista
#print(soma)

#print(sum(lista)) #outra forma de se fazer a soma dos conteudos da lista
#print(max(lista)) #imprime o maior valor que tem na lista
#print(min(lista)) #imprime o maior valor que tem na lista

#print(max(lista_animal)) #imprime a palavra de maior "valor", ou seja, gato pois ela começa com a letra G que é a letra maior
#print(min(lista_animal)) #imprime a palavra de menor "valor", ou seja, cachorro pois ela começa com a letra C que é a letra menor

    #é possível validar se um valor existe na lista, utilizando condicional, isso diz se elemento já foi incluido na lista.

# Ex:

#if 'lobo' in lista_animal:     #irá procurar se existe o elemento 'gato' na lista_animal
#    print('Existe um lobo na lista')   #imprime na tela se existe o elemento 'gato'
#else:
#    print('nao existe um lobo na lista. Será incluído')   #imprime na tela se NÃO existe o elemento 'gato'
#    lista_animal.append('lobo') #inclui o elemento lobo na lista
#    print(lista_animal)

#lista_animal.pop() #ele retira sempre o último item da lista, como não utiliza parâmetro nenhum, ele retira o último n°
# lista_animal.pop(0) #ele irá retirar o elemento que está na posição indicada (0) o cachorro

#lista_animal.remove('elefante') #remove o item listado dentro do parentese 
#print(lista_animal)

#Tuplas

lista = [12, 10, 7, 5]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

lista_animal[0] = 'macaco' #troca a posição 0 (cachorro) por macaco
print(lista_animal)

# TUPLA

tupla = (1, 10, 12, 14) #ao invés de colchetes, usa-se parenteses
print(tupla[2]) #imprime o que está no parametro designado, posiçaõ 2 - 12
print(len(tupla)) #retorna ao usuário a quantidade de elementos que tem na tupla, funciona também com listas

#a tupla é imutável, diferente da lista que é mutável, ou seja, é possível alterar valores, ordenar a lista, etc..

#é possível converter uma lista para uma tupla, e vice-versa

# Ex:
 
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)

lista_numerica = list(tupla) #converte a tupla para uma lista
print(type(lista_numerica)) 
print(lista_numerica) #imprime a tupla que foi convertida para uma lista

#após essa conversão é possível fazer alterações nela, tupla é usada para não fazer alterações, pois ela é imutável
#quando se quer mudar alguma informação de uma tupla é necessário converte-la para uma lista
