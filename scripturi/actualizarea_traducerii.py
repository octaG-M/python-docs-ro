# Presupunem instalate pachetele: poutils, polib
# Vezi: [ https://pypi.org/project/poutils/ ]
#       [ https://pypi.org/project/polib/ ]
#
# Periodic, trebuie (re)generate fisierele [ *.pot ] ale documentatiei.
# Actualizarea fisierelor [ *.po ] cu traduceri (vechi), in raport cu 
# noile fisiere [ *.pot ], se realizeaza, dintr-un terminal PowerShell, 
# cu comanda:
#
# sphinx-intl update -p build/gettext -l ro
#
# La actualizare, vor fi INSERATE comentarii "#, fuzzy" in fragmentele
# care trebuie (eventual) modificate/actualizate/sterse.
#
# (Meta)Pachetul poutils, prin scriptul potodo (.exe), ofera statistici 
# privind aceste intrari FUZZY (adica, fragmentele de verificat), respectiv 
# intrarile NETRADUSE din continutul unor fisiere [ *.po ].
#
# Utilizarea lui potodo din poutils: deschidem un terminal PowerShell in 
# directorul fisierelor [ *.po ] si rulam comanda 
# (vezi https://git.afpy.org/AFPy/potodo/src/branch/main/potodo/arguments_handling.py):
#
# potodo -c -f
#
# Optiunea [ c ] se refera la fragmentele netraduse inca, optiunea [ f ] la
# fragmentele fuzzy.
#
# Atunci cand dorim sa localizam, intr-un fisier [ *.po ], fragmentele fuzzy,
# putem folosi, deschizand interpretorul de Python in directorul fisierului, 
# biblioteca polib
# (vezi https://polib.readthedocs.io/en/latest/quickstart.html#more-examples,
#  respectiv https://git.afpy.org/AFPy/potodo/src/commit/a108154acf9afc5e4f386943da5a26ddd0c8ec6e/potodo/po_file.py#L71):

import polib
fisierul_po = polib.pofile('./numele_fisierului.po')
for intrare in fisierul_po.fuzzy_entries():
    print(intrare.msgid, intrare.msgstr)
for intrare in fisierul_po.untranslated_entries():
    print(intrare.msgid, intrare.msgstr)


