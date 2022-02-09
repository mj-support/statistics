import math
from scipy.stats import t
import os
# Indix: gesucht wird Mittelwert / Erwartungswert, Varianz der Stichprobe S^2 gegeben
# siehe Ü3.9b, Ü3.10a

"""Eingabe"""
vergleichswert = 90
operator = "<"
Y = "Erwartungswert"    # Erwartungswert
n = 25
x̅ = 84   # Mittelwert
µ_0 = vergleichswert  # unbekannter Erwartungwert
S = 15 #round(math.sqrt(6.98), 3)   # Wurzel aus Varianz der Stichprobe
𝛼 = 0.01

T = round(math.sqrt(n) * (x̅ - µ_0) / S, 3)

if operator == "=":
    H_0 = "µ {0} {1}".format("=", vergleichswert)
    H_1 = "µ {0} {1}".format("≠", vergleichswert)
    KW = [round(t.ppf(𝛼 / 2, n - 1), 4), round(t.ppf(1 - (𝛼 / 2), n - 1), 4)]
    KW_satz = "t_[{0}/2; {1} - 1] = {2}, t_[1 - {0}/2, {1} - 1] = {3}".format(𝛼, n, KW[0], KW[1])
    KB = "[-∞; {0}] v [{1}; +∞]".format(KW[0], KW[1])
    if T > KW[0] and T < KW[1]:
        antwortsatz = "T∉K -> H_0 kann nicht verworfen werden. Zu {0}% können wir davon ausgehen, dass µ {1} {2} ist.".format((1 - 𝛼) * 100, operator, vergleichswert)
    else:
        antwortsatz = "T∈K -> H_0 kann verworfen werden. Zu {0}% können wir davon ausgehen, dass µ {1} {2} falsch ist".format((1 - 𝛼) * 100, operator, vergleichswert)
elif operator == ">":
    H_0 = "µ {0} {1}".format("<=", vergleichswert)
    H_1 = "µ {0} {1}".format(">", vergleichswert)
    KW = round(t.ppf(1- 𝛼, n - 1), 4)
    KW_satz = "t_[1 - {0}, {1} - 1] = {2}".format(𝛼, n, KW)
    KB = "[{0}; +∞]".format(KW)
    if T < KW:
        antwortsatz = "T∉K -> H_0 kann nicht verworfen werden. Zu {0}% können wir davon ausgehen, dass µ {1} {2} falsch ist.".format((1 - 𝛼) * 100, operator, vergleichswert)
    else:
        antwortsatz = "T∈K -> H_0 kann verworfen werden. Zu {0}% können wir davon ausgehen, dass µ {1} {2} ist".format((1 - 𝛼) * 100, operator, vergleichswert)
elif operator == "<":
    H_0 = "µ {0} {1}".format(">=", vergleichswert)
    H_1 = "µ {0} {1}".format("<", vergleichswert)
    KW = round(t.ppf(𝛼, n - 1), 4)
    KW_satz = "t_[{0}; {1} - 1] = {2}".format(𝛼, n, KW)
    KB = "[-∞; {0}]".format(KW)
    if T > KW:
        antwortsatz = "T∉K -> H_0 kann nicht verworfen werden. Zu {0}% können wir davon ausgehen, dass µ {1} {2} falsch ist.".format((1 - 𝛼) * 100, operator, vergleichswert)
    else:
        antwortsatz = "T∈K -> H_0 kann verworfen werden. Zu {0}% können wir davon ausgehen, dass µ {1} {2} ist".format((1 - 𝛼) * 100, operator, vergleichswert)

print(os.path.basename(__file__)[3:-3])
print("H_0: {0}".format(H_0))
print("H_1: {0}".format(H_1))
print("T = (WURZEL({0}) * ({1} - {2})/{3} = {4}".format(n, x̅, µ_0, S, T))
print("KW = {0}".format(KW_satz))
print("KB = {0}".format(KB))
print(antwortsatz)