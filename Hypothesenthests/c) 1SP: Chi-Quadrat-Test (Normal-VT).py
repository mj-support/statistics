import math
from scipy.stats import chi2
import os
# Indix: Aussage über Varianz treffen
# siehe Ü3.10b

"""Eingabe"""
vergleichswert = 6.25
operator = ">"
Y = "Varianz"    # (konkrete) Varianz
n = 20
S_hoch2 = 8.32   # Varianz der Stichprobe
𝛼 = 0.05
σ_hoch2_0 = vergleichswert # Varianz der Sollwertabweichung

T = round((n - 1) * S_hoch2 / σ_hoch2_0, 3)

if operator == "=":
    H_0 = "σ^2 {0} {1}".format("=", vergleichswert)
    H_1 = "σ^2 {0} {1}".format("≠", vergleichswert)
    KW = [round(chi2.ppf(𝛼 / 2, n - 1), 3), round(chi2.ppf(1 - (𝛼 / 2), n - 1), 3)]
    KW_satz = "Chi-Quadrat_[{0}/2; {1} - 1] = {2}, Chi-Quadrat_[1 - {0}/2, {1} - 1] = {3}".format(𝛼, n, KW[0], KW[1])
    KB = "[-∞; {0}] ∩ [{1}; +∞]".format(KW[0], KW[1])
    if T > KW[0] or T < KW[1]:
        antwortsatz = "T∉K -> H_0 kann nicht verworfen werden. Zu {0}% können wir davon ausgehen, dass σ^2 {1} {2} falsch ist.".format((1 - 𝛼) * 100, operator, vergleichswert)
    else:
        antwortsatz = "T∈K -> H_0 kann verworfen werden. Zu {0}% können wir davon ausgehen, dass σ^2 {1} {2} ist".format((1 - 𝛼) * 100, operator, vergleichswert)
elif operator == ">":
    H_0 = "σ^2 {0} {1}".format("<=", vergleichswert)
    H_1 = "σ^2 {0} {1}".format(">", vergleichswert)
    KW = round(chi2.ppf(1- 𝛼, n - 1), 3)
    KW_satz = "Chi-Quadrat_[1 - {0}, {1} - 1] = {2}".format(𝛼, n, KW)
    KB = "[{0}; +∞]".format(KW)
    if T < KW:
        antwortsatz = "T∉K -> H_0 kann nicht verworfen werden. Zu {0}% können wir davon ausgehen, dass σ^2 {1} {2} falsch ist.".format((1 - 𝛼) * 100, operator, vergleichswert)
    else:
        antwortsatz = "T∈K -> H_0 kann verworfen werden. Zu {0}% können wir davon ausgehen, dass σ^2 {1} {2} ist".format((1 - 𝛼) * 100, operator, vergleichswert)
elif operator == "<":
    H_0 = "σ^2 {0} {1}".format(">=", vergleichswert)
    H_1 = "σ^2 {0} {1}".format("<", vergleichswert)
    KW = round(chi2.ppf(𝛼, n - 1), 3)
    KW_satz = "Chi-Quadrat_[{0}; {1} - 1] = {2}".format(𝛼, n, KW)
    KB = "[-∞; {0}]".format(KW)
    if T > KW:
        antwortsatz = "T∉K -> H_0 kann nicht verworfen werden. Zu {0}% können wir davon ausgehen, dass σ^2 {1} {2} falsch ist.".format((1 - 𝛼) * 100, operator, vergleichswert)
    else:
        antwortsatz = "T∈K -> H_0 kann verworfen werden. Zu {0}% können wir davon ausgehen, dass σ^2 {1} {2} ist".format((1 - 𝛼) * 100, operator, vergleichswert)

print(os.path.basename(__file__)[:-3])
print("H_0: {0}".format(H_0))
print("H_1: {0}".format(H_1))
print("T = (({0} - 1) * {1})/{2} = {3}".format(n, S_hoch2, σ_hoch2_0, T))
print("KW = {0}".format(KW_satz))
print("KB = {0}".format(KB))
print(antwortsatz)