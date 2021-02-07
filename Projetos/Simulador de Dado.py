from random import randint
print('=' * 20)
print('SIMULADOR DE DADO')
print('=' * 20)
print('Função: escolher aleatoriamente um número de 1 a 6, tal como um dado.')
print()

while True:
    pergunta = str(input('Você quer jogar o dado?[Sim/Não] ')).upper().strip()[0]
    while pergunta not in 'SN':
        print('Resposta inválida! Tente novamente.')
        pergunta = str(input('Você quer jogar o dado?[Sim/Não] ')).upper().strip()[0]
    if pergunta == 'S':
        print(randint(1,6))
    else:
        break
    parada = str(input('Deseja jogar o dado novamente?[Sim/Não] ')).upper().strip()[0]
    while parada not in 'SN':
        print('Resposta inválida! Tente novamente.')
        parada = str(input('Deseja jogar o dado novamente?[Sim/Não] ')).upper().strip()[0]
    if parada == 'S':
        while parada not in 'N':
            print(randint(1, 6))
            parada = str(input('Deseja jogar o dado novamente?[Sim/Não] ')).upper().strip()[0]
            while parada not in 'SN':
                print('Resposta inválida! Tente novamente.')
                parada = str(input('Deseja jogar o dado novamente?[Sim/Não] ')).upper().strip()[0]
            if parada == 'N':
                break
        break
    break

print()
print('Simulador de dado encerrado!')
