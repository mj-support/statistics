A = 0.4    # Allgemeine WS
A_B = 0.8    # WS in Abhängigkeit von A

B = 0.38   # Allgemeine WS von B  muss selbst errechnet werden. Nicht gegeben!!!

P_B_A = round(A_B * A / B, 4)
print("P(B/A) = {0} * {1} / {2} = {3}".format(A_B, A, B, P_B_A))
print("Die Wahrscheinlichkeit liegt bei {0}%.".format(round(P_B_A*100, 4)))

print("")
print("------------------")
print("Mit welcher WS mindestens eines der beiden")

X = 0.4
Y = 0.6

XY = X * Y
P = X + Y - XY

print("P(X u Y) = {0} + {1} - {2} = {3}".format(X, Y, XY, P))