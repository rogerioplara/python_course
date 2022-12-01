"""
While / else
contadores
acumuladores
"""
contador = 1
acumulador = 0

while contador <= 10:
    print(contador, acumulador)
    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no else.')

print(acumulador)
print('Acabou!')
