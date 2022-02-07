import math
from scipy.stats import t
#FS. S. 49

"""Eingabe"""
Y = "kognitive Leistungsfähigkeit"
X = "körperliche Leistungsfähigkeit"
n = 323 # Anzahl Zeilen bzw. n-WErt der Summen
summe_x_v = 941.84 # Summe von x_v
summe_y_v = 17947.45  # Summe von y_v
summe_x_hoch2_v = 18992.01  # Summe von x^2_v
summe_y_hoch2_v = 6570487  # Summe von y^2_v
summe_x_v_mal_y_v = 350110.1  # Summe von x_v * y_v
#S_hoch2_U = 616.942  # S^2_U  wird nicht verwendet

"""Berechnungen"""
x̅ = round(summe_x_v / n, 3)
š_hoch2_x = round(summe_x_hoch2_v / n - x̅ * x̅, 3)   # varianz
š_x = round(math.sqrt(š_hoch2_x), 3)
y̅ = round(summe_y_v / n, 3)
š_hoch2_y = round(summe_y_hoch2_v / n - y̅ * y̅, 3)
š_y = round(math.sqrt(š_hoch2_y), 3)
š_xy = round(1 / n * summe_x_v_mal_y_v - x̅ * y̅, 3)  # Kovarianz (S.14) -> wenn Positiv, d.h. je mehr x desto mehr y

print("Rechenhilfen")
print("x̅ = {0}/{1} = {2}".format(summe_x_v, n, x̅))
print("š²_x = {0}/{1} - {2}² = {3}".format(summe_x_hoch2_v, n, x̅, š_hoch2_x))
print("š_x = wurzel({0}) = {1}".format(š_hoch2_x, š_x))
print("y̅ = {0}/{1} = {2}".format(summe_y_v, n, y̅))
print("š²_y = {0}/{1} - {2}² = {3}".format(summe_y_hoch2_v, n, y̅, š_hoch2_y))
print("š_y = wurzel({0}) = {1}".format(š_hoch2_y, š_y))
print("š_xy = 1/{0} * {1} - {2} * {3} = {4}".format(n, summe_x_v_mal_y_v, x̅, y̅, š_xy))

print("--------------------")
print("1) Frage: Bestimmen Sie einen geeigneten Korrelationskoeffizienten")
print("")

r_xy = round(š_xy / (š_x * š_y), 3)  # Bravais Pearson (S. 14)

print("r_xy = {0}/({1}*{2}) = {3}".format(š_xy, š_x, š_y, r_xy))
print("Ein geeigneter Korrelationskoeffizient ist der Bravais-Pearson. Dieser hat den Wert {0}.".format(r_xy))


print("--------------------")
print("2) Frage: Führen Sie eine lineare Regression der Milchlieferungen als Funktion der Einwohnerzahlen in 1000 durch.")
print("bzw. Ermitteln Sie die Regressiongleichung.")
print("")

ß_dach_1 = round(š_xy / š_hoch2_x, 3)
ß_dach_0 = round(y̅ - ß_dach_1 * x̅, 3)   # Achtung: Für den Fall von Einwohnerzahlen in 1.000 hätte man hier x̅ noch durch die jeweilige Einheit teilen müssen
ŷ = "{0} + {1}x".format(ß_dach_0, ß_dach_1, x̅)  # wenn x um eine Einheit steigt, steigt y um ß_dach_1 Einheiten

print("ß_dach_1 = {0}/{1} = {2}".format(š_xy, š_hoch2_x, ß_dach_1))
print("ß_dach_0 = {0} - {1} * {2} = {3}".format(y̅, ß_dach_1, x̅, ß_dach_0))
print("ŷ = {0}".format(ŷ))


print("--------------------")
print("3) Frage: Wie hoch ist das Bestimmtheitsmaß der Regression?")
print("Interpretieren Sie dieses.")
print("")

R_hoch2 = round(r_xy * r_xy, 4)
R_hoch2_prozent = R_hoch2 * 100
if R_hoch2_prozent < 40:
    modellgüte = "geringe Modellgüte"
elif R_hoch2_prozent < 60:
    modellgüte = "mitelhohe Modellgüte"
elif R_hoch2_prozent < 80:
    modellgüte = "hohe Modellgüte"
