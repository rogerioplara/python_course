secreto = input('Digite uma palavra para ser adivinhada: ')
digitadas = []  # lista vazia para receber as tentativas
chances = 3

while True:
    # condição para verificar se existem chances restantes
    if chances <= 0:
        print('Você perdeu :(')
        break

    # capta o input do usuário
    letra = input('Digite uma letra: ')

    # verifica se o que foi digitado é somente um caracter
    if len(letra) > 1:
        print('Ahhh, isso não vale, digite apenas uma letra.')
        continue

    # adiciona à lista todas as letras digitadas
    digitadas.append(letra)

    # se a letra estiver na palavra secreta, deixa armazenado na lista
    if letra in secreto:
        print(f'UHUL, a letra "{letra}" existe na palavra secreta.')
    else:  # se não, tira uma chance e deleta a letra da lista com o .pop
        print(f':( a letra {"letra"} NÃO está na palavra secreta.')
        chances -= 1
        print(f'Você tem mais {chances} chance(s).')
        digitadas.pop()

    # variável que vai armazenar a palavra correta
    secreto_temporario = ''
    # iteração sobre a lista para verificar se a letra está na palavra a ser adivinhada
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    # condição de final de jogo, fecha o loop caso a condição seja atendida
    if secreto_temporario == secreto:
        print(f'Que legal! Você acertou!!! A palavra era {secreto_temporario}.')
        break
    else: # para toda iteração, será mostrada essa mensagem com a palavra sendo atualizada em caso de acerto
        print(f'A palavra secreta está assim: {secreto_temporario}')
        print()
