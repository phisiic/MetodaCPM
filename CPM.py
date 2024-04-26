from Node import Czynnosc, Zdarzenie, clear_folder
from Diagram import create_diagram

class CPM:
    def __init__(self, ilosc_zdarzen, zdarzenia, ilosc_czynnosci, czynnosci):
        self.ilosc_zdarzen = ilosc_zdarzen + 1
        self.ilosc_czynnosci = ilosc_czynnosci
        self.zdarzenia = zdarzenia
        self.czynnosci = czynnosci

        # Calculate ti for each event
        for czynnosc in self.czynnosci:
            if czynnosc.before.ti + czynnosc.duration > czynnosc.after.ti:
                czynnosc.after.ti = czynnosc.before.ti + czynnosc.duration

        czynnosci[-1].after.tj = czynnosci[-1].after.ti

        # Calculate tj for each event
        for czynnosc in reversed(czynnosci):
            if czynnosc.after.tj - czynnosc.duration < czynnosc.before.tj or czynnosc.before.tj == 0:
                czynnosc.before.tj = czynnosc.after.tj - czynnosc.duration

        for zdarzenie in zdarzenia:
            zdarzenie.float = zdarzenie.tj - zdarzenie.ti

        for czynnosc in self.czynnosci:
            print(czynnosc.name, czynnosc.before.ti, czynnosc.before.tj, czynnosc.after.ti, czynnosc.after.tj)

        sciezka_krytyczna = []
        for zdarzenie in zdarzenia:
            if zdarzenie.float == 0:
                sciezka_krytyczna.append(zdarzenie)

        for zdarzenie in zdarzenia:
            if zdarzenie.id != "0":
                zdarzenie.draw()
                # print(zdarzenie)

        # print("Sciezka krytyczna:")
        # for zdarzenie in sciezka_krytyczna:
        #     print(zdarzenie.id)

        # Define a dictionary to store events leading into each event
        events_leading_to = {z.id: [] for z in zdarzenia}

        # Populate the dictionary with events leading into each event
        for czynnosc in czynnosci:
            events_leading_to[czynnosc.after.id].append(czynnosc.before)

        # Print events leading into each event
        # for zdarzenie in zdarzenia:
        #     if zdarzenie.id != "0" and zdarzenie.id != "1":
        #         print(f"Events leading into Zdarzenie {zdarzenie.id}:")
        #         for event in events_leading_to[zdarzenie.id]:
        #             print(event.id)

        create_diagram(events_leading_to, zdarzenia, sciezka_krytyczna)