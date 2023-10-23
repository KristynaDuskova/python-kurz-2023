#Úkol 3


import json
with open('body.json', encoding='utf-8') as file:
    absolvents = json.load(file)
print(absolvents)

new_dict = {}
for name in absolvents:
    if absolvents[name] > 60:
        print(name, ": Pass")
    else:
        print(name, ": Fail")



# jenom nevím, jak uložit nový json
new_dict = {}
for name in absolvents:
    if absolvents[name] > 60:
        new_dict[name] = "Pass"
    else:
        new_dict[name] = "Fail"
print(new_dict)

with open("prospech.json", mode="w", encoding="utf-8") as file:
    json.dump(new_dict, file)