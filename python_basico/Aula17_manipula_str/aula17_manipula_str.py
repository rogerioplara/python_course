"""
Manipulando strings
* string indicies
* fatiamento de strings [inicio:fim:passo]
* funções build-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.
"""
# cada letra representa um índica em uma string:
# exemplo: 'Python s2' = [012345678] (positivos)
texto = 'Python_s2'
print(texto[0])

# indices negativos: 'Python s2' = [-9-8-7-6-5-4-3-2-1]
print(texto[-1])  # mostra o ultimo
url = 'www.goggle.com.br/'
print(url[:-1])  # tira o último character (fatiamento)

nova_string = texto[2:6]  # o caracter final não é incluído
print(nova_string)
nova_nova_string = texto[:6]  # define do começo da string até o quinto caracter
print(nova_nova_string)
new = texto[7:]  # define do caracter 7 até o fim da string
print(new)
new_string = texto[-9]
print(new_string)
new_new = texto[-9:-3]
print(new_new)

new_str = texto[0:6:2]  # inicio do recorte:fim do recorte:passo
print(new_str)
new_str = texto[::2]  # se deixar vazio, vai até o fim da string pulando de 2 em 2
print(new_str)

print(len(texto))

for letra in texto:  # imprime todos os índices em cada iteração por linha
    print(letra)
