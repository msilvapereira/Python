# Objetivos da aula 

# 1. Se aprofundar nas sintaxes básicas;
# 2. Aprender a utilizar as condicionais;
# 3. Aprender a utilizar os operadores lógicos; 
 
    # Diz qual valor é maior A, B ou C

#a = int(input('Primeiro valor: '))
#b = int(input('Segundo valor: '))
#c = int(input('Terceiro valor: '))

#a condicional é o "if" e o nosso operador lógico é o "and", ele diz qual número é maior

#if a > b and a > c:
#    print('o maior número é: {}'.format(a))
#elif b > a and b >c:
#    print('o maior número é: {}'.format(b))
#else:
#    print('o maior número é: {}'.format(c))
#print('final do programa')

    # Irá dizer se um dos números digitados é par ou não

#a = int(input('Entre com o primeiro valor: '))
#b = int(input('Entre com o segundo valor: '))
#resto_a = a % 2
#resto_b = b % 2

#OR faz o código dizer se A ou B é par, ele diz se um deles é par ou não

#NOT diz se a operação não é verdadeira, este operador inverte a condição
#não é mais se isso for verdadeiro e sim se isso foi uma mentira, uma falsa afirmação

#if resto_a == 0 or not resto_b > 0:
#    print('Foi digitado um número par')
#else:
#    print('Nenhum número par foi digitado')

    # Vai pedir 4 notas para o usuário e depois irá dar sua média, e irá validar se a nota foi digitada corretamente

#a = int(input('Primeiro bimestre: '))
#b = int(input('Segundo bimestre: '))
#c = int(input('Terceiro bimestre: '))
#d = int(input('Quarto bimestre: '))
#media = (a + b + c + d) / 4

#if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#    print('Media: {}'.format(media))
#else:
#    print('\nFoi informada alguma nota errada\n')

    # Irá validar a nota assim que ela for digitada

a = int(input('Primeiro bimestre: '))
if a >= 10:
    a = int(input('Você digitou uma nota errada. Digite novamente...\n\nPrimeiro bimestre: '))
b = int(input('Segundo bimestre: '))
if b >= 10:
    b = int(input('Você digitou uma nota errada. Digite novamente...\n\nSegundo bimestre: '))
c = int(input('Terceiro bimestre: '))
if c >= 10:
    c = int(input('Você digitou uma nota errada. Digite novamente...\n\nTerceiro bimestre: '))
d = int(input('Quarto bimestre: '))
if d >= 10:
    d = int(input('Você digitou uma nota errada. Digite novamente...\n\nQuarto bimestre: '))
media = (a + b + c + d) / 4
print('Media: {}'.format(media))
