# úkol 2
sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

print(sklad)


soucastka = input("Zadej soucastku: ")
if soucastka in sklad:
    print(f" Ve skladu máme {sklad[soucastka]} ks.")
else:
    print(f"Bohužel součástku {soucastka} neprodáváme.")

kusy = int(input(" Chci kusů: "))
if kusy > sklad[soucastka]:
    print(f" Nemáme dostatek kusů. ")
else:
    print(f" Poptávku je možné zařídit. ")



# uprava zaznamu
sklad[soucastka] = (sklad[soucastka] - kusy)
print(sklad)
"""
# odebrani zaznamu
kusy_soucastky = sklad.pop("BC547C")
"""



#Bonus1 ani Bonus2 jsem nezvládla
