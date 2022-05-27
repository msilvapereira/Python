    # Objetivos da Aula

# 1. Aprender a utilização de métodos e funções no Python
# 2. Aprender a utilização de classes
# 3. Entender os motivos para se usar métodos, funções e classes
 
#def soma (a, b): #esse método é uma função que tem retorno, irá retornar a soma de a + b
#    return a + b

#def subtracao (a, b): #esse método retorna a subtração de a - b
#    return a - b

#def multiplicacao (a, b): #esse método retorna a multiplicação de a * b
#    return a * b

#def divisao (a, b): # esse método retorna a divisão de a / b
#    return a / b

#print('A soma é: {}'.format(soma(1, 2)))
#print('A soma é: {}'.format(soma(3,4)))
#print('A subtração é: {}'.format(subtracao(10, 2)))
#print('A multiplicação é: {}'.format(multiplicacao(10, 2)))
#print('A divisão é: {}'.format(divisao(10, 2)))

    #criando a classe calculadora, para colocar os métodos acima 
#a criação da classe permite que você acesse todas as operações sem ter que informar o valor novamente

class Calculadora:
    def __init__(self, num1, num2): #self serve para acessar os valores dentro da classe
        self.valor_a = num1
        self.valor_b = num2
        
    def soma (self): 
        return self.valor_a + self.valor_b

    def subtracao (self): 
        return self.valor_a - self.valor_b

    def multiplicacao (self): 
        return self.valor_a * self.valor_b

    def divisao (self): 
        return self.valor_a / self.valor_b

#instanciando uma classe
calculadora = Calculadora(10, 2)
print(calculadora.valor_a) #o self acessa o valor_a e imprime que é 10
print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.multiplicacao())
print(calculadora.divisao())
