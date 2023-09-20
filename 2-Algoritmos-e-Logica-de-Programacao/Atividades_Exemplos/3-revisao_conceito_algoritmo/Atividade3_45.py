"""
Para o fluxograma apresentado na Figura 3.32, responda:
a) determine o valor de no para ni = 8730;
b) determine o valor de no para ni =1234


"""

n = int(input("Que termo deseja encontrar: "))

no = 0
pin = 2
while pin > 1:
    prf = n % 10
    no = no * 10 + prf
    pin = n / 10
    n = pin
print(f"{no}")
