    # Objetivos da aula  

# 1. Se aprofundar nas sintaxes básicas;
# 2. Aprender a utilizar laços de repetição;
# 3. Criar programas com condicional e laço de repetição;

    #imprime na tela todos os numeros primos

#a = int(input('entre com um valor: '))
#for num in range(a+1):
#    div = 0
#    for x in range(1, num+1):
#        resto = num % x
#        #print(x, resto)
#        if resto == 0:
#           div += 1
#
#   if div == 2:        
#        print(num)

    #te diz se determinado numero é primo ou nao 

#a = int(input('entre com um numero: '))

#div = 0
#for x in range(1, a+1):
#    resto = a % x
#    print(x, resto)
#    if resto == 0:
#        div += 1

#if div == 2:        
#    print('numero {} é primo'.format(a))
#else:
#    print('numero {} não é primo'.format(a))

#a = 0
#while a <= 10: #imprimi os numeros menores ou iguais a 10 na tela
#    print(a)
#    a += 1

    #ele vai ficar repetindo: 'Nota invalida. Entre com a nota correta: ' até o usuário digitar uma nota menor ou igual a 10.

#nota = int(input('entre com uma nota: '))
#while nota > 10:
#    nota = int(input('Nota invalida. Entre com a nota correta: '))
#print(nota)

a = int(input('Primeiro bimestre: '))
while a > 10:
    a = int(input('Você digitou uma nota errada. Digite novamente...\n\nPrimeiro bimestre: '))
b = int(input('Segundo bimestre: '))
while b > 10:
    b = int(input('Você digitou uma nota errada. Digite novamente...\n\nSegundo bimestre: '))
c = int(input('Terceiro bimestre: '))
while c > 10:
    c = int(input('Você digitou uma nota errada. Digite novamente...\n\nTerceiro bimestre: '))
d = int(input('Quarto bimestre: '))
while d > 10:
    d = int(input('Você digitou uma nota errada. Digite novamente...\n\nQuarto bimestre: '))
media = (a + b + c + d) / 4
print('Media: {}'.format(media))
