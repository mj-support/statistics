import math
from scipy.stats import norm
import os

#ungetestet
### Rep 3.5a

"""Eingabe"""
operator = ">"
n = 397  # Anzahl Werte X ## Achtung X gehört n und Y gehört zum m
m = 328  # Anzahl Werte Y
x̅ = 65   # Mittelwert
Y̅ = 60
S_hoch2_x = round(5.4**2, 3)  # Stichprobenvarianz
S_hoch2_y = round(3.25**2, 3)

𝛼 = 0.05

T = round((x̅ - Y̅)/math.sqrt(S_hoch2_x / n + S_hoch2_y / m), 3)


if operator == "=":
    H_0 = "µ_x {0} µ_y".format("=")
    H_1 = "µ_x {0} µ_y".format("≠")
    KW = [round(norm.ppf(𝛼 / 2), 4), round(norm.ppf(1 - 𝛼 / 2), 4)]
    KW_satz = "z_[{0}/2] = {1}, z_[1 - {0}/2] = {2}".format(𝛼, KW[0], KW[1])
    KB = "[-∞; {0}] v [{1}; +∞]".format(KW[0], KW[1])
    if T > KW[0] and T < KW[1]:
        antwortsatz = "T∉K -> H_0 kann nicht verworfen werden. Zu {0}% können wir davon ausgehen, dass µ_x {1} µ_y ist.".format((1 - 𝛼) * 100, operator)
    else:
        antwortsatz = "T∈K -> H_0 kann verworfen werden. Zu {0}% können wir davon ausgehen, dass µ_x {1} µ_y falsch ist.".format((1 - 𝛼) * 100, operator)
elif operator == ">":
    H_0 = "µ_x {0} µ_y".format("<=")
    H_1 = "µ_x {0} µ_y".format(">")
    KW = round(norm.ppf(1 - 𝛼), 4)
    KW_satz = "z_[1 - {0}] = {1}".format(𝛼, KW)
    KB = "[{0}; +∞]".format(KW)
    if T < KW:
        antwortsatz = "T∉K -> H_0 kann nicht verworfen werden. Zu {0}% können wir davon ausgehen, dass µ_x {1} µ_y falsch ist.".format((1 - 𝛼) * 100, operator)
    else:
        antwortsatz = "T∈K -> H_0 kann verworfen werden. Zu {0}% können wir davon ausgehen, dass µ_x {1} µ_y ist".format((1 - 𝛼) * 100, operator)
elif operator == "<":
    H_0 = "µ_x {0} µ_y".format(">=")
    H_1 = "µ_x {0} µ_y".format("<")
    KW = round(norm.ppf(𝛼), 4)
    KW_satz = "z_[{0}] = {1}".format(𝛼, KW)
    KB = "[-∞; {0}]".format(KW)
    if T > KW:
        antwortsatz = "T∉K -> H_0 kann nicht verworfen werden. Zu {0}% können wir davon ausgehen, dass µ_x {1} µ_y falsch ist.".format((1 - 𝛼) * 100, operator)
    else:
        antwortsatz = "T∈K -> H_0 kann verworfen werden. Zu {0}% können wir davon ausgehen, dass µ_x {1} µ_y ist".format((1 - 𝛼) * 100, operator)

print(os.path.basename(__file__)[3:-3])
print("H_0: {0}".format(H_0))
print("H_1: {0}".format(H_1))
print("T = ({0} - {1})/WURZEL({2}/{3} + {4}/{5}) = {6}".format(x̅, Y̅, S_hoch2_x, n, S_hoch2_y, m, T))
print("KW = {0}".format(KW_satz))
print("KB = {0}".format(KB))
print(antwortsatz)