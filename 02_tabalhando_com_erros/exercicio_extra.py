nome_usuario = input("digite o nome de usuario")

if nome_usuario.isdigit():
    print("Você digitou seu nome errado")
    exit()
elif len(nome_usuario) == 0:
    print("Você não digitou nada")
    exit()
elif nome_usuario.isspace():
    print("Você digitou só espaço")