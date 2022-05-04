# Objetivos da aula 

# 1. Se aprofundar nas sintaxes básicas;
# 2. Aprender sobre variáveis em Python;
# 3. Realizar interações com o usuário; 

#a = 5
#b = 7
a = int(input('Entre com o primeiro valor:')) #para o código interagir com o usuário 
b = int(input('Entre com o segundo valor:')) 

soma = a + b
sub = a - b 
multi = a * b
div = a / b
resto = a % b

    #para somar uma string com um int, voce precisa primeiro converter esse int para string
    #utilizando o "print('soma: ' + str(soma))" eu transformei meu int em uma string

print('soma: ' + str(soma)) #imprimi uma string junto que no caso foi "soma: "
print('sub: ' + str(sub))
print('multi: ' + str(soma))
print(div)  #imprimi somente a string, ou seja, o resultado
print(resto)

    #obs: mas essa não é a melhor maneira para se imprimir uma string, o melhor é usar o comando format

print('soma: {} \nsub: {}'.format(soma, sub)) #comando que concatena, seja int, string ou qualquer outra coisa

    #tem o mesmo resultado do de cima

#print('soma: {soma}'
 #   '\nsub: {sub}'
  #  '\nmulti: {multi}'
   # '\ndiv: {div}'
    #'\nresto: {resto}'.format(soma=soma, sub=sub, multi=multi, div=div, resto=resto)) 

#da para colocar tudo isso dentro de uma variavel e pedir para imprimir apenas uma variavel

resultado = ('soma: {soma}'
    '\nsub: {sub}'
    '\nmulti: {multi}'
    '\ndiv: {div}'
    '\nresto: {resto}'.format(soma=soma, sub=sub, multi=multi, div=div, resto=resto)) 

print(resultado)

