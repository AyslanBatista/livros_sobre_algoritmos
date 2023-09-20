from statistics import median

valores = []
while True:
    print("Caso tenha passado todos os valores escreva 'exit' ")
    numero_x = input("Informe o numero x: ")
    numero_y = input("Informe o numero y: ")
    if numero_x == "exit" or numero_y == "exit":
        break
    else:
        resultado = int(numero_x) ** int(numero_y)
        valores.append(int(resultado))


media = median(valores)
print(media)
