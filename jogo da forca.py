# %%
import random

palavra = random.choice(['neymar', 'quincy promes', 'pogba'])
letras_corretas = []
letras_erradas = []
tentativas = 6

while tentativas > 0:
    palavra_formada = ''

    for letra in palavra:
        if letra in letras_corretas:
            palavra_formada = palavra_formada + letra
        else:
            palavra_formada = palavra_formada + '_'
    print(f'palavra: {palavra_formada}')

    if palavra_formada == palavra:
        print('parabens!, graças a Deus')
        break

    chute =str(input('digite uma letra:'))

    if len(chute) != 1:
        print('apenas uma letra')
        continue

    if chute in palavra:
        letras_corretas.append(chute)
    else:
        letras_erradas.append(chute)
        tentativas = tentativas - 1

