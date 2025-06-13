TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
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

print("""projekt_1.py: první projekt do Engeto Online Python Akademie
      
author: Kristýna Hanáčková
email: hanackova.kr@gmail.com
""")

uzivatele = {'bob':'123', 'ann':'pass123', 'mike':'password123', 'liz':'pass123'}

jmeno = input('Enter your username: ')
heslo = input('Enter your password: ')

if jmeno in uzivatele and heslo in list(uzivatele.values()):
    print(f'''
username: {jmeno}
password: {heslo}
{50*'-'}
Welcome to the app, {jmeno}. 
We have 3 texts to be analyzed.
{50*'-'}''')
else:
    print(f'''
username: {jmeno}
password: {heslo}
Unregistered user, terminating the program.''')
    exit()
 
ocislovane_texty = {}
for indexy, TEXTS in enumerate(TEXTS, start=1):
    ocislovane_texty[indexy] = TEXTS

cislo_textu = input('Enter a number btw. 1 and 3 to select: ')

if cislo_textu.isdigit(): # podminka input musí být číslo
    cislo_textu = int(cislo_textu)
else:
    print('1- Unknown entered value, terminating the program.')
    exit()

if cislo_textu not in ocislovane_texty.keys(): # podmínka input musí být 1-3
    print('2 -Unknown entered value, terminating the program.')
    exit()

vybrany_text = ocislovane_texty.get(cislo_textu, 'chyba')
seznam_slov = vybrany_text.split()
velke_prvni_pismeno = [slovo for slovo in seznam_slov if slovo.istitle()]
velka_pismena = [slovo for slovo in seznam_slov if slovo.isupper()]
mala_pismena = [slovo for slovo in seznam_slov if slovo.islower()]
cisla_v_textu = [slovo for slovo in seznam_slov if slovo.isdigit()]

suma = 0 
for cislo in cisla_v_textu:
    if cislo.isdigit():
        suma += int(cislo)

cetnosti = dict()
for slovo in seznam_slov:
    slovo_bez_tecky_carky = slovo.strip(',.')
    if len(slovo_bez_tecky_carky) not in cetnosti:
        cetnosti[len(slovo_bez_tecky_carky)] = 1
    else:
        cetnosti[len(slovo_bez_tecky_carky)] += 1

print(f'''
{50*'-'}
There are {len(seznam_slov)} words in the selected text.
There are {len(velke_prvni_pismeno)} titlecase words.
There are {len(velka_pismena)} uppercase words.
There are {len(mala_pismena)} lowercase words.
There are {len(cisla_v_textu)} numeric strings.
The sum of all the numbers {suma}
{50*'-'}
LEN | OCCURENCE    | NR. 
{50*'-'}
''')

for delka, pocet in sorted(cetnosti.items()):
    print(f'{delka}| {"*" * pocet}| {pocet}')
 




 

    


