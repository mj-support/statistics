import math

from scipy import stats

## SS 2019 2.2b
print("Wahrscheinlichkeit, von mind. 1 Seite ohne Fehler bei 50 Seiten, wenn 3 Fehler pro Seite erwartet.")
print("")

X_satz = "Erwartete Fehler je Seite"
n = 2 # Betrachtungsraum
λ = 4 * n   # Erwartungswert
X = 10   # Wert der Eintreten soll
operator = "=="

print("X := '{0}'".format(X_satz))
print("X~Po({0})".format(λ))
#P_X = round(λ**0 / math.factorial(X) * math.e**-λ, 3)
#P_S = round(1 - (1 - P_X)**n, 3)
if operator == ">":
    po = round(stats.poisson.cdf(X, λ), 3)
    print("P(X > {0}) = 1 - P(X <= {0}) = 1 - F({0}) = 1 - {1} = {2}".format(X, po, round(1-po, 4)))
elif operator == ">=":
    po = round(stats.poisson.cdf(X-1, λ), 3)
    print("P(X >= {0}) = 1 - P(X <= {1}) = 1 - F({1}) = 1 - {2} = {3}".format(X, X-1, po, round(1-po, 4)))
elif operator == "==":
    po_1 = round(stats.poisson.cdf(X, λ), 3)
    po_2 = round(stats.poisson.cdf(X - 1, λ), 3)
    print("P(X = {0}) = P(X <= {0}) - P(X <= {1}) = F({0}) - F({1}) = {2} - {3} = {4}".format(X, X-1, po_1, po_2, round(po_1-po_2, 4)))