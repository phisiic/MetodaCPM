import csv
from Node import Czynnosc, Zdarzenie, clear_folder

def read_csv(filename):
    czynnosci = []
    zdarzenia = []

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        ilosc_czynnosci = int(next(reader)[0])
        ilosc_zdarzen = int(next(reader)[0])

    zdarzenia.append(Zdarzenie(id="0"))
    zdarzenia.append(Zdarzenie(id="1", ti=0))
    for i in range(2, ilosc_zdarzen + 1):
        zdarzenia.append(Zdarzenie(id=str(i)))


    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the first two lines
        next(reader)
        for row in reader:
            name, duration, before_id, after_id = row
            duration = int(duration)
            before_event = zdarzenia[int(before_id)]
            after_event = zdarzenia[int(after_id)]
            activity = Czynnosc(name=name, duration=duration, before=before_event, after=after_event)
            czynnosci.append(activity)

    return ilosc_zdarzen, zdarzenia, ilosc_czynnosci, czynnosci