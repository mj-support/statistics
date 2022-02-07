import math
from scipy.stats import t
import os

#Indiz: gleiche Varianz -> σ^2_x = σ^2_y, Vergleich Erwartungswerte
# siehe Ü3.12a

"""Eingabe"""
operator = "="
n = 567  # Anzahl Werte X ## Achtung X gehört n und Y gehört zum m
m = 646  # Anzahl Werte Y
x̅ = 397   # Mittelwert
Y̅ = 190
S_hoch2_x = 722.22  # Stichprobenvarianz
S_hoch2_y = 332

𝛼 = 0.05

S_hoch2_p = round(((n - 1) * S_hoch2_x + (m - 1) * S_hoch2_y)/(n + m - 2), 3)
T = round((x̅ - Y̅)/math.sqrt(S_hoch2_p * (1/n + 1/m)), 3)

if operator == "=":
    H_0 = "µ_x {0} µ_y".format("=")
    H_1 = "µ_x {0} µ_y".format("≠")
    KW = [round(t.ppf(𝛼 / 2, n + m - 2), 4), round(t.ppf(1 - 𝛼 / 2, n + m - 2), 4)]
    KW_satz = "t_[{0}/2, {1} + {2} - 2] = {3}, t_[1 - {0}/2, {1} + {2} - 2] = {4}".format(𝛼, n, m, KW[0], KW[1])
    KB = "[-∞; {0}] v [{1}; +∞]".format(KW[0], KW[1])
    if T > KW[0] and T < KW[1]:
        antwortsatz = "T∉K -> H_0 kann nicht verworfen werden. Zu {0}% können wir davon ausgehen, dass µ_x {1} µ_y ist.".format((1 - 𝛼) * 100, operator)
    else:
        antwortsatz = "T∈K -> H_0 kann verworfen werden. Zu {0}% können wir davon ausgehen, dass µ_x {1} µ_y falsch ist.".format((1 - 𝛼) * 100, operator)
elif operator == ">":
    H_0 = "µ_x {0} µ_y".format("<=")
    H_1 = "µ_x {0} µ_y".format(">")
    KW = round(t.ppf(1 - 𝛼, n + m - 2), 4)
    KW_satz = "t_[1 - {0}, {1} + {2} - 2] = {3}".format(𝛼, n, m, KW)
    KB = "[{0}; +∞]".format(KW)
    if T < KW:
        antwortsatz = "T∉K -> H_0 kann nicht verworfen werden. Zu {0}% können wir davon ausgehen, dass µ_x {1} µ_y falsch ist.".format((1 - 𝛼) * 100, operator)
    else:
        antwortsatz = "T∈K -> H_0 kann verworfen werden. Zu {0}% können wir davon ausgehen, dass µ_x {1} µ_y ist".format((1 - 𝛼) * 100, operator)
elif operator == "<":
    H_0 = "µ_x {0} µ_y".format(">=")
    H_1 = "µ_x {0} µ_y".format("<")
    KW = round(t.ppf(𝛼, n + m - 2), 4)
    KW_satz = "t_[{0}, {1} + {2} - 2] = {3}".format(𝛼, n, m, KW)
    KB = "[-∞; {0}]".format(KW)
    if T > KW:
        antwortsatz = "T∉K -> H_0 kann nicht verworfen werden. Zu {0}% können wir davon ausgehen, dass µ_x {1} µ_y falsch ist.".format((1 - 𝛼) * 100, operator)
    else:
        antwortsatz = "T∈K -> H_0 kann verworfen werden. Zu {0}% können wir davon ausgehen, dass µ_x {1} µ_y ist".format((1 - 𝛼) * 100, operator)

print(os.path.basename(__file__)[3:-3])
print("H_0: {0}".format(H_0))
print("H_1: {0}".format(H_1))
print("S^2_p = (({0} - 1) * {1} + ({2} - 1) * {3})/({0} + {2} - 2) = {4}".format(n, S_hoch2_x, m, S_hoch2_y, S_hoch2_p))
print("T = (({0} * {1})/WURZEL({2} * (1/{3} + 1/{4}) = {5}".format(x̅, Y̅, S_hoch2_p, n, m, T))
print("KW = {0}".format(KW_satz))
print("KB = {0}".format(KB))
print(antwortsatz)