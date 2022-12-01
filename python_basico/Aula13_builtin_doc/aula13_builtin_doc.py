num1 = input('Digite um número: ')
num2 = input('Digite um número: ')

# STRING METHODS
# isnumeric / isdigit / isdecimal

# checa números inteiros e positivos
print(num1.isnumeric())  # os dois podem ser convertidos para número inteiro, não funciona com negativos;
print(num2.isnumeric())

if num1.isdigit() and num2.isdigit():  # faz a checagem ANTES e converte depois, evita erros de tipagem;
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
else:
    print('Número(s) inteiros inválidos.')

try:  # TRY tenta executar, porém, se não for possível pula para EXCEPT;
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
except:
    print('ERROR')
