import os
import math
from scipy.stats import t

# Ü3.4, 3.6

"""Eingabe"""
n = 20
x̅ = 500
𝛼 = 0.05
S = round(math.sqrt(8.32), 3)    # S^2 = Varianz -> Wurzel aus Varianz

t_value = round(t.ppf(1 - 𝛼 / 2, n - 1), 4)
teilrechnung = round(t_value * S / math.sqrt(n), 3)
KW = [round(x̅ - teilrechnung, 3), round(x̅ + teilrechnung, 3)]

print(os.path.basename(__file__)[3:-3])
print("t_[1 - {0}/2; {1} - 1] = {2}".format(𝛼, n, t_value))
print("[{0} +/- {1} * {2}/WURZEL({3})] = [{4}; {5}]".format(x̅, t_value, S, n, KW[0], KW[1]))