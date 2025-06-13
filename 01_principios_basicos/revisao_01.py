
#INTEIROS (int)

# 1 - Escreva um programa que soma dois números inteiros inseridos pelo usuário.
primeiro_numero = int(input("Digite o primeiro numero: "))
segundo_numero = int(input("Digite o segundo numero: "))
soma = primeiro_numero + segundo_numero
print(f"A soma de {primeiro_numero} mais {segundo_numero} é {soma}")

# 2 - Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
numero = int(input("Digite o numero: "))
divisor = 5
divisao = numero % divisor
print(f"O resto da divisão de {numero} dividido po {divisor} é {divisao}")

# 3 - Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
primeiro_numero = int(input("Digite o primeiro numero: "))
segundo_numero = int(input("Digite o segundo numero: "))
multiplicacao = primeiro_numero * segundo_numero
print(f"o numero {primeiro_numero} multiplicado por {segundo_numero} é igual a: {multiplicacao}")

# 4 - Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
primeiro_numero = int(input("Digite o primeiro numero: "))
segundo_numero = int(input("Digite o segundo numero: "))
divisao_inteira = primeiro_numero // segundo_numero
print(f"A divisão inteira de {primeiro_numero} dividido por {segundo_numero} é : {divisao_inteira}")

# 5 - Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
numero = int(input("Digite o numero: "))
quadrado = numero ** 2
print(f"O quadrado de {numero} é : {quadrado}")

#NÚMEROS DE PONTO FLUTUANTE (float)

# 6 - Escreva um programa que receba dois números flutuantes e realize sua adição.
primeiro_numero = float(input("Digite o primeiro numero: "))
segundo_numero = float(input("Digite o segundo numero: "))
adicao = primeiro_numero + segundo_numero
print(f"A adição de {primeiro_numero} + {segundo_numero} é : {adicao}")

# 7 - Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
media = (num1 + num2)/2
print(f"A média de {num1} e {num2} é : {media}")

# 8 - Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = float(input("Digite o primeiro numero base: "))
expoente = float(input("Digite o expoente: "))
potencia = base ** expoente
print(f" {base} elevado a {expoente} potencia é : {potencia}")

# 9 - Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f" {celsius} graus Celsius é igual a {fahrenheit} graus Fahrenheit")

# 10 - Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio = float(input("Digite o raio do círculo: "))
area = 3.14159 * raio ** 2
print("A área do círculo é:", area)

#STRINGS (str)

# 11 - Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
string_usuario = str(input("Digite o seu nome: "))
print(string_usuario.upper())

# 12 - Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome_usuario = str(input("Digite o seu nome completo: "))
print(string_usuario.lower())

# 13 - Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase_usuario = str(input("Digite uma frase: "))
print(frase_usuario.lstrip())

# 14 - Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = data.split("/")
print("Dia:", dia)
print("Mês:", mes)
print("Ano:", ano)

# 15 - Escreva um programa que concatene duas strings fornecidas pelo usuário.
texto1 = input("Digite o seu nome: ")
texto2 = input("Digite o seu sobrenome: ")
concatenado = texto1 + ' ' + texto2
print(f"Seu nome é {concatenado}")

#BOOLEANOS (bool)

# 16 - Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
valor1 = True
valor2 = False
resultado_and = valor1 and valor2
print("Resultado do AND lógico:", resultado_and)

# 17 - Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
resultado_or = valor1 or valor2
print("Resultado do OR lógico:", resultado_or)

# 18 - Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
resultado_not = not valor1
print("Resultado do NOT lógico:", resultado_not)

# 19 - Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
num1 = 5
num2 = 5
resultado_igualdade = (num1 == num2)
print("Resultado da igualdade:", resultado_igualdade)

# 20 - Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
resultado_diferenca = (num1 != num2)
print("Resultado da diferença:", resultado_diferenca)

'''

https://github.com/lvgalvao/data-engineering-roadmap/tree/main/Bootcamp%20-%20Python%20para%20dados/aula02

'''