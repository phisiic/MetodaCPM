from Node import Czynnosc, Zdarzenie, clear_folder
import csv
from Node import Czynnosc, Zdarzenie


def read_input_file(file_path):
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data


def main():
    file_path = input("Podaj ścieżkę do pliku CSV: ")
    data = read_input_file(file_path)

    # Initialize events and activities
    czynnosci = []
    zdarzenia = {}

    # Create activities and events based on input data
    for row in data:
        name = row['name']
        duration = int(row['duration'])
        before_id = row['before']
        after_id = row['after']

        if before_id not in zdarzenia:
            zdarzenia[before_id] = Zdarzenie(id=before_id)
        if after_id not in zdarzenia:
            zdarzenia[after_id] = Zdarzenie(id=after_id)

        before_event = zdarzenia[before_id]
        after_event = zdarzenia[after_id]

        czynnosc = Czynnosc(name=name, duration=duration, before=before_event, after=after_event)
        czynnosci.append(czynnosc)

    # Calculate ti for each event
    for czynnosc in czynnosci:
        if czynnosc.before.ti + czynnosc.duration > czynnosc.after.ti:
            czynnosc.after.ti = czynnosc.before.ti + czynnosc.duration

    # Set tj for the last event
    czynnosci[-1].after.tj = czynnosci[-1].after.ti

    # Calculate tj for each event
    for czynnosc in reversed(czynnosci):
        if czynnosc.after.tj - czynnosc.duration < czynnosc.before.tj or czynnosc.before.tj == 0:
            czynnosc.before.tj = czynnosc.after.tj - czynnosc.duration

    # Calculate float for each event
    for zdarzenie in zdarzenia.values():
        zdarzenie.float = zdarzenie.tj - zdarzenie.ti

    # Find critical path
    sciezka_krytyczna = []
    for zdarzenie in zdarzenia.values():
        if zdarzenie.float == 0:
            sciezka_krytyczna.append(zdarzenie)

    # Print critical path
    print("Zdarzenia:")
    for zdarzenie in sorted(zdarzenia.values(), key=lambda z: int(z.id)):
        print(f"Zdarzenie ID: {zdarzenie.id}, Ti: {zdarzenie.ti}, Tj: {zdarzenie.tj}, Float: {zdarzenie.float}")

    print("\nSciezka krytyczna:")
    for zdarzenie in sorted(sciezka_krytyczna, key=lambda z: int(z.id)):
        print(zdarzenie.id)


if __name__ == "__main__":
    main()