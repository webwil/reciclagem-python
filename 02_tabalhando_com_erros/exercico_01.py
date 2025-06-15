# Exercício 21: Conversor de Temperatura
'''
Escreva um programa que converta a temperatura de 
Celsius para Fahrenheit. O programa deve solicitar ao 
usuário a temperatura em Celsius e, utilizando try-except, 
garantir que a entrada seja numérica, tratando qualquer 
ValueError. Imprima o resultado em Fahrenheit ou uma mensagem 
de erro se a entrada não for válida.
'''

temperatura_celsius = float(input("Digite a temperatura em celsius: "))
resultado = 0
try:
    fahrenheit = (temperatura_celsius * 9/5) + 32
    resultado = f" {temperatura_celsius} graus Celsius é igual a {fahrenheit} graus Fahrenheit" 
except KeyboardInterrupt:
    resultado = "O programa foi enterrompido pelo usuario"

print(resultado)
    