nome = 'Rogerio'
print(nome, type(nome))
idade = 29  # int
altura = 1.92  # float
e_maior = idade > 18  # bool
peso = 106
imc = peso/(altura**2)

print(nome, 'tem', idade, 'de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')  # f strings (format strings);
# dessa forma pode-se usar as variáveis entre chaves nas aspas;
# para formatar casas decimais, usa-se :.2f ou o número de casas desejadas;
print('{0} tem {1} anos e seu imc é {2}'. format(nome, idade, imc))  # pode numerar e reutilizar na string;
