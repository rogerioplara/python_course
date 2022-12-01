"""
Tipos de dados
str - string - textos 'assim' "assim"
int - inteiro - integer - 0123456789 -1 -2 -3 -4 -5
float - real - decimal/ponto flutuante - 0.1 -0.1, 1.5 -10.35
bool - booleano - lógico true/false - 10 == 10
"""
# type serve para retornar o tipo que está entre o parênteses;
print('Rogerio', type('Rogerio'))
print(10, type(10))
print(25.23, type(25.23))
print(10 == 10, type(10 == 10))  # == é um comparador;
print('L' == 'P', type('L' == 'P'))
print('L' == 'l', type('L' == 'l'))  # case sensitive: letras maiúsculas não são iguais às letras minúsculas;
print(bool(''))  # vazio é avaliado em falso, seja lista, aspas, ou zero;

# Conversão de tipos:
print('Luiz', type('Luiz'), bool('Luiz'))  # valor avaliado em TRUE, pois, não é vazio;
# Bool é utilizado para desvio de fluxo, IF / ELSE;

print('10', type('10'), type(int('10')))  # typecasting = conversão de tipos;
# Só funciona se o que estiver na conversão for realmente o tipo que deseja converter;

# Exercício

# Nome
print('Rogerio Peres Lara', type('Rogerio Peres Lara'))
# Idade
print(29, type(29))
# Altura
print(1.92, type(1.92))
# Maior de idade?
print(29 > 18, type(29 > 18))
