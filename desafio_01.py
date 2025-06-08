nome_funcionario = str(input("Digite seu nome: "))
salario_funcionario = float(input("Digite seu salario: "))
percentual_bonus_funcionario = float(input("digite o percetual do bonua"))

soma_salario_bonus = ((salario_funcionario / 100) * percentual_bonus_funcionario) + 1000+ salario_funcionario

print(f"olá {nome_funcionario} seu salario com o bonos e % de comissão vai ser de R$ {soma_salario_bonus}")