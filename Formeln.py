import math
# Konfidenzintervall, Hypothesentests (S.40)
# Ermittlung Stichprobenvarianz S^2
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

