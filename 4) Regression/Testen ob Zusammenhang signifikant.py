import math
from scipy.stats import t

"Testen/Überprüfen Sie, ob der lineare Zusammenhang zwischen X und Y zum Signifikanzniveau von 𝛼=????% signifikant ist."
"Testen Sie, ob der lineare Zusammenhang zwischen kognitiver und körperlicher Leistungsfähigkeit signifikant positiv ist (𝛼 = 0.01)"

# Immer Hypothesentest für ß_1 und immmer beidseitig (S.50 / 51)
"""Eingabe"""
Y = "kognitive Leistungsfähigkeit"
X = "körperliche Leistungsfähigkeit"
operator = ">"
𝛼 = 0.01
n = 323
š_y = round(math.sqrt(218.452), 3)
š_x = round(math.sqrt(277.828), 3)
ß_dach_1 = 0.048
ß_dach_0 = 13.504
R_hoch2 = 0.0029


s_hoch2_E = round(n / (n - 2) * š_y * š_y * (1 - R_hoch2), 3)     # Wurzel daraus ist der Standardfehler der Residuen
s_dach_B_1 = round(math.sqrt(s_hoch2_E) / (math.sqrt(n) * š_x), 3)
T = round((ß_dach_1 - 0) / s_dach_B_1, 3)  # 0 ist eigl b_1 aber wird immer mit 0 gerechnet?!

if operator == "=":
    H_0 = "H_0: ß_1 ≠ 0"
    H_1 = "H_1: ß_1 = 0"
    KW = round(t.ppf(1 - 𝛼/2, n-2), 4)
    KW_satz = "+/-t_[1 - {0}/2; {1} - 2] = {2}".format(𝛼, n, KW)
    KB = "[-∞; -{0}] v [{0}; +∞]".format(KW)
    if T < KW:
        antwortsatz = "T∉K -> H_0 kann nicht verworfen werden. Der lineare Zusammenhang zwischen {0} und {1} ist nicht signifikant positiv.".format(X, Y)
    else:
        antwortsatz = "T∈K -> Damit wird die H_0 zum vorliegenden Signifikanzniveau verworfen. " \
                      "Der lineare Zusammenhang zwischen {0} und {1} ist signifikant positiv.".format(X, Y)
elif operator == ">":
    H_0 = "H_0: ß_1 <= 0"
    H_1 = "H_1: ß_1 > 0"
    KW = round(t.ppf(1 - 𝛼, n-2), 4)
    KW_satz = "t_[1 - {0}; {1} - 2] = {2}".format(𝛼, n, KW)
    KB = "[{0}; +∞]".format(KW)
    if T < KW:
        antwortsatz = "T∉K -> H_0 kann nicht verworfen werden. Der lineare Zusammenhang zwischen {0} und {1} ist nicht signifikant negativ.".format(X, Y)
    else:
        antwortsatz = "T∈K -> Damit wird die H_0 zum vorliegenden Signifikanzniveau verworfen. " \
                      "Der lineare Zusammenhang zwischen {0} und {1} ist signifikant negativ.".format(X, Y)
elif operator == "<":
    H_0 = "H_0: ß_1 >= 0"
    H_1 = "H_1: ß_1 < 0"
    KW = round(t.ppf(𝛼, n-2), 4)
    KW_satz = "t_[{0}; {1} - 2] = {2}".format(𝛼, n, KW)
    KB = "[-∞; {0}]".format(KW)
    if T < KW:
        antwortsatz = "T∉K -> H_0 kann nicht verworfen werden. {0} hat keinen signifikanten Einfluss auf {1}.".format(X, Y)
    else:
        antwortsatz = "T∈K -> Damit wird die H_0 zum vorliegenden Signifikanzniveau verworfen. " \
                      "Es kann ein signifikanter linearer Zusammenhang zwischen {0} und {1} angenommen werden.)".format(X, Y)

print("𝛼 = {0}".format(𝛼))
print("H_0: {0}".format(H_0))
print("H_1: {0}".format(H_1))
print("s²_E = {0}/({0} - 2) * {1}² * (1 - {2}) = {3}".format(n, š_y, R_hoch2, s_hoch2_E))
print("s_dach_B_1 = WURZEL({0})/(WURZEL({1}) * {2}) = {3}".format(s_hoch2_E, n, š_x, s_dach_B_1))
print("T = ({0} - {1})/{2} = {3}".format(ß_dach_1, 0, s_dach_B_1, T))
print("KW = {0}".format(KW_satz))
print("KB = {0}".format(KB))
print(antwortsatz)

print("")
print("WEITERE AUFGABE DAZU: Interpretieren des Ergebnis (man soll scheinbar das Bestimmtheitsmaß angeben) / Plausbilitätsprüfung.")
print("")

#R_hoch2 = round(r_xy * r_xy, 4)
R_hoch2_prozent = R_hoch2 * 100
if R_hoch2_prozent < 40:
    modellgüte = "geringe Modellgüte"
elif R_hoch2_prozent < 60:
    modellgüte = "mitelhohe Modellgüte"
elif R_hoch2_prozent < 80:
    modellgüte = "hohe Modellgüte"
else:
    modellgüte = "sehr hohe Modellgüte"
#print("R² = {0}² = {1}".format(r_xy, R_hoch2))
print("{0}% der Gesamtstreuung der linearen Regression bzw. des linearen Modells werden erklärt. "
      "Es liegt eine {1} vor.".format(R_hoch2_prozent, modellgüte))