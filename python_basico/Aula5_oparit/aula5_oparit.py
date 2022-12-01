"""
Operadores Aritméticos
+ Soma
- Subtração
* Multiplicação
/ Divisão
// Divisão inteira
** Exponenciação
% Resto (mod)
() Altera a precedência das contas
"""

print('Multiplicação =', 10 * 10)
print('Adição =', 10 + 10)
print('Subtração =', 10 - 10)
print('Divisão =', 10 / 3)
print('Divisão inteira =', 10 // 3)
print('Resto da divisão 10 % 3 =', 10 % 3)
print('Multiplicação de uma String =', 10 * '10')
print('Exponenciação =', 10**2)

print('Soma de strings (concatenação) =', '5' + '5')
print('Rogerio' + ' ' + 'Peres' + ' ' + 'Lara' + 'tem' + str(29) + 'anos')  # não será utilizado assim
print('Rogerio Peres Lara tem', 29, 'anos')

print('Precedência normal =', (5 + 2 * 10))
print('Precedência alterada =', ((5+2)*10))
