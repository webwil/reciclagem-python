valor = int(5)
divisao = int(1)

try:
    resultado = valor / divisao
    print(resultado)
except ZeroDivisionError:
    resultado = "Erro: integer division or modulo by zero Willian"
    print(resultado)
except KeyboardInterrupt:
    resultado = "Acho que você interrompeu o programa"
    print(resultado)
    
try:
    resultado = len("5")
except TypeError as e:
    print(e)
else:
    print("eu tudo certo com o programa")
finally:
    print("Finalizando o programa")