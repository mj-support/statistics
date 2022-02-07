import math
from scipy.stats import norm
import os

# Indiz: wahre Varianz σ^2 gegeben, gesucht wird Erwartungswert µ
# siehe Ü3.9a

"""Eingabe"""
vergleichswert = 1200
operator = "<"
Y = "Erwartungswert"    # "Erwartungswert
n = 100
x̅ = 1165   # Mittelwert
µ_0 = vergleichswert  # unbekannter Erwartungswert
σ = 200   # Wurzel aus wahren Varianz
𝛼 = 0.05

T = round(math.sqrt(n) * (x̅ - µ_0) / σ, 3)

if operator == "=":
    H_0 = "µ {0} {1}".format("=", vergleichswert)
    H_1 = "µ {0} {1}".format("≠", vergleichswert)
    KW = [round(norm.ppf(𝛼 / 2), 2), round(norm.ppf(1 - (𝛼 / 2)), 2)]
    KW_satz = "z_[{0}/2] = {1}, z_[1 - {0}/2] = {2}".format(𝛼, KW[0], KW[1])
    KB = "[-∞; {0}] v [{1}; +∞]".format(KW[0], KW[1])
    if T > KW[0] and T < KW[1]:
        antwortsatz = "T∉K -> H_0 kann nicht verworfen werden. Zu {0}% können wir davon ausgehen, dass µ {1} {2} ist.".format((1 - 𝛼) * 100, operator, vergleichswert)
    else:
        antwortsatz = "T∈K -> H_0 kann verworfen werden. Zu {0}% können wir davon ausgehen, dass µ {1} {2} falsch ist".format((1 - 𝛼) * 100, operator, vergleichswert)
elif operator == ">":
    H_0 = "µ {0} {1}".format("<=", vergleichswert)
    H_1 = "µ {0} {1}".format(">", vergleichswert)
    KW = round(norm.ppf(1 - 𝛼), 2)
    KW_satz = "z_[1 - {0}] = {1}".format(𝛼, KW)
    KB = "[{0}; +∞]".format(KW)
    if T < KW:
        antwortsatz = "T∉K -> H_0 kann nicht verworfen werden. Zu {0}% können wir davon ausgehen, dass µ {1} {2} falsch ist.".format((1 - 𝛼) * 100, operator, vergleichswert)
    else:
        antwortsatz = "T∈K -> H_0 kann verworfen werden. Zu {0}% können wir davon ausgehen, dass µ {1} {2} ist".format((1 - 𝛼) * 100, operator, vergleichswert)
elif operator == "<":
    H_0 = "µ {0} {1}".format(">=", vergleichswert)
    H_1 = "µ {0} {1}".format("<", vergleichswert)
    KW = round(norm.ppf(𝛼), 2)
    KW_satz = "z_[{0}] = {1}".format(𝛼, KW)
    KB = "[-∞; {0}]".format(KW)
    if T > KW:
        antwortsatz = "T∉K -> H_0 kann nicht verworfen werden. Zu {0}% können wir davon ausgehen, dass µ {1} {2} falsch ist.".format((1 - 𝛼) * 100, operator, vergleichswert)
    else:
        antwortsatz = "T∈K -> H_0 kann verworfen werden. Zu {0}% können wir davon ausgehen, dass µ {1} {2} ist".format((1 - 𝛼) * 100, operator, vergleichswert)

print(os.path.basename(__file__)[3:-3])
print("H_0: {0}".format(H_0))
print("H_1: {0}".format(H_1))
print("T = (WURZEL({0}) * ({1} - {2})/{3} = {4}".format(n, x̅, µ_0, σ, T))
print("KW = {0}".format(KW_satz))
print("KB = {0}".format(KB))
print(antwortsatz)


