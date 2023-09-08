from statistics import median

valores = []
while True:
    print("Caso tenha passado todos os valores escreva 'exit' ")
    numero = input("Informe o numero: ")
    if numero == "exit":
        break
    elif not numero.isdigit():
        print("###### ERROR: informe apenas numeros - ######")
        continue
    else:
        valores.append(int(numero))


media = median(valores)
print(media)
