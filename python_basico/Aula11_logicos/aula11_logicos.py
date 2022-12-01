"""
Operadores lógicos
AND = só retorna verdadeiro se as 2 condições forem verdadeiras
OR = retorna verdadeiro se qualquer uma das 2 condições forem verdadeiras
NOT = inversor - zero é considerado um valor booleano falso
IN
NOT IN
"""
# EXEMPLO NOT
a = 2
b = 3
if not b > a:  # NOT inverte o valor da expressão
    print('B é maior que A')
else:
    print('A é maior que B')

# IN / NOT IN
print()

nome = input('Digite seu nome: ')
letra = input('Digite uma letra: ')

if letra in nome:  # IN compara se está contido ou não
    print(f'A letra {letra} está contida no seu nome')

if letra not in nome:  # NOT IN compara se não está contido no nome
    print(f'A letra {letra} não está contida no seu nome')

usuario = input('Nome de usuário: ')
senha = input('Senha de usuário: ')
usuario_bd = 'rogerio'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema!')
else:
    print('Usuário ou senha inválidos.')

num1 = 0
num2 = 0
if not num1 != num2:
    print('1')
else:
    print('2')
