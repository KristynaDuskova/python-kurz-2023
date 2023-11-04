# Úkol 4
# Zadání
# Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:
#Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
#Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
#Tvůj program bude obsahovat dvě funkce:
#První funkce ověří telefonní číslo. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). Funkce ověří, jestli je číslo platné. Pokud je platné, vrátí hodnotu True, jinak vrátí hodnotu False.
#Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
#Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživateli


import math

def is_correct(number):
    digits = len(number)

    if digits == 9:
        return True
    elif digits == 13:
        if number[0:4] == "+420":
            return True
        else:
            return False
    else:
        return False

def calculate(sms):
    count = len(sms)

    return 3 * math.ceil(count / 180)


program = input("Zadejte své číslo: ")

if is_correct(program):
    print("Vaše číslo je v pořádku.")
else:
    print("Číslo je špatně zapsané!")
    exit()

sms = input("Napište zprávu: ")
price = calculate(sms)

print("Cena:", price, "kč")
