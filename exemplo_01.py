nome = str(input("Digite seu nome: "))

# Exibindo o numero de caracteres do numero digitado
numero_caracteres = len(nome)

print(f"O nome {nome} possui {numero_caracteres} caracteres")

# Criando recurso que realiza a soma de 2 valores fornecidos pelo usuario
primeiro_numero = int(input("Digite o primeiro numero: "))
segundo_numero = int(input("Digite o segundo numero: ")) 

soma = primeiro_numero + segundo_numero

print(f"A soma dos dois numeros é {soma} e é do tipo {type(soma)}")
