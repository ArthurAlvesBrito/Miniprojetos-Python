from random import randint
a = randint(10, 30)
lista = list()
lista.append(a)

print('=' * 20)
print('JOGO DA ADIVINHAÇÃO')
print('=' * 20)
print('Objetivo: Adivinhar um número entre 10 e 30, escolhido aleatoriamente.')
print()

pergunta = int(input('Adivinhe o número: '))
while pergunta != a:
    if pergunta < a:
        print('Um pouco mais.')
        pergunta = int(input('Adivinhe o número: '))
    else:
        print('Um pouco menos')
        pergunta = int(input('Adivinhe o número: '))

print()
print('Parabéns!! Você adivinhou o número!!')
