from random import randint

computador = randint(0,10)

print('-=' * 17)
print('Bem-vindo ao jogo da advinhação!')
print('-=' * 17)
user = int(input('Digite o número que você acha que eu pensei: '))

if user == computador:
    print('Parabéns! você acertou!')
else:
    print('Errooooooooooooouuuuuuuuu!!!!!, eu pensei no número: {}'.format(computador))

    if user >10:
        print('Digite um número de 1 A 10!')
