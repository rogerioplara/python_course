"""
Criar variáveis para nome, idade, altura e peso de uma pessoa;
criar variável com ano atual;
obter o ano de nascimento da pessoa baseado na idade e ano atual
obter imc da pessoa com 2 casas decimais
exibir um texto com toso os valores na tela usando f-strings
"""

nome = 'Rogerio'
idade = 29
altura = 1.92
peso = 106
ano = 2022
imc = peso / (altura**2)
nascimento = ano - idade

print(f'{nome} tem {idade} anos, {altura} de altura, pesa {peso}kg e seu imc é de {imc:.2f}.')
print(f'{nome} nasceu em {nascimento}.')
