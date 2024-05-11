# CPM Method
Critical Path Method generation program, written in Python with matplotlib and diagrams. Python Django used for the web app to make it interactive.

## Django WebApp
Django backend combined with HTMX to make it interactive. The webapp allows the user to input the activities and events through dynamic forms or by uploading a csv file. After adding the activities, the server computes the critical path and draws the diagram, after which it is sent to the website. 

**NOTE:** Remove old activities if you wish to make a new diagram, as the old ones aren't deleted.

**Website UI:**
![image](https://github.com/phisiic/MetodaCPM/assets/63189115/28e9114c-eb7c-4fb5-9688-f4eb571127ab)

**After adding a few nodes:**
![image](https://github.com/phisiic/MetodaCPM/assets/63189115/a278a453-7e13-4be0-910b-e49071f6db97)

![image](https://github.com/phisiic/MetodaCPM/assets/63189115/98dacb25-d5f5-46ca-85be-15e4491ac172)

**Generated Diagram:**
![image](https://github.com/phisiic/MetodaCPM/assets/63189115/4e5d4014-4b48-42a1-b9c4-9fd1c159f0c1)

**Uploading CSV file:**
![image](https://github.com/phisiic/MetodaCPM/assets/63189115/cc8c4dc9-b352-4eca-b9bb-8af0acaab460)

## Console CSV version
Example usage:

Input file formatted like this:

```
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
```

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



