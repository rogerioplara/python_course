"""
Iniciar com letra, pode conter números, separa por _, letras minúsculas;
"""
nome = 'Rogerio'
print(nome, type(nome))
idade = 29  # int
altura = 1.92  # float
e_maior = idade > 18  # bool
peso = 106
imc = peso/(altura**2)

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior de idade:', e_maior)

print(nome, 'tem', idade, 'de idade e seu imc é', imc)


idade = """40"""

print(idade, type(idade))
