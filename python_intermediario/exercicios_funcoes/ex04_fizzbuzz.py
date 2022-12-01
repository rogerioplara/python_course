"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz. Se o parâmetro da função for divisível por
5, retorne buzz. Se o parâmetro da função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.
"""
final = int(input('Digite até qual número deseja "brincar" de FizzBuzz: '))


def fizzbuzz(a):
    if (a % 5 == 0) and (a % 3 == 0):
        return f'FizzBuzz - {a} é divisível por 3 e 5'
    if a % 5 == 0:
        return f'Buzz - {a} é divisível por 5'
    if a % 3 == 0:
        return f'Fizz - {a} é divisível por 3'
    return a


b = range(1, final + 1)
for n in b:
    print(fizzbuzz(n))
print()


# Outra maneira de resolver com operadores ternários - if de uma linha
# Utilizando valores Booleanos
def fb(x):
    fizz = True if x % 3 == 0 else False  # fizz é verdadeiro se x % 3 == 0
    buzz = True if x % 5 == 0 else False  # buzz é verdadeiro se x % 5 == 0
    return f'FizzBuzz {x}' if fizz and buzz else f'Fizz {x}' if fizz else f'Buzz {x}' if buzz else x
#   retorna fizzbuzz se             ;  se fizz for verdadeiro;      se buzz for verdadeiro ; se tudo for falso
#   fizz e buzz forem verdadeiros   ;  retorna fizz          ;      retorna buzz           ; retorna o número x


c = range(1, final + 1)
for p in c:
    print(fb(p))
