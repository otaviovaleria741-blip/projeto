# Calculadora — meu segundo programa
# Escreva o código embaixo:
print("===calculadora===")
while True:
    a = float(input("digite o primeiro numero: "))
    op = input("digite a operação (+, -, *, /): ")
    b = float(input("segundo numero: "))

    if op == "+":
        resultado = a + b
    elif op == "-":
        resultado = a - b
    elif op == "*":
        resultado = a * b
    elif op == "/":
        try:
            resultado = a / b
        except ZeroDivisionError:
            resultado = "erro: divisão por zero"
    else:
        resultado = "operação invalida"

    print(f"{a} {op} {b} = {resultado}")
    de_novo = input("deseja fazer outra operação? (s/n): ")
    if de_novo != "s":
        break
