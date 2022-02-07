import math
from scipy.stats import norm

"""Aufgabe"""
"Wie viele Ausschussstücke dürfen in einer Stichprobe von 400 Stück höchstens gefunden werden, " \
"damit es nicht zur Ablehnung der Warenlieferung kommt (𝛼𝛼 = 0.05)."""

p_0 = 0.02  # so hoch darf der Anteil maximal sein
n = 400
𝛼 = 0.05


z_value = round(norm.ppf(1 - 𝛼), 2)
p_dach = round(p_0 + z_value * math.sqrt(p_0 * (1 - p_0))/math.sqrt(n), 4)
mw = round(p_dach * n, 1)

print("H_0 wird verworfen, wenn t > z_1-𝛼, d.h.")
print("WURZEL(n) * (p_dach - p_0)/WURZEL(p_0 * (1 - p_0)) > z_1-𝛼")
print("p_dach >= p_0 + z_1-𝛼 * WURZEL(p_0 * (1 - p_0))/WURZEL(n)")
print("p_dach >= {0} + {1} * WURZEL({0} * (1 - {0}))/WURZEL({2}) = {3}".format(p_0, z_value, n, p_dach))
print("{0} * {1} = {2} -> {3}".format(p_dach, n, mw, math.floor(mw)))