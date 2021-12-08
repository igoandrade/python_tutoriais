# captura ou controle de exceções

try:
    print(8/0)
except ZeroDivisionError:
    print('Não se pode dividir por zero.')