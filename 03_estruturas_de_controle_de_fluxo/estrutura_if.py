x = int(input("digite um numero inteiro: "))

if x < 0:
    x = 0
    print('numero negativo ou menor que zero')
elif x == 0:
    print("o Numero digitado foi zero")
elif x == 1:
    print("Numero digitado foi um")
else:
    print(f"Voce digitou o numero: {x}")