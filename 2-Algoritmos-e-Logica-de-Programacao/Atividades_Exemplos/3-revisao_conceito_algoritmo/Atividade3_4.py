from math import sqrt

R = 2
S = 5
T = -1
X = 3
Y = 1
Z = 0

A = (R >= 5) or (T > Z) and (X - Y + R > 3 * Z)
B = (abs(T) + 3 >= 4) and not (3 * R / 2 < S * 3)
C = (X == 2) or (Y == 1) and ((Z == 0) or (R > 3)) and (S < 10)
D = (R != S) or not (sqrt(R) < sqrt(X)) and (4327 * X * S * Z == 0)

print(f"{A}\n{B}\n{C}\n{D}")
