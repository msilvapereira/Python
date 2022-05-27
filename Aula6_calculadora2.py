#Continuação da Aula 06 com a mesma fórmula de calculadora, mas nesta serão feitas alterações
#Caso queira continuar tendo a classe sem instanciar os objetos

class Calculadora:
    #como não vamos inicializar nada, o método init não é necessário
#    def __init__(self): #o init não pode ser vazio, por isso colocamos um pass, ele não faz nada, serve para não ficar vazio, mas também pode ser feito sem o init
#        pass 

    def soma (self, valor_a, valor_b): 
        return valor_a + valor_b

    def subtracao (self, valor_a, valor_b): 
        return valor_a - valor_b

    def multiplicacao (self, valor_a, valor_b): 
        return valor_a * valor_b

    def divisao (self, valor_a, valor_b): 
        return valor_a / valor_b

#dentro dos parenteses se informa os valores que você quer atribuir para valor_a e valor_b
#ao invés de instanciar um valor, se passa os valores em todas as operações

calculadora = Calculadora()
print(calculadora.soma(10, 2))
print(calculadora.subtracao(5, 3))
print(calculadora.multiplicacao(10, 5))
print(calculadora.divisao(100, 2))    
