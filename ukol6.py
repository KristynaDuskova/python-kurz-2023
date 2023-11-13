#Úkol 6
"""
class Auto:
    registracni_znacka = ""
    typ_vozidla = ""
    najete_km = ""

peugeot = Auto ()
peugeot.registracni_znacka = "4A2 3020"
peugeot.typ_vozidla = "Peugeot 403 Cabrio"
peugeot.najete_km = "47534"

octavia = Auto ()
octavia.registracni_znacka = "1P3 4747"
octavia.typ_vozidla = "Škoda Octavia"
octavia.najete_km = "41253"

print(octavia.registracni_znacka)

class Auto:
    def get_info(self):
        return f"Auto se značkou {self.registracni_znacka} typu {self.typ_vozidla} s {self.najete_km} najetými kilometry je dostupné."

"""

class Auto:
    registracni_znacka = ""
    typ_vozidla = ""
    najete_km = ""

    def __init__(self, znacka, typ, km):
        self.registracni_znacka = znacka
        self.typ_vozidla = typ
        self.najete_km = km
        return
    
    def get_info(self):
        return f"Auto se značkou {self.registracni_znacka} typu {self.typ_vozidla} s {self.najete_km} najetými kilometry je dostupné."
    
    def __str__(self):
        return f"Auto se značkou {self.registracni_znacka} typu {self.typ_vozidla} s {self.najete_km} najetými kilometry je dostupné"

    def deliver(self):
        if self.dostupnost == "dostupne":
            return "Auto je dostupné."
        else:
            self.dostupnost = "nedostupne"
            return "Auto není k dispozici."

peugeot = Auto("4A2 3020","Peugeot 403 Cabrio", "47534")
octavia = Auto("1P3 4747","Škoda Octavia", "41253")
print(peugeot.registracni_znacka)

print(peugeot.get_info())
print(octavia.get_info())