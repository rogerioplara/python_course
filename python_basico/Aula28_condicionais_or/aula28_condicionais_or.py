nome = input('Qual o seu nome? ')

if nome:
    print(nome)
else:
    print('Você não digitou nada. ')

print(nome or 'Você não digitou nada.')  # se nome tiver um valor, o que foi digitado será impresso
#  Operador OR pode ser utilizado e vai parar na primeira expressão verdadeira
print(nome or None or False or 0 or 'Você não digitou nada' or 'Outra coisa')

print()

a = 0  # retorna falso
b = None  # retorna falso
c = False  # retorna falso
d = []  # retorna falso
e = {}  # retorna falso
f = 22  # retorna verdadeiro
g = 'Luiz'  # retorna verdadeiro

# var recebe o primeiro valor TRUE que encontrar dentre os operadores OR
var = a or b or c or d or e or f or g
print(var)

# Substitui tudo isso:
# if a:
#     var = a
# elif b:
#     var = b
# elif c:
#     var = c
# elif d:
#     var = d
# elif e:
#     var = e
# elif f:
#     var = f
# elif g:
#     var = g
# print(var)
