import os
import math
from scipy.stats import norm

### Ü3.7a,b, 3.11b

"""Eingabe"""
x̅ = 0.5   # Mitte des Intervalls bzw. Einfach der Erwartungswert halt bzw. ohne Vorabinformation ist x̅ = 0.5
𝛼 = 0.05
L_stern = 0.1 #2 * 𝛼 # da in beide Richtungen

z_value = round(norm.ppf(1 - 𝛼 / 2), 2)
n = round(((2 * z_value * math.sqrt(x̅ * (1 - x̅))) / L_stern)**2, 3)

print(os.path.basename(__file__)[:-3])
print("z_[1 - {0}/2] = {1}".format(𝛼, z_value))
print("n >= ((2 * {0} * WURZEL({1} * (1 - {1}))/{2})^2 >= {3} -> {4}".format(z_value, x̅, L_stern, n, math.ceil(n)))


