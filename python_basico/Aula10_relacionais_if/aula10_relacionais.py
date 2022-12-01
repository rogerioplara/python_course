"""
Operadores relacionais
== > >= < <= !=
"""

print(2 == 2)
print(2 == 1)
print(2 == '2')
print()
num_1 = 2
num_2 = '2'

print(num_1, num_2)  # imprime 2 2
print(num_1 == num_2)  # false
print()

num_3 = 3
num_4 = 3
exp_1 = num_3 == num_4
exp_2 = num_3 > num_4
exp_3 = num_3 >= num_4
exp_4 = num_3 < num_4
exp_5 = num_3 <= num_4
exp_6 = num_3 != num_4
print(exp_1)
print(exp_2)
print(exp_3)
print(exp_4)
print(exp_5)
print(exp_6)

nome = input('Qual o seu nome? ')
idade = int(input('Qual sua idade? '))  # não esquecer de converter o input;
idade_limite = 18
if (idade >= idade_limite) and (idade <= 120):
    print(f'{nome} tem {idade} anos, pode pegar o empréstimo!')
elif (idade < idade_limite) and (idade > 0):
    print(f'{nome} tem {idade} anos, NÃO pode pegar o empréstimo')
else:
    print('Idade inválida')

# Limite para pegar empréstimo
idade_menor = 20
idade_maior = 60

if (idade >= 20) and (idade <= idade_maior):
    print(f'{nome} tem {idade} anos e está dentro da categoria de trabalhador ativo.')
elif(idade <= 18) and (idade >= 7):
    print(f'{nome} tem {idade} anos e está dentro da categoria de formação.')
elif(idade < 7) and (idade > 0):
    print(f'{nome} tem {idade} anos e está dentro da categoria de pequena criança.')
elif(idade > idade_maior) and (idade <= 120):
    print(f'{nome} tem {idade} anos e está dentro da categoria de aposentado.')
else:
    print('Idade inválida')  # imprime duplicado devido ao primeiro else da linha 40;
