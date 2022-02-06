import math
from scipy.stats import t
import os

#Indiz: unterschiedliche Varianz -> σ^2_x != σ^2_y, Vergleich Erwartungswerte
# Ü3.12b, Rep 3.5a

"""Eingabe"""
operator = "="
n = 10  # Anzahl Werte X ## Achtung X gehört n und Y gehört zum m
m = 10  # Anzahl Werte Y
x̅ = 200   # Mittelwert
Y̅ = 190
S_hoch2_x = round(5.4**2, 3)  # Stichprobenvarianz
S_hoch2_y = round(3.25**2, 3)

𝛼 = 0.05

T = round((x̅ - Y̅)/math.sqrt(S_hoch2_x / n + S_hoch2_y / m), 3)
Q = round((S_hoch2_x * m) / (S_hoch2_y * n), 3)
FG = math.floor(((1 + Q)**2) / (Q**2 / (n - 1) + (1 / (m - 1))))

if operator == "=":
    H_0 = "µ_x {0} µ_y".format("=")
    H_1 = "µ_x {0} µ_y".format("≠")
    KW = [round(t.ppf(𝛼 / 2, FG), 4), round(t.ppf(1 - 𝛼 / 2, FG), 4)]
    KW_satz = "t_[{0}/2, {1}] = {2}, t_[1 - {0}/2, {1}] = {3}".format(𝛼, FG, KW[0], KW[1])
    KB = "[-∞; {0}] v [{1}; +∞]".format(KW[0], KW[1])
    if T > KW[0] and T < KW[1]:
        antwortsatz = "T∉K -> H_0 kann nicht verworfen werden. Zu {0}% können wir davon ausgehen, dass µ_x {1} µ_y ist.".format((1 - 𝛼) * 100, operator)
    else:
        antwortsatz = "T∈K -> H_0 kann verworfen werden. Zu {0}% können wir davon ausgehen, dass µ_x {1} µ_y falsch ist.".format((1 - 𝛼) * 100, operator)
elif operator == ">":
    H_0 = "µ_x {0} µ_y".format("<=")
    H_1 = "µ_x {0} µ_y".format(">")
    KW = round(t.ppf(1 - 𝛼, FG), 4)
    KW_satz = "t_[1 - {0}, {1}] = {2}".format(𝛼, FG, KW)
    KB = "[{0}; +∞]".format(KW)
    if T < KW:
        antwortsatz = "T∉K -> H_0 kann nicht verworfen werden. Zu {0}% können wir davon ausgehen, dass µ_x {1} µ_y falsch ist.".format((1 - 𝛼) * 100, operator)
    else:
        antwortsatz = "T∈K -> H_0 kann verworfen werden. Zu {0}% können wir davon ausgehen, dass µ_x {1} µ_y ist".format((1 - 𝛼) * 100, operator)
elif operator == "<":
    H_0 = "µ_x {0} µ_y".format(">=")
    H_1 = "µ_x {0} µ_y".format("<")
    KW = round(t.ppf(𝛼, FG), 4)
    KW_satz = "t_[{0}, {1}] = {2}".format(𝛼, FG, KW)
    KB = "[-∞; {0}]".format(KW)
    if T > KW:
        antwortsatz = "T∉K -> H_0 kann nicht verworfen werden. Zu {0}% können wir davon ausgehen, dass µ_x {1} µ_y falsch ist.".format((1 - 𝛼) * 100, operator)
    else:
        antwortsatz = "T∈K -> H_0 kann verworfen werden. Zu {0}% können wir davon ausgehen, dass µ_x {1} µ_y ist".format((1 - 𝛼) * 100, operator)

print(os.path.basename(__file__)[3:-3])
print("H_0: {0}".format(H_0))
print("H_1: {0}".format(H_1))
print("T = ({0} - {1})/WURZEL({2}/{3} + {4}/{5}) = {6}".format(x̅, Y̅, S_hoch2_x, n, S_hoch2_y, m, T))
print("Q = ({0} * {1})/({2} * {3}) = {4}".format(S_hoch2_x, m, S_hoch2_y, n, Q))
print("FG = ((1 + {0})^2)/(({0}^2)/({1} - 1) + 1/({2} - 1) = {3}".format(Q, n, m, FG))
print("KW = {0}".format(KW_satz))
print("KB = {0}".format(KB))
print(antwortsatz)