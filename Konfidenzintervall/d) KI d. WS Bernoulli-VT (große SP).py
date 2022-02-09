import os
import math
from scipy.stats import norm

# Ü3.5a, 3.7c, 3.10a

"""Eingabe"""
n = 450
x̅ = 0.61 #1500 / n   # round(256 / 400, 3)
𝛼 = 0.01

z_value = round(norm.ppf(1 - 𝛼 / 2), 2)
teilrechnung = round(z_value * math.sqrt((x̅ * (1 - x̅)) / n), 3)
KW = [round(x̅ - teilrechnung, 4), round(x̅ + teilrechnung, 4)]

print(os.path.basename(__file__)[3:-3])
print("z_[1 - {0}/2] = {1}".format(𝛼, z_value))
print("[{0} +/- {1} * WURZEL({0}*(1 - {0})/{2}) = [{3}; {4}]".format(x̅, z_value, n, KW[0], KW[1]))
print("Zum Konfidenzniveau von {0} % liegt der Anteil zwischen {1}% und {2}%.".format((1-𝛼)*100, KW[0]*100, KW[1]*100 ))