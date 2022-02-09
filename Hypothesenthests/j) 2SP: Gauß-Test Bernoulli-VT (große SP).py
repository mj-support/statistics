import math
from scipy.stats import norm
import os

# Indiz: Gesucht: Anteil / WS / Erfolgsquote
# Ü3.8b, Ü3.11c

"""Eingabe"""
operator = "<"
n = 450  # Anzahl Werte X ## Achtung X gehört n und Y gehört zum m
m = 1000  # Anzahl Werte Y
x̅ = round(0.61, 3)   # Mittelwert bzw. Wahrscheinlichkeit / Anteil ausrechnen
Y̅ = round(800 / m, 3)   # manchmal auch die Mitte eines Intervalls

𝛼 = 0.10

p_dach = round((n * x̅ + m * Y̅) / (n + m), 3)
T = round((x̅ - Y̅)/math.sqrt(p_dach * (1 - p_dach) * (1/n + 1/m)), 3)


if operator == "=":
    H_0 = "p_x {0} p_y".format("=")
    H_1 = "p_x {0} p_y".format("≠")
    KW = [round(norm.ppf(𝛼 / 2), 2), round(norm.ppf(1 - 𝛼 / 2), 2)]
    KW_satz = "z_[{0}/2] = {1}, z_[1 - {0}/2] = {2}".format(𝛼, KW[0], KW[1])
    KB = "[-∞; {0}] v [{1}; +∞]".format(KW[0], KW[1])
    if KW[0] < T < KW[1]:
        antwortsatz = "T∉K -> H_0 kann nicht verworfen werden. Zu {0}% können wir davon ausgehen, dass p_x {1} p_y ist.".format((1 - 𝛼) * 100, operator)
    else:
        antwortsatz = "T∈K -> H_0 kann verworfen werden. Zu {0}% können wir davon ausgehen, dass p_x {1} p_y falsch ist.".format((1 - 𝛼) * 100, operator)
elif operator == ">":
    H_0 = "p_x {0} p_y".format("<=")
    H_1 = "p_x {0} p_y".format(">")
    KW = round(norm.ppf(1 - 𝛼), 2)
    KW_satz = "z_[1 - {0}] = {1}".format(𝛼, KW)
    KB = "[{0}; +∞]".format(KW)
    if T < KW:
        antwortsatz = "T∉K -> H_0 kann nicht verworfen werden. Zu {0}% können wir davon ausgehen, dass p_x {1} p_y falsch ist.".format((1 - 𝛼) * 100, operator)
    else:
        antwortsatz = "T∈K -> H_0 kann verworfen werden. Zu {0}% können wir davon ausgehen, dass p_x {1} p_y ist".format((1 - 𝛼) * 100, operator)
elif operator == "<":
    H_0 = "p_x {0} p_y".format(">=")
    H_1 = "p_x {0} p_y".format("<")
    KW = round(norm.ppf(𝛼), 2)
    KW_satz = "z_[{0}] = {1}".format(𝛼, KW)
    KB = "[-∞; {0}]".format(KW)
    if T > KW:
        antwortsatz = "T∉K -> H_0 kann nicht verworfen werden. Zu {0}% können wir davon ausgehen, dass p_x {1} p_y falsch ist.".format((1 - 𝛼) * 100, operator)
    else:
        antwortsatz = "T∈K -> H_0 kann verworfen werden. Zu {0}% können wir davon ausgehen, dass p_x {1} p_y ist".format((1 - 𝛼) * 100, operator)

print(os.path.basename(__file__)[3:-3])
print("H_0: {0}".format(H_0))
print("H_1: {0}".format(H_1))
print("p_dach = ({0} * {1} + {2} * {3})/({0} + {2}) = {4}".format(n, x̅, m, Y̅, p_dach))
print("T = ({0} - {1})/WURZEL({2} * (1 - {2}) * (1/{3} + 1/{4}) = {5}".format(x̅, Y̅, p_dach, n, m, T))
print("KW = {0}".format(KW_satz))
print("KB = {0}".format(KB))
print(antwortsatz)