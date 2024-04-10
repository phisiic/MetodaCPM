from Node import Czynnosc, Zdarzenie, clear_folder

ilosc_czynnosci = 18
ilosc_zdarzen = 10

# Define events
zdarzenia = []
zdarzenia.append(Zdarzenie(id="0"))
zdarzenia.append(Zdarzenie(id="1", ti=0))  # Start event - indeksowanie od 1 do N
for i in range(2, ilosc_zdarzen + 1):
    zdarzenia.append(Zdarzenie(id=str(i)))

clear_folder("nodes")

# Define activities and append them to the array
czynnosci = []
czynnosci.append(Czynnosc(name="A", duration=5, before=zdarzenia[1], after=zdarzenia[2]))
czynnosci.append(Czynnosc(name="B", duration=10, before=zdarzenia[1], after=zdarzenia[3]))
czynnosci.append(Czynnosc(name="C", duration=3, before=zdarzenia[1], after=zdarzenia[4]))
czynnosci.append(Czynnosc(name="D", duration=12, before=zdarzenia[1], after=zdarzenia[5]))
czynnosci.append(Czynnosc(name="E", duration=10, before=zdarzenia[2], after=zdarzenia[5]))
czynnosci.append(Czynnosc(name="F", duration=23, before=zdarzenia[2], after=zdarzenia[6]))
czynnosci.append(Czynnosc(name="G", duration=5, before=zdarzenia[3], after=zdarzenia[4]))
czynnosci.append(Czynnosc(name="H", duration=3, before=zdarzenia[3], after=zdarzenia[5]))
czynnosci.append(Czynnosc(name="I", duration=16, before=zdarzenia[3], after=zdarzenia[7]))
czynnosci.append(Czynnosc(name="J", duration=9, before=zdarzenia[3], after=zdarzenia[8]))
czynnosci.append(Czynnosc(name="K", duration=7, before=zdarzenia[4], after=zdarzenia[8]))
czynnosci.append(Czynnosc(name="L", duration=9, before=zdarzenia[5], after=zdarzenia[6]))
czynnosci.append(Czynnosc(name="M", duration=12, before=zdarzenia[5], after=zdarzenia[7]))
czynnosci.append(Czynnosc(name="N", duration=20, before=zdarzenia[6], after=zdarzenia[10]))
czynnosci.append(Czynnosc(name="O", duration=13, before=zdarzenia[7], after=zdarzenia[9]))
czynnosci.append(Czynnosc(name="P", duration=18, before=zdarzenia[7], after=zdarzenia[10]))
czynnosci.append(Czynnosc(name="Q", duration=15, before=zdarzenia[8], after=zdarzenia[9]))
czynnosci.append(Czynnosc(name="R", duration=10, before=zdarzenia[9], after=zdarzenia[10]))

# Calculate ti for each event
for czynnosc in czynnosci:
    if czynnosc.before.ti + czynnosc.duration > czynnosc.after.ti:
        czynnosc.after.ti = czynnosc.before.ti + czynnosc.duration

czynnosci[-1].after.tj = czynnosci[-1].after.ti

# Calculate tj for each event
for czynnosc in reversed(czynnosci):
    if czynnosc.after.tj - czynnosc.duration < czynnosc.before.tj or czynnosc.before.tj == 0:
        czynnosc.before.tj = czynnosc.after.tj - czynnosc.duration

for zdarzenie in zdarzenia:
    zdarzenie.float = zdarzenie.tj - zdarzenie.ti

sciezka_krytyczna = []
for zdarzenie in zdarzenia:
    if zdarzenie.float == 0:
        sciezka_krytyczna.append(zdarzenie)

for zdarzenie in zdarzenia:
    if zdarzenie.id != "0":
        zdarzenie.draw()
        print(zdarzenie)

print("Sciezka krytyczna:")
for zdarzenie in sciezka_krytyczna:
    print(zdarzenie.id)