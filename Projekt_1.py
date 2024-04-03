

texts = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
oddelovac = "=" * 30
uzivatele = {
  "bob": "123",
  "ann": "pass123",
  "mike": "password123",
  "liz": "pass123",
}

username = input("Uživatelské jméno: ")
password = input("Heslo: ")

if username in uzivatele: 
    print("Welcome to the app," + " " + username)
else:
    print("Špatné uživatelské jméno nebo heslo")
    exit()
print("Níže provedeme analýzu jednoho ze tří textů: ")

volba_uzivatele = int(input("Zadejte číslo textu: 1,2,3: "))
print(oddelovac)

if volba_uzivatele == 1:
    print(texts[0])
    print(oddelovac)
    vybrany_text = texts[0]
elif volba_uzivatele == 2:
    print(texts[1])
    print(oddelovac)
    vybrany_text = texts[1]
elif volba_uzivatele == 3:
    print(texts[2])
    print(oddelovac)
    vybrany_text = texts[2]    
else:
    print("spatny vyber")
    exit()
statistika = vybrany_text.split()
pocet_slov = len(statistika)
print("V textu je: ",pocet_slov,"slov")

filtrovana_slova = []
for slovo in vybrany_text.split():
    slovo = slovo.strip(".,/;").lower()
    if slovo:
        filtrovana_slova.append(slovo)

statistiky_slov = {
    "pocet_slov": len(filtrovana_slova),
    "mala": 0,
    "velka": 0,
    "cisla": 0,
    "velke_pismeno": 0,
    "soucet": 0
}

for i in range(len(filtrovana_slova)):
    if filtrovana_slova[i].istitle():
        statistiky_slov["velke_pismeno"] += 1
    elif filtrovana_slova[i].isupper():
        statistiky_slov["velka"] += 1
    elif filtrovana_slova[i].islower():
        statistiky_slov["mala"] += 1
    elif filtrovana_slova[i].isnumeric():
        statistiky_slov["cisla"] += 1
        statistiky_slov["soucet"] += float(filtrovana_slova[i])

print(statistiky_slov)