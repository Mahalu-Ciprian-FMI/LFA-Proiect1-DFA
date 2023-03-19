
f=open('dfa.in','r') #deschidem fisierul
for i,line in enumerate(f): #citim din fisier linie cu linie,si actualizam DFA-ul de tip tuplu,in afara de functia de tranzitie
    if i==0:
        Q=line.split()
    if i==1:
        sigma=line.split()
    if i==2:
        start=line.strip()
    if i==3:
        final=line.split()
    if i==4:
        cuvant=line
    if i>=5:
        break;
delta={} # Initializam un dictionar ce reprezinta functia de tranzitie
for state in Q:
    for char in sigma:
        print(f"{state}  --{char}-->  ",end="") # pentru a arata frumos in console
        destinatie=input() # citim de la tastatura functia de tranzitie
        if (destinatie.lower())=="stop":  # stop reprezinta un dead end
            delta[(state,char)]=-1    # daca avem dead end, vom reprezenta acest dead end cu valoarea -1
        else:
            delta[(state,char)]=destinatie  # daca nu avem dead end, adaugam in delta starea in care se ajunge dintr-o anumita stare cu un anumit caracter din alfabet
#print(Q)
#print(sigma)
#print(start)
#print(final)
#print(cuvant)
#print(delta)
stare_curenta=start # initializam "stare_curenta" cu starea initiala
drum=start + "-->" # pentru a afisa drumul impreuna cu starea initiala
for litera in cuvant:
    stare_curenta=delta[(stare_curenta,litera)] # ii dam lui stare curenta valoarea din interiorul dictionarului, care va corespunde defat cu ce avem in "destinatie".
    if stare_curenta==-1: #se verifica daca avem drum direct, daca nu break, daca da, linia 38
        break # pentru a nu continua citirea daca cuvantul nu este acceptat
    else:
        drum=drum+ stare_curenta + "-->"
if stare_curenta in final: # daca odata ce am terminat de citit cuvantul, starea in care a ajuns la final este acceptata de catre limbaj,afisam drumul si mesajul "Acceptat"
    print("Acceptat")
    drum=drum[:len(drum)-3] #stergem ultimele 3 caractere (ultima sageata) folosind splices
    print(drum)
else:
    print("Neacceptat") # daca am dat de un drum direct invalid/inexistent sau starea in care am ajuns nu este finala


