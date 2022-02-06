import os
import math
from scipy.stats import norm

# ungetestet

"""Eingabe"""
n = 25
x̅ = 75
𝛼 = 0.05
S = 41.079

z_value = round(norm.ppf(1 - 𝛼 / 2), 4)
teilrechnung = round(z_value * S / math.sqrt(n), 3)
KW = [round(x̅ - teilrechnung, 3), round(x̅ + teilrechnung, 3)]

print(os.path.basename(__file__)[3:-3])
print("z_[1 - {0}/2] = {2}".format(𝛼, n, z_value))
print("[{0} +/- {1} * {2}/WURZEL({3})] = [{4}, {5}]".format(x̅, z_value, S, n, KW[0], KW[1]))