import math
from scipy.stats import norm
import os
# Indiz: Anteil / WS herausfinden
#Ü3.8a

"""Eingabe"""
vergleichswert = 0.1
operator = "<"
Y = "Anteil"    # Wahrscheinlichkeit / Anteil
n = 200
x̅ = 4/n   # Anteil bspw. 4/200
p_0 = vergleichswert  # Wahrscheinlichkeit / Anteil
𝛼 = 0.05

T = round(math.sqrt(n) * (x̅ - p_0) / math.sqrt(p_0 * (1 - p_0)), 3)

if operator == "=":
    H_0 = "p {0} {1}".format("=", vergleichswert)
    H_1 = "p {0} {1}".format("≠", vergleichswert)
    KW = [round(norm.ppf(𝛼 / 2), 2), round(norm.ppf(1 - (𝛼 / 2)), 2)]
    KW_satz = "z_[{0}/2] = {1}, z_[1 - {0}/2] = {2}".format(𝛼, KW[0], KW[1])
    KB = "[-∞; {0}] ∩ [{1}; +∞]".format(KW[0], KW[1])
    if T > KW[0] or T < KW[1]:
        antwortsatz = "T∉K -> H_0 kann nicht verworfen werden. Zu {0}% können wir davon ausgehen, dass p {1} {2} ist.".format((1 - 𝛼) * 100, operator, vergleichswert)
    else:
        antwortsatz = "T∈K -> H_0 kann verworfen werden. Zu {0}% können wir davon ausgehen, dass p {1} {2} falsch ist.".format((1 - 𝛼) * 100, operator, vergleichswert)
elif operator == ">":
    H_0 = "p {0} {1}".format("<=", vergleichswert)
    H_1 = "p {0} {1}".format(">", vergleichswert)
    KW = round(norm.ppf(1- 𝛼), 2)
    KW_satz = "z_[1 - {0}] = {1}".format(𝛼, KW)
    KB = "[{0}; +∞]".format(KW)
    if T < KW:
        antwortsatz = "T∉K -> H_0 kann nicht verworfen werden. Zu {0}% können wir davon ausgehen, dass p {1} {2} falsch ist.".format((1 - 𝛼) * 100, operator, vergleichswert)
    else:
        antwortsatz = "T∈K -> H_0 kann verworfen werden. Zu {0}% können wir davon ausgehen, dass p {1} {2} ist.".format((1 - 𝛼) * 100, operator, vergleichswert)
elif operator == "<":
    H_0 = "p {0} {1}".format(">=", vergleichswert)
    H_1 = "p {0} {1}".format("<", vergleichswert)
    KW = round(norm.ppf(𝛼), 2)
    KW_satz = "z_[{0}] = {1}".format(𝛼, KW)
    KB = "[-∞; {0}]".format(KW)
    if T > KW:
        antwortsatz = "T∉K -> H_0 kann nicht verworfen werden. Zu {0}% können wir davon ausgehen, dass p {1} {2} falsch ist.".format((1 - 𝛼) * 100, operator, vergleichswert)
    else:
        antwortsatz = "T∈K -> H_0 kann verworfen werden. Zu {0}% können wir davon ausgehen, dass p {1} {2} ist.".format((1 - 𝛼) * 100, operator, vergleichswert)

print(os.path.basename(__file__)[:-3])
print("H_0: {0}".format(H_0))
print("H_1: {0}".format(H_1))
print("T = (WURZEL({0}) * ({1} - {2})/WURZEL({2} * (1 - {2})) = {3}".format(n, x̅, p_0, T))
print("KW = {0}".format(KW_satz))
print("KB = {0}".format(KB))
print(antwortsatz)
