# CPM Method
Critical Path Method generation program, written in Python with matplotlib and diagrams. Python Django used for the web app to make it interactive.

Example usage:

Input file formatted like this:

10

9

A,3,1,2

B,4,2,3

C,6,2,4

D,7,3,5

E,1,5,7

F,2,4,7

G,3,4,6

H,4,6,7

I,1,7,8

J,2,8,9


Where:
* 10 - number of activities (czynnosci)
* 9 - number of events (zdarzenia)
* A - activity name
* 3 - activity duration
* 1 - event before
* 2 - event after

And the script will generate this sort of CPM Diagram:

 ![image](https://github.com/phisiic/MetodaCPM/assets/63189115/75af5f6f-c470-4b97-80b4-af9c25f36cf1)

## To run
Activate a virtual environment and use the command
*python main.py <name_of_csv_file>*

