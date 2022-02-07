import math
from scipy.stats import t

"""Eingabe"""
Y = "körperliche Leistungsfähigkeit"
X = "kognitive Leistungsfähigkeit"
n = 323 # Anzahl Zeilen bzw. n-WErt der Summen
summe_x_hoch2_v = 48008500  # Summe von x^2_v
š_hoch2_x = 277.828   # varianz
š_hoch2_y = 218.452
ß_dach_1 = 0.048
ß_dach_0 = 13.504
s_hoch2_E = 4500
R_hoch2 = 0.0029
KI_ß_dach_1 = [0.14, 0.16]
𝛼 = 0.01


print("--------------------")
print("1) Frage: Testen Sie ob Konstante signifikant kleiner/größer als xxx ist.")
print("")

"""Eingabe"""
vergleichswert = 0
operator = ">"

s_dach_B_0 = round(math.sqrt((s_hoch2_E * 1/n * summe_x_hoch2_v) / (n * š_hoch2_x)), 3) #Standardfehler der Residuen
T = round((ß_dach_0 - vergleichswert) / s_dach_B_0, 3)  # 0 ist eigl b_1 aber wird immer mit 0 gerechnet?!

if operator == "=":
    H_0 = "ß_0 {0} {1}".format("=", vergleichswert)
    H_1 = "ß_0 {0} {1}".format("≠", vergleichswert)
    KW = round(t.ppf(1 - 𝛼 / 2, n - 2), 4)
    KW_satz = "+/-t_[1 - {0}/2; {1} - 2] = {2}".format(𝛼, n, KW)
    KB = "[-∞; -{0}] ∩ [{0}; +∞]".format(KW)
    if T < KW:
        antwortsatz = "T∉K -> H_0 kann nicht verworfen werden. {0} hat keinen signifikanten Einfluss auf {1}.".format(X, Y)
    else:
        antwortsatz = "T∈K -> Damit wird die H_0 zum vorliegenden Signifikanzniveau verworfen. " \
                      "Es kann ein signifikanter linearer Zusammenhang zwischen {0} und {1} angenommen werden.)".format(X, Y)
elif operator == ">":
    H_0 = "ß_0 {0} {1}".format("<=", vergleichswert)
    H_1 = "ß_0 {0} {1}".format(">", vergleichswert)
    KW = round(t.ppf(1 - 𝛼, n - 2), 4)
    KW_satz = "t_[1 - {0}; {1} - 2] = {2}".format(𝛼, n, KW)
    KB = "[{0}; +∞]".format(KW)
    if T < KW:
        antwortsatz = "T∉K -> H_0 kann nicht verworfen werden. {0} hat keinen signifikanten Einfluss auf {1}.".format(X, Y)
    else:
        antwortsatz = "T∈K -> Damit wird H_0 zum vorliegenden Signifikanzniveau verworfen. " \
                      "Es kann ein signifikanter linearer Zusammenhang zwischen {0} und {1} angenommen werden.".format(X, Y)
elif operator == "<":
    H_0 = "ß_0 {0} {1}".format(">=", vergleichswert)
    H_1 = "ß_0 {0} {1}".format("<", vergleichswert)
    KW = round(t.ppf(𝛼, n - 2), 4)
    KW_satz = "t_[{0}; {1} - 2] = {2}".format(𝛼, n, KW)
    KB = "[-∞; {0}]".format(KW)
    if T > KW:
        antwortsatz = "T∉K -> H_0 kann nicht verworfen werden. {0} hat keinen signifikanten Einfluss auf {1}.".format(X, Y)
    else:
        antwortsatz = "T∈K -> Damit wird H_0 zum vorliegenden Signifikanzniveau verworfen. " \
                      "Es kann ein signifikanter linearer Zusammenhang zwischen {0} und {1} angenommen werden.".format(X, Y)


print("s_dach_B_0 = WURZEL(({0} * 1/{1} * {2})/({1} * {3}) = {4}".format(s_hoch2_E, n, summe_x_hoch2_v, š_hoch2_x, s_dach_B_0))
print("H_0: {0}".format(H_0))
print("H_1: {0}".format(H_1))
print("T = ({0} - {1})/{2} = {3}".format(ß_dach_0, vergleichswert, s_dach_B_0, T))
print("KW = {0}".format(KW_satz))
print("KB = {0}".format(KB))
print(antwortsatz)

print("--------------------")
print("2) Frage: Interpretation von ß_dach_0 und ß_dach_1.")
print("")

ß_dach_0_interpretation = "ß_dach_0 gibt den Schnittpunkt mit der Y-Achse an. Dadurch wissen wir welchen Wert " \
                          "ß_dach_0 annimmt, wenn ß_dach_1 = 0 ist. Für unseren Fall bedeutet das, dass {0} den Wert " \
                          "{1} betragen, wenn {2} = 0 ist.".format(Y, ß_dach_0, X)

if ß_dach_1 > 0:
    ß_dach_1_interpretation = "Je mehr {0}, desto größer {1} und zwar um {2} je Einheit.".format(X, Y, ß_dach_1)
else:
    ß_dach_1_interpretation = "Je mehr {0}, desto kleiner {1} und zwar um {2} je Einheit.".format(X, Y, ß_dach_1)

print(ß_dach_0_interpretation)
print("ß_dach_1 Interpretation: {0}".format(ß_dach_1_interpretation))


print("--------------------")
print("3) Frage: Interpretieren Sie das Bestimmtheitsmaß der Regression?"
      "Plausbilitätsprüfung.")
print("")

R_hoch2_prozent = R_hoch2 * 100
if R_hoch2_prozent < 40:
    modellgüte = "geringe Modellgüte"
elif R_hoch2_prozent < 60:
    modellgüte = "mitelhohe Modellgüte"
elif R_hoch2_prozent < 80:
    modellgüte = "hohe Modellgüte"
else:
    modellgüte = "sehr hohe Modellgüte"
print("{0}% der Gesamtstreuung der linearen Regression bzw. des linearen Modells werden erklärt. "
      "Es liegt eine {1} vor.".format(R_hoch2_prozent, modellgüte))
