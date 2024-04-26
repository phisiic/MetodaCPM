import sys
from Node import Czynnosc, Zdarzenie, clear_folder
from CPM import CPM
from csv_read import read_csv

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python main.py <csv_file_path>")
        return

    # Extract the CSV file path from command-line arguments
    csv_file_path = sys.argv[1]

    # Clear the 'nodes' folder
    clear_folder("nodes")

    # Read data from the CSV file
    ilosc_zdarzen, zdarzenia, ilosc_czynnosci, czynnosci = read_csv(csv_file_path)

    # Run the CPM algorithm with the provided data
    cpm_diagram = CPM(ilosc_zdarzen, zdarzenia, ilosc_czynnosci, czynnosci)

if __name__ == "__main__":
    main()
