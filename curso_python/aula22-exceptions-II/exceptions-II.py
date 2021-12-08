try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    try:
        print(num1/num2)
    except ZeroDivisionError:
        print('Não se pode dividir por zero!!')
except ValueError:
    print('Digite apenas números inteiros.')
finally:
    print('Programa finalizado')