else:
    modellgüte = "sehr hohe Modellgüte"
print("R² = {0}² = {1}".format(r_xy, R_hoch2))
print("{0}% der Gesamtstreuung der linearen Regression bzw. des linearen Modells werden erklärt. "
      "Es liegt eine {1} vor.".format(R_hoch2_prozent, modellgüte))


print("--------------------")
print("4) Frage: Interpretieren Sie die Koeffizienten a und b.")
print("Testen/Überprüfen Sie, ob der lineare Zusammenhang zwischen X und Y zum Signifikanzniveau von 𝛼=????% signifikant ist.")
print("")
# Immer Hypothesentest für ß_1 und immmer beidseitig (S.50 / 51)
"""Eingabe"""
𝛼 = 0.01
operator = ">"

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



print("--------------------")
print("5) Frage: Berechnen Sie ein Prognoseintervall der Milchanlieferungen"
      "für eine Gemeinde mit 100.000 Einwohnern (𝛼 = 0.05).")
print("")
#S. 51
"""Eingabe"""
x_B = 25
𝛼 = 0.05

y_dach_0 = round(ß_dach_0 + ß_dach_1 * x_B, 3)
t_verteilung = round(t.ppf(1 - 𝛼/2, n-2), 4)
s_y_dach_0_minus_s_y_0 = round(math.sqrt(s_hoch2_E * (1 + 1 / n + ((x_B - x̅) * (x_B - x̅)) / (n * š_hoch2_x))), 3)
PI_1 = round(y_dach_0 + t_verteilung * s_y_dach_0_minus_s_y_0, 3)
PI_2 = round(y_dach_0 - t_verteilung * s_y_dach_0_minus_s_y_0, 3)
PI = "[{0}; {1}]".format(PI_1, PI_2)

print("x_B = {0}".format(x_B))
print("𝛼 = {0}".format(𝛼))
print("y_dach_0 = {0} + {1} * {2} = {3}".format(ß_dach_0, ß_dach_1, x_B, y_dach_0))
print("t_[1 - {0}/2; {1} - 2] = {2}".format(𝛼, n, t_verteilung))
print("s_y_dach_0-y_0 = WURZEL({0} * (1 + 1/{1} + ({2} - {3})/({1} * {4})) = {5}".format(s_hoch2_E, n, x_B, x̅, š_hoch2_x, s_y_dach_0_minus_s_y_0))
print("PI = [{0} +/- {1} * {2}] = {3}".format(y_dach_0, t_verteilung, s_y_dach_0_minus_s_y_0, PI))
print("NOCH ÜBERARBEITEN!! Mit einer Wahrscheinlichkeit von {0}% liegen bei {1} {2} die {3} zwischen {4} und {5}.".format(1 - 𝛼, x_B, X, Y, PI_1, PI_2 ))


print("--------------------")
print("6) Frage: Berechnen Sie die Streuungszerlegung.")
print("")

TSS = round(n * š_hoch2_y, 3)
RSS = round(TSS * (1 - R_hoch2), 3)
ESS = round(TSS - RSS, 3)

print("TSS = {0} * {1} = {2}".format(n, š_hoch2_y, TSS))
print("RSS = {0} * (1 - {1}) = {2}".format(TSS, R_hoch2, RSS))
print("ESS = {0} - {1} = {2}".format(TSS, RSS, ESS))

print("--------------------")
print("7) Frage: Interpretation von ß_dach_1.")
print("")

if ß_dach_1 > 0:
    ß_dach_1_interpretation = "Je mehr {0}, desto größer {1} und zwar um {2}.".format(X, Y, ß_dach_1)
else:
    ß_dach_1_interpretation = "Je mehr {0}, desto kleiner {1} und zwar um {2}.".format(X, Y, ß_dach_1)
if T > KW:
    ß_dach_1_interpretation += " Dieser Zusammenhang ist signifikant, d.h. wir gehen von einem linearen Zusammenhang aus."
else:
    ß_dach_1_interpretation += " Dieser Zusammenhang ist aber nicht signifikant, d.h. wir gehen nicht von einem linearen Zusammenhang aus."

print("{0}".format(ß_dach_1_interpretation))

