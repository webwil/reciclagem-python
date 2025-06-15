# Exercício 23: Calculadora Simples
'''
Desenvolva uma calculadora simples que aceite duas entradas 
numéricas e um operador (+, -, *, /) do usuário. 
Use try-except para lidar com divisões por zero e 
entradas não numéricas. Utilize if-elif-else para realizar a 
operação matemática baseada no operador fornecido. Imprima o 
resultado ou uma mensagem de erro apropriada.
'''
try:
    num1 = float(input("digite o primeiro numero: "))
    num2 = float(input("digite o segundo numero: "))
    operador = input("Digite o operador (+, -, *, /): ")
    resultado = 0
    
    if operador == '+':
        resultado = num1 + num2
    if operador == '-':
        resultado = num1 - num2
    if operador == '*':
        resultado = num1 * num2
    if operador == '/':
        resultado = num1 / num2
    else:
        print("Operador inválido ou divisão por zero.")
    print(f"Resultado: {resultado}")
except ValueError:
    print("Erro: Entrada inválida. Certifique-se de inserir números.")