import math
# Konfidenzintervall, Hypothesentests (S.40)
# Ermittlung Stichprobenvarianz S^2
n = 25
summe_x_hoch2_v = 181125
x̅ = 75

S_hoch2 = 1 / (n - 1) * (summe_x_hoch2_v - (n * x̅**2))
S = round(math.sqrt(1687.5), 3)
print("S^2 = 1 / ({0} - 1) * ({1} - ({0} * {2}^2) = {3}".format(n, summe_x_hoch2_v, x̅, S_hoch2))
print("S = WURZEL({0}) = {1}".format(S_hoch2, S))



# 3.10c, 3.11a, 3.11b, 3.13a, 3.13c, 3.14a, 3.14c, 3.15 komplett, 3.16 komplett