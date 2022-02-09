import math
print("Konfidenzintervall, Hypothesentests (S.40)")
print("Ermittlung Stichprobenvarianz S^2")
print("")
n = 5
summe_x_hoch2_v = 181125
x̅ = 75

S_hoch2 = round(1 / (n - 1) * (summe_x_hoch2_v - (n * x̅**2)), 3)
S = round(math.sqrt(S_hoch2), 3)
print("S^2 = 1 / ({0} - 1) * ({1} - ({0} * {2}^2) = {3}".format(n, summe_x_hoch2_v, x̅, S_hoch2))
print("S = WURZEL({0}) = {1}".format(S_hoch2, S))

# Alternativ
n = 5
x̅ = round((0.18 + 0.25 + 0.12 + 0.2 + 0.25) / 5, 3)
X_hoch2_v = round(0.18**2 + 0.25**2 + 0.12**2 + 0.2**2 + 0.25**2, 3)

S_hoch2 = round((1 / (n - 1)) * (X_hoch2_v - n * x̅**2), 3)
S = round(math.sqrt(S_hoch2), 3)

print("S^2 = 1/({0} - 1) * ({1} - {0}*{2}^2) = {3}".format(n, X_hoch2_v, x̅, S_hoch2))
print("S = WURZEL({0}) = {1}".format(S_hoch2, S))

print("")
print("__________________________________")
print("5-Zahlenzusammenfassung")

# Eingabe
werte = [72, 67, 78, 40, 34, 50, 98, 116, 82, 31, 58, 15]
länge = len(werte)
werte.sort()

if länge % 2 == 0:
    x_0_5 = (werte[int(länge / 2 - 1)] + werte[int(länge / 2)]) / 2
else:
    x_0_5 = werte[int(länge / 2)]

if länge % 4 == 0:
    x_0_25 = (werte[int(länge / 4 - 1)] + werte[int(länge / 4)]) / 2
else:
    x_0_25 = werte[int(länge / 4)]

if 3 * länge % 4 == 0:
    x_0_75 = (werte[int(3 * länge / 4 - 1)] + werte[int(3 * länge / 4)]) / 2
else:
    x_0_75 = werte[int(länge / 4)]

print("n = {0}".format(länge))
print("                 x_[0.5] = {0}".format(x_0_5))
print("x_[0.25] = {0}                    x_[0.75] = {1}".format(x_0_25, x_0_75))
print("x_[1] = {0}                       x_[12] = {1}".format(werte[0], werte[länge - 1]))