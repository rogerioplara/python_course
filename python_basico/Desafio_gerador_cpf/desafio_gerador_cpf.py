"""
CPF = 168.995.350-90 -> gerado para testes
---------------------------------------------------------------
1 * 10 = 10                 #   1 * 11 = 11 <-
6 * 9 = 54                  #   6 * 10 = 60
8 * 8 = 64                  #   8 * 9 = 72
9 * 7 = 63                  #   9 * 8 = 72
9 * 6 = 54                  #   9 * 7 = 63
5 * 5 = 25                  #   5 * 6 = 30
3 * 4 = 12                  #   3 * 5 = 15
5 * 3 = 15                  #   5 * 4 = 20
0 * 2 = 0                   #   0 * 3 = 0
        297                 #-> 0 * 2 = 0
                            #           343
11 - (297 % 11) = 11        #   11 - (343 % 11) = 9
11 > 9 = 0                  #
Digito 1 = 0                #   Digito 2 = 9

Se o resultado do MOD for maior do que 9, o DÍGITO vira 0
"""
from random import randint
numero = str(randint(10000000000, 99999999999))  # gera um número aleatório dentro do intervalo definido
cpf = numero
# única mudança feita do código do validador, gera um novo número aleatório e gera os dois dígitos
# sempre será verdadeiro matematicamente, pois não existe comparação com o input do validador


novo_cpf = cpf[:-2]  # fatia a string tirando os dígitos
sum1 = 0  # inicia as variáveis que receberão a multiplicação dos valores
sum2 = 0

# Loop de leitura da string (p) e de contagem 10 .. 2 (r)
for p, r in enumerate(range(10, 1, -1)):
    sum1 += (int(novo_cpf[p]) * int(r))  # soma da multiplicação de cada índice do cpf (p) pela contagem 10 .. 2 (r)
    digito_1 = 11 - (sum1 % 11)  # fórmula de validação / geração do primeiro dígito

if digito_1 > 9:  # checagem de validação do dígito 1
    digito_1 = 0
novo_cpf += str(digito_1)  # inserção do dígito encontrado no novo cpf

for p, r in enumerate(range(11, 1, -1)):  # loop igual ao anterior, porém com o dígito encontrado a mais
    sum2 += (int(novo_cpf[p]) * int(r))
    digito_2 = 11 - (sum2 % 11)
if digito_2 > 9:
    digito_2 = 0
novo_cpf += str(digito_2)

print(f'CPF gerado: {novo_cpf}')
