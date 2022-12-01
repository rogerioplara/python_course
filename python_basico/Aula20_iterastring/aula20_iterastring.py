#  Índices
#        0123456789.......................33
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
print(tamanho_frase)

#  deve haver uma variável de controle em para o while

entrada = input('Qual letra deseja colocar maiúscula: ')

contador = 0  # contador do loop while
nova_string = ''  # nova string a ser iterada

while contador < tamanho_frase:  # passa pela string em todos seus elementos
    # print(frase[contador], contador) - conta e monta a frase
    letra = frase[contador]  # variável que vai receber cada letra em cada iteração para comparação
    if letra == entrada:  # condição de comparação
        nova_string += entrada.upper()  # coloca maiúsculo a letra indicada pelo usuário
    else:
        nova_string += letra  # mantém o restante em letras minúsculas
    contador += 1  # aumenta 1 a cada passagem do contador até encontrar o valor do índice

print(nova_string)
