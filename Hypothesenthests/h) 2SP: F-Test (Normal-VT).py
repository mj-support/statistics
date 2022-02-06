import math
from scipy.stats import f
import os

#Indiz: Testen ob Streuung sich unterscheidet
# Ü3.12c Rep 3.8c

"""Eingabe"""
operator = "="
n = 10  # Anzahl Werte X ## Achtung X gehört n und Y gehört zum m
m = 10  # Anzahl Werte Y
S_hoch2_x = round(50**2, 3)  # Stichprobenvarianz
S_hoch2_y = round(25**2, 3)

𝛼 = 0.05

T = round(S_hoch2_x / S_hoch2_y, 3)

if operator == "=":
    H_0 = "σ^2_x {0} σ^2_y".format("=")
    H_1 = "σ^2_x {0} σ^2_y".format("≠")
    KW = [round(f.ppf(𝛼 / 2, n - 1, m - 1), 3), round(f.ppf(1 - 𝛼 / 2, n - 1, m - 1), 3)]
    KW_satz = "f_[{0}/2, {1} - 1, {2} - 1] = {3}, f_[1 - {0}/2, {1} - 1, {2} - 1] = {4}".format(𝛼, n, m, KW[0], KW[1])
    KB = "[-∞; {0}] v [{1}; +∞]".format(KW[0], KW[1])
    if T > KW[0] and T < KW[1]:
        antwortsatz = "T∉K -> H_0 kann nicht verworfen werden. Zu {0}% können wir davon ausgehen, dass σ^2_x {1} σ^2_y ist.".format((1 - 𝛼) * 100, operator)
    else:
        antwortsatz = "T∈K -> H_0 kann verworfen werden. Zu {0}% können wir davon ausgehen, dass σ^2_x {1} σ^2_y falsch ist.".format((1 - 𝛼) * 100, operator)
elif operator == ">":
    H_0 = "σ^2_x {0} σ^2_y".format("<=")
    H_1 = "σ^2_x {0} σ^2_y".format(">")
    KW = round(f.ppf(1 - 𝛼, n - 1, m - 1), 3)
    KW_satz = "f_[1 - {0}, {1} - 1, {2} - 1] = {3}".format(𝛼, n, m, KW)
    KB = "[{0}; +∞]".format(KW)
    if T < KW:
        antwortsatz = "T∉K -> H_0 kann nicht verworfen werden. Zu {0}% können wir davon ausgehen, dass σ^2_x {1} σ^2_y falsch ist.".format((1 - 𝛼) * 100, operator)
    else:
        antwortsatz = "T∈K -> H_0 kann verworfen werden. Zu {0}% können wir davon ausgehen, dass σ^2_x {1} σ^2_y ist".format((1 - 𝛼) * 100, operator)
elif operator == "<":
    H_0 = "σ^2_x {0} σ^2_y".format(">=")
    H_1 = "σ^2_x {0} σ^2_y".format("<")
    KW = round(f.ppf(𝛼, n - 1, m - 1), 3)
    KW_satz = "f_[{0}, {1} - 1, {2} - 1] = {3}".format(𝛼, n, m, KW)
    KB = "[-∞; {0}]".format(KW)
    if T > KW:
        antwortsatz = "T∉K -> H_0 kann nicht verworfen werden. Zu {0}% können wir davon ausgehen, dass σ^2_x {1} σ^2_y falsch ist.".format((1 - 𝛼) * 100, operator)
    else:
        antwortsatz = "T∈K -> H_0 kann verworfen werden. Zu {0}% können wir davon ausgehen, dass σ^2_x {1} σ^2_y ist".format((1 - 𝛼) * 100, operator)

print(os.path.basename(__file__)[3:-3])
print("H_0: {0}".format(H_0))
print("H_1: {0}".format(H_1))
print("T = {0} / {1} = {2}".format(S_hoch2_x, S_hoch2_y, T))
print("KW = {0}".format(KW_satz))
print("KB = {0}".format(KB))
print(antwortsatz)