import random


def gerar():
    print('Será gerado um número de 1 até 100')
    return random.randint(1,100)

def jogo():
    resposta = gerar()
    tentativas = 0

    print('Número gerado!')
    
    numero = False
    chute = 0

    while numero == False:
        while chute is not resposta:
            
            tentativas +=1
            chute = input('Qual o número? ')

            try:
                chute = int(chute)

                if chute > resposta:
                    print('Errou! O número é um valor menor que ', chute)
                
                elif chute < resposta:
                    print('Errou! O número é um valor maior que ', chute)
                
                else:
                    print('Parabéns! O número gerado foi ', resposta,
                          'Você acertou em ', tentativas, 'tentativas!')
                    numero = True
                
            except:
                print('Número inválido. Favor digitar apenas números inteiros')


while True:
    jogo()
    
    novamente = input('Deseja jogar novamente? (S ou N) ').lower()
    
    if novamente == 'n':
        break
    
print('Jogo finalizado')
