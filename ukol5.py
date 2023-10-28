# Úkol 5

teploty_1 = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]


#Vytvoř seznam průměrných teplot pro každý den
#Tady jsi nám ukazoval, že si máme importovat statistiku a pomocí mean vypočítat průměr.

import statistics
prumer = [statistics.mean(stupen) for stupen in teploty_1]
print(prumer)

#Vytvoř seznam ranních teplot
ranni_teplota = [stupen [0] for stupen in teploty_1]
print(ranni_teplota)
#Vytvoř seznam nočních teplot
nocni_teplota = [stupen [3] for stupen in teploty_1]
print(nocni_teplota)
#Vytvoř seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu
"""
Tohle je špatně, ale nechám to tady, aby bylo vidět, jak postupuji. Či-li je blbost sčítat, ale stačí přidat čárku.
poledni_a_nocni_teploty = [stupen [1] + stupen [3] for stupen in teploty]
print(poledni_a_nocni_teploty)
"""
poledni_a_nocni_teploty = [[stupen [1], stupen [3]] for stupen in teploty_1]
print(poledni_a_nocni_teploty)

#Jenom mám otázku, proč jsi ve svém programu psal stupen -1 a ne stupen 3? Jaký je rozdíl?


