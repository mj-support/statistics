import os
import math
from scipy.stats import t

# Ü3.4

"""Eingabe"""
n = 25
x̅ = 75
𝛼 = 0.05
S = 41.079

t_value = round(t.ppf(1 - 𝛼 / 2, n - 1), 4)
teilrechnung = round(t_value * S / math.sqrt(n), 3)
KW = [x̅ - teilrechnung, x̅ + teilrechnung]

print(os.path.basename(__file__)[3:-3])
print("t_[1 - {0}/2; {1} - 1] = {2}".format(𝛼, n, t_value))
print("[{0} +/- {1} * {2}/WURZEL({3})] = [{4}, {5}]".format(x̅, t_value, S, n, KW[0], KW[1]))