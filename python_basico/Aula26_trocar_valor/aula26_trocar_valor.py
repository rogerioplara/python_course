"""
Como trocar valor de variáveis
"""
x = 10  # Luiz
y = 'Luiz'  # 10
z = 'Otávio'

# z = x
# x = y
# y = z
# print(f'x = {x} e y = {y}')
# em python existe uma forma muito mais simples de fazer essa troca

x, y, z = z, x, y  # forma de fazer em pyton
print(f'x = {x} e y = {y} e z = {z}')
