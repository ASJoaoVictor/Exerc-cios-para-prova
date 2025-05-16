from math import ceil

def q1():
    """
    Escreva um programa que solicite ao usuário um número e
    verifique se ele é par ou ímpar. Imprima uma mensagem informando o 
    resultado.
    """
    num = int(input("Digite um número: "))

    if num % 2 == 0:
        print("Par")
    else:
        print("Impar")
    pass


def q2():
    """
    Dada a string use o operador de fatiamento para imprimir somente a metade final
    Para 'abcdef, imprima: 'def'
    Para 'texto', imprima 'to'

    """
    texto = input("Digite um texto: ")

    metade = ceil(len(texto)/2)
    print(texto[metade:])

    pass

def q3():
    """
    Leia um número da entrada e imprima todos os 10 primeiros múltiplos dele na mesma linha
    """
    num = int(input("Digite um número: "))

    cont = 0
    i = 1
    while(cont < 10):
        if(i % num == 0):
            print(i, end=" ")
            cont += 1
        i+=1
    pass


def q4():
    """
    Escreva um programa que solicite ao usuário para digitar seu nome em letras
    minúsculas e, em seguida, imprima o nome com a primeira letra em maiúscula. Você
    não deve usar o método str.capitalize(). Preposições não devem ser iniadas com maiúsculo
    Exemplo: 
     - romulo junior - Romulo Junior
     - ze da manga - Ze da Manga
    """
    nome_completo = input("Digite seu nome: ").split()
    nome_atualizado = ""
    for nome in nome_completo:
        if(nome == "da" or nome =="de"):
            nome_atualizado += f"{nome} "
        else:
            nome_atualizado += f"{nome[0].upper()}{nome[1:]} "
    
    print(nome_atualizado[0:len(nome_atualizado)-1])
    pass
         
"""     for i in range(0, len(nome_completo)):
        if(nome_completo[i] == "de" or nome_completo[i] == "da"):
            print(nome_completo[i], end="")
        else:
            print(f"{nome_completo[i][0].upper()}{nome_completo[i][1:]}", end="")

        if(i != len(nome_completo)-1):
            print(end=" ")
    print("") """

def q5():
    """
    Verificação de Triângulo: Peça ao usuário o comprimento de três lados em uma única entrada
    e verifique se eles podem formar um triângulo. 
    Se sim, determine se é um triângulo equilátero, isósceles ou escaleno.
    Exemplo:
        333: equilátero
        322: isosceles
        234: escaleno
    """
    lados = input("Digite os valores dos lados: ")

    if(lados[0] == lados[1] and lados[2] == lados[1]):
        print("equilátero")
    elif(lados[0] == lados[1] or lados[1] == lados[2] or lados[2] == lados[0]):
        print("isósceles")
    else:
        print("escaleno")

    pass

def q6():
    """Periodicamente as crianças brasileiras devem tomar vacinas que as protegem de diversas doenças. 
    Escrever um programa para ler o ano em que a criança toma a 1a dose e a periodicidade (intervalo em anos) da vacina e exibir em que outros anos a criança deve tomar as próximas doses desta vacina, sabendo que são 4(quatro) doses ao total.

    Veja abaixo os exemplos de entrada e saída esperadas."""
    ano = int(input("Digite o ano da primeira dose: "))
    periodo = int(input("Digite periodicidade da vacina: "))

    for i in range(0, 4):
        ano += periodo
        print(f"{ano}", end=" ")
    pass

def q7():
    """Faça um programa que leia uma sequencia de números e indique se eles são primos ou não.  Você deve parar ao ler o número -1."""

    num = int(input("Digite um número: "))
    while(num != -1):
        controle = 0
        for i in range(2, num+1):
            if(num % i == 0):
                controle += 1
                
        if(0 < controle < 2):
            print("Primo")
        else:
            print("Não")

        num = int(input("Digite um número: "))
    pass

def q8():
    """Valquíria trabalha em uma padaria e foi roubada ontem. Seus clientes ficaram com pena e resolveram organizar uma vaquinha para comprar um novo 
    celular para ela. Escreva um programa que receba como entrada o valor doado por cada cliente, até que seja informado um valor negativo, 
    e exiba o total arrecadado e o valor médio doado por eles."""

    doacao = float(input("Digite o valor da doação: "))
    total = 0
    i = 0
    media = 0
    while(doacao >= 0):
        i += 1
        total += doacao
        media = total/i
        doacao = float(input("Digite o valro da doação: "))
    print(f"{total:.2f}\n{(media):.2f}")
    pass

def q9():
    pass

def q10():
    pass

if __name__ == "__main__":
    q7()