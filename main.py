from Node import Czynnosc, Zdarzenie, clear_folder
from CPM import CPM
from csv_read import read_csv

clear_folder("nodes")

ilosc_zdarzen, zdarzenia, ilosc_czynnosci, czynnosci = read_csv("nodes.csv")

cpm_diagram = CPM(ilosc_zdarzen, zdarzenia, ilosc_czynnosci, czynnosci)
