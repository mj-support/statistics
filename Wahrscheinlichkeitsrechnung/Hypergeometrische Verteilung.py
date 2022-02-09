import math
from scipy import stats

# Hypergeometrisch = Stichprobe ohne Zurücklegen, FS S.33
# SS2019 2.1a
print("5 Lieblingstitel bei 15 Lieder. 10 Titel im Shuffle-Modus (kein Titel kommt nochmal)")
print("werden gespielt. Erwartungswert von Lieblingstitel und Varianz berchnen")
print("")

X_satz = "Anzahl Lieblingstitel in SP von 10 Titeln"
n = 8  # Stichprobenumfang, der betrachtet wird
N = 20  # Übergeordnete Anzahl die es gibt
M = 5   # Anzahl der gesuchten Elemente in der übergeordneten Anzahl

p = round(M/N, 3)
bed1 = round(n/N, 3)
bed2 = round(9/(p*(1-p)), 3)

print("X := '{0}'".format(X_satz))
print("X~H(n={0}; N={1}; M={2})".format(n, N, M))
print("p = {0}/{1} = {2}".format(M, N, p))
if bed1 > 0.05:
    print("{0}/{1} = {2} > 0.05 -> Bedingung für hypergeometrische VT erfüllt.".format(n, N, bed1))
    if bed2 > n:
        print("9/({0}*(1-{0})) = {1} > {2} -> Bedingung für hypergeometrische VT erfüllt.".format(p, bed2, n))
        print("-> Hypergeometrische VT.")
        E_x = round(n * M / N, 3)
        Var_x = round(E_x * (1 - M / N) * (N - n) / (N - 1), 3)
        print("E(X) = {0} * {1}/{2} = {3}".format(n, M, N, E_x))
        print("Der Erwartungswert liegt bei {0}.".format(E_x))
        print("Var(X) = {0} * (1 - {1}/{2}) * ({2}-{3})/({2}-1) = {4}".format(E_x, M, N, n, Var_x))
        print("Die Varianz liegt bei {0}.".format(Var_x))
    else:
        print("9/({0}*(1-{0})) = {1} > {2} FALSCH! -> Bedingung für hypergeometrische VT nicht erfüllt.".format(p, bed2, n))
        if bed1 < 1:
            print("{0}/{1} = {2} > 0.05 -> Bedingung für Normal-VT erfüllt.".format(n, N, bed1))
            print("Approximieren über Normal-VT!")
        else:
            print("HÄÄÄ")
else:
    print("{0}/{1} = {2} > 0.05 FALSCH! -> Bedingung nicht erfüllt.".format(n, N, bed1))
    print("Approximieren über Binomialverteilung!")



print("")
print("______________________")
## SS 2019 2b,c
print("Wahrscheinlichkeit, dass genau 2 Lieder Lieblingslieder sind.")
print("")

# Eingabe
operator = "==" # alternativ höchstens / mindestens
X_satz = "Anzahl Lieblingstitel in SP von 10 Titeln"
n = 60  # Stichprobenumfang, der betrachtet wird
N = 800 # Übergeordnete Anzahl die es gibt
M = 240   # Anzahl der gesuchten Elemente in der übergeordneten Anzahl
X = 15   # Anzahl der gesuchten WS in der SP

p = round(M/N, 3)
bed1 = round(n/N, 3)
bed2 = round(9/(p*(1-p)), 3)

print("X := '{0}'".format(X_satz))
print("X~H(n={0}; N={1}; M={2})".format(n, N, M))
print("p = {0}/{1} = {2}".format(M, N, p))
if bed1 > 0.05:
    print("{0}/{1} = {2} > 0.05 -> Bedingung für hypergeometrische VT erfüllt.".format(n, N, bed1))
    if bed2 > n:
        print("9/({0}*(1-{0})) = {1} > {2} -> Bedingung für hypergeometrische VT erfüllt.".format(p, bed2, n))
        print("-> Hypergeometrische VT.")
        P = round(math.comb(M, X) * math.comb(N - M, n - X) / math.comb(N, n), 4)
        if operator != "==":
            print("AAAAAACCHTUNG!!!!!!!!!!!!!!!!!!!!!!!!!! Siehe Rep 2.7")
        print("P(X = {0}) = nCr({1}, {0}) * nCr({2}-{1}, {3}-{0})/nCr({2}, {3}) = {4}".format(X, M, N, n, P))
        print("Die Wahrscheinlichkeit liegt bei {0}%.".format(round(P * 100, 4)))
    else:
        print("9/({0}*(1-{0})) = {1} > {2} -> Bedingung für hypergeometrische VT nicht erfüllt.".format(p, bed2, n))
        if bed1 < 1:
            print("{0}/{1} = {2} > 0.05 -> Bedingung für Normal-VT erfüllt.".format(n, N, bed1))
            print("Approximieren über Normal-VT!")
            E_x = p * n  # Erwartungswert
            print("E(x) = {0} * {1} = {2}".format(p, n, E_x))
            Var_x = round(n * p * (1 - p), 3)
            print("Var(x) = {0} * {1} (1 - {1}) = {2}".format(n, p, Var_x))
            if operator == "<=":
                ϕ_value = round((X + 0.5 - E_x) / math.sqrt(Var_x), 4)
                ϕ = round(stats.norm.cdf(ϕ_value), 4)
                print("P(X <= {0}) = ϕ(({0} + 0.5 - {1})/WURZEL({2}) = ϕ({3}) = {4}".format(X, E_x, Var_x, ϕ_value, ϕ))
            elif operator == "==":
                ϕ_value_1 = round((X + 0.5 - E_x) / math.sqrt(Var_x), 4)
                ϕ_value_2 = round((X - 0.5 - E_x) / math.sqrt(Var_x), 4)
                ϕ_1 = round(stats.norm.cdf(ϕ_value_1), 4)
                ϕ_2 = round(stats.norm.cdf(ϕ_value_2), 4)
                print("P(X = {0}) = ϕ(({0} + 0.5 - {1})/WURZEL({2})) - ϕ(({0} - 0.5 - {1})/WURZEL({2}) = ϕ({3}) - ϕ({4}) = {5}".format(X, E_x, Var_x, ϕ_value_1, ϕ_value_2, round(ϕ_1 - ϕ_2, 3)))
        else:
            print("HÄÄÄ")
else:
    print("{0}/{1} = {2} > 0.05 -> Bedingung nicht erfüllt.".format(n, N, bed1))
    print("Approximieren über Binomialverteilung!")