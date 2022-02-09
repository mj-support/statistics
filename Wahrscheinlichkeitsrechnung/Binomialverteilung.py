import math

from scipy import stats

# SS20 2.1a
print("250 Mal Münze werfen ")
X_Satz = "Wurf der Münzseite Zahl"
n = 8 # Wie oft / Wie viele insgesamt
p = 0.3 # Wahrscheinlichkeit
X = 8 # Wie oft gesuchtes Ereignis eintreten soll
operator = "=="

print("X := '{0}'".format(X_Satz))
print("X~B({0}, {1})".format(n, p))
Bedingung = round(9/(p*(1-p)), 3)

if n < Bedingung:
    print("9/({0}*(1-{0}) = {1} > {2} -> Bedingung für Binomial-VT erfüllt.".format(p, Bedingung, n))
    E_x = p * n  # Erwartungswert
    print("E(x) = {0} * {1} = {2}".format(p, n, E_x))
    Var_x = round(n * p * (1 - p), 3)
    print("Var(x) = {0} * {1} * (1 - {1}) = {2}".format(n, p, Var_x))
    if operator == "==":
        P_X = round(math.comb(n, X)*(p**X)*((1-p)**(n-X)), 4)
        print("P(X = {0}) = nCR({1}, {0}) * {2}^{0} * (1 - {2})^({1}-{0}) = {3}".format(X, n, p, P_X))
    elif operator == ">" or ">=":
        print("Für jede WS die möglich ist, einzelne WS addieren (==) und Operator anpassen!!")
        P_X = round(math.comb(n, X)*(p**X)*((1-p)**(n-X)), 4)
        print("z.B: P(X > {2}) = P(X = 3) + P(X = 4) ... = (nCR({1}, {0}) * {2}^{0} * (1 - {2})^({1}-{0}) = {3}".format(X, n, p, P_X))
else:
    print("9/({0}*(1-{0}) = {1} > {2} FALSCH! -> Bedingung für Binomial-VT nicht erfüllt.".format(p, Bedingung, n))
    print("Approximieren über Normal-VT!")
    E_x = p * n  # Erwartungswert
    print("E(x) = {0} * {1} = {2}".format(p, n, E_x))
    Var_x = round(n * p * (1 - p), 3)
    print("Var(x) = {0} * {1} (1 - {1}) = {2}".format(n, p, Var_x))
    if operator == "<=":
        ϕ_value = round((X + 0.5 - E_x) / math.sqrt(Var_x), 4)
        ϕ = round(stats.norm.cdf(ϕ_value), 4)
        print("P(X <= {0}) = ϕ(({0} + 0.5 - {1})/WURZEL({2}) = ϕ({3}) = {4}".format(X, E_x, Var_x, ϕ_value, ϕ))
    elif operator == "<":
        ϕ_value = round((X - 1 + 0.5 - E_x) / math.sqrt(Var_x), 4)
        ϕ = round(stats.norm.cdf(ϕ_value), 4)
        print("P(X < {0}) = ϕ(({0} - 1 + 0.5 - {1})/WURZEL({2}) = ϕ({3}) = {4}".format(X, E_x, Var_x, ϕ_value, ϕ))
    elif operator == "==":
        ϕ_value_1 = round((X + 0.5 - E_x) / math.sqrt(Var_x), 4)
        ϕ_value_2 = round((X - 0.5 - E_x) / math.sqrt(Var_x), 4)
        ϕ_1 = round(stats.norm.cdf(ϕ_value_1), 4)
        ϕ_2 = round(stats.norm.cdf(ϕ_value_2), 4)
        print(
            "P(X = {0}) = ϕ(({0} + 0.5 - {1})/WURZEL({2})) - ϕ(({0} - 0.5 - {1})/WURZEL({2}) = ϕ({3}) - ϕ({4}) = {5}".format(
                X, E_x, Var_x, ϕ_value_1, ϕ_value_2, round(ϕ_1 - ϕ_2, 3)))
    elif operator == ">":
        ϕ_value = round((X + 0.5 - E_x) / math.sqrt(Var_x), 4)
        ϕ = round(1 - stats.norm.cdf(ϕ_value), 4)
        print("P(X > {0}) = 1 - ϕ(({0} + 0.5 - {1})/WURZEL({2}) = 1 - ϕ({3}) = {4}".format(X, E_x, Var_x, ϕ_value, ϕ))
    elif operator == ">=":
        ϕ_value = round((X - 1 + 0.5 - E_x) / math.sqrt(Var_x), 4)
        ϕ = round(1 - stats.norm.cdf(ϕ_value), 4)
        print("P(X >= {0}) = 1 - ϕ(({0} - 1 + 0.5 - {1})/WURZEL({2}) = 1 - ϕ({3}) = {4}".format(X, E_x, Var_x, ϕ_value, ϕ))
    elif operator == "><":
        print("Berechnung von der oberen Grenze - 1 + Berechnung von der unteren Grenze(mit X+1) = Ergebnis")


