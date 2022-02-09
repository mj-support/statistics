import math

from scipy import stats

# SS15 2.2b
print("WS von Geburt vor mehr als 259 Tagen bei E(x) von 280 und Standardabweichung von 10")
X_satz = "Dauer der Schwangerschaft"
X = 80 # gegebener Wert dessen WS berechnet werden soll
λ = 65   # Erwartungswert
σ_hoch2 = 15 ** 2 # Standardabweichung^2
operator = ">"

print("X := '{0}'".format(X_satz))
print("X~N({0}; {1})".format(λ, σ_hoch2))

if operator == "<":
    ϕ_value = round((X - λ) / math.sqrt(σ_hoch2), 4)
    ϕ = round(stats.norm.cdf(ϕ_value), 4)
    print("P(X < {0}) = ϕ(({0} - {1})/{2} = ϕ({3}) = {4}".format(X, λ, round(math.sqrt(σ_hoch2),3), ϕ_value, ϕ))
elif operator == "<=":
    ϕ_value = round((X+1 - λ) / math.sqrt(σ_hoch2), 4)
    ϕ = round(stats.norm.cdf(ϕ_value), 4)
    print("P(X <= {0}) = ϕ(({0} + 1 - {1})/{2} = ϕ({3}) = {4}".format(X, λ, round(math.sqrt(σ_hoch2),3), ϕ_value, ϕ))
elif operator == ">=":
    ϕ_value = round((X - λ) / math.sqrt(σ_hoch2), 4)
    ϕ = round(1- stats.norm.cdf(ϕ_value), 4)
    print("P(X >= {0}) = 1 - ϕ(({0} - {1})/{2} = 1 - ϕ({3}) = {4}".format(X, λ, round(math.sqrt(σ_hoch2),3), ϕ_value, ϕ))
elif operator == ">":
    ϕ_value = round((X - λ) / math.sqrt(σ_hoch2), 4)
    ϕ = round(1- stats.norm.cdf(ϕ_value), 4)
    print("P(X > {0}) = 1 - ϕ(({0} - {1})/{2} = 1 - ϕ({3}) = {4}".format(X, λ, round(math.sqrt(σ_hoch2),3), ϕ_value, ϕ))

print("Die Wahrscheinlichkeit liegt bei {0}%.".format(ϕ * 100))


print("")
print("______________________")
print("Welche Länge habe die 25% größten Haie mindestens")

gesucht = 0.75  # 0.75 bei mindestens die größten 25%
λ = 65   # Erwartungswert
σ = 15  # Standardabweichung

ϕ = round(stats.norm.ppf(gesucht), 4)
ergebnis = λ + ϕ * σ


print("x_[{0}] = {1} + z_[{0}] * {2} = {1} + {3} * {2} = {4}".format(gesucht, λ, σ, ϕ, ergebnis))




print("")
print("______________________")
## SS 2019 2b,c
print("Wie hoch Erwartungswert, damit WS einer zur geringen Befüllung max. 0.1%.")
print("")

max_ϕ_value = 0.001
X = 3
σ = 0.2 # Standardabweichung bzw. Wurzel aus Varianz

z = round(stats.norm.ppf(max_ϕ_value), 3)
ergebnis = X + z * σ * -1

print("ϕ(z) <= {0}".format(max_ϕ_value))
print(("z <= {0}".format(z)))
print("(x-μ)/σ = {0}".format(z))
print("μ = x + {0} * σ".format(z * -1))
print("{0} + {1} * {2} = {3}".format(X, z*-1, σ, ergebnis))
