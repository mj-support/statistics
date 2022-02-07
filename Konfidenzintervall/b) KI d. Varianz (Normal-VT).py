import os
import math
from scipy.stats import chi2

# ungetestet

"""Eingabe"""
n = 25
𝛼 = 0.05
S_hoch2 = 41.079    # # S^2 = Varianz

chi_hoch2 = [round(chi2.ppf(1 - 𝛼 / 2, n - 1), 4), round(chi2.ppf(𝛼 / 2, n - 1), 4)]
teilrechnung = round((n - 1) * S_hoch2, 3)
KW = [round(teilrechnung / chi_hoch2[0], 4), round(teilrechnung / chi_hoch2[1], 4)]

print(os.path.basename(__file__)[3:-3])
print("chi^2_[1 - {0}/2; {1} - 1] = {2}".format(𝛼, n, chi_hoch2[0]))
print("chi^2_[{0}/2; {1} - 1] = {2}".format(𝛼, n, chi_hoch2[1]))
print("[(({0} - 1) * {1})/{2}; (({0} - 1) * {1})/{3}] = [{4}; {5}]".format(n, S_hoch2, chi_hoch2[0], chi_hoch2[1], KW[0], KW[1]))