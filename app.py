import inquirer
import statistics
import numpy as np
from itertools import islice

# CHOOSE 'CECHA CIĄGŁA, CECHA NASTĘPNA, PUNKTOWA
options = [
    inquirer.List('cecha', 
        message = 'Jaka cecha Xi?',
        choices = ['Punktowa', 'Ciągła'],
    ),
]
answers = inquirer.prompt(options)
print(answers['cecha'])

# IF PUNKTOWA - INPUT X  - list
def statMenu():
    """
    Menu with stat options and inputs
    """
    n = int(input("Enter the size of the list: "))
    print("\n")
    numList = list(int(num) for num in input("Enter the list numbers separated by space ").strip().split())[:n]

    if answers['cecha'] == 'Punktowa':
        # numList = list(int(num) for num in input("Enter the list numbers separated by space ").strip().split())[:n]
        print("User List: ", numList)
        return numList
    else:
        xynumList = iter(numList)
        xynumList = iter(lambda: tuple(islice(numList, n)), ())
        print("User List: ", xynumList)
        return xynumList
statMenu()
        
    #     final_list = [] 
    #     line = int(input("Enter the list of tuples: "))
    #     print("\n")
    #     # WHILE LOOP
    #     while(line != ''): 
    #         final_list.append(tuple(line.split())) 
    #         line = input() 

    #     print(final_list)
    # return final_list
 # else:
   

class Average():
    """
    Count avg of pkt or cgl
    """
    def avgPkt(numList):
        AvgDataPkt = statistics.mean(numList)
        return AvgDataPkt
    
    def avgPkt(final_list):
        AvgDataCgl = statistics.mean(final_list)
        return AvgDataCgl




#IF CIĄGŁA, NASTĘPNA - INPUT (X - Y), (X - Y) - dict

# INPUT NUM OF - Ni, CZYLI ILOŚĆ

# COUNT - ŚREDNIA ARYTMETYCZNA
 
# COUNT - ŚRODEK PRZEDZIAŁÓW - ŚREDNIA ARYTMETYCZNA

# COUNT -  (ŚRODEK PRZEDZIAŁÓW - ŚREDNIA ARYTMETYCZNA)^2 * Ni

# COUNT -  (ŚRODEK PRZEDZIAŁÓW - ŚREDNIA ARYTMETYCZNA)^3 * Ni

# COUNT -  (ŚRODEK PRZEDZIAŁÓW - ŚREDNIA ARYTMETYCZNA)^4 * Ni

# COUNT - ODCHYLENIE STANDARDOWE

# COUNT - WSPÓŁCZYNNIK ZMIENNOŚCI Vx

# COUNT - WSPÓŁCZYNNIK ASYMETRII

# COUNT - WSPÓŁCZYNNIK KONCENTRACJI

# IF CIĄGŁA, NASTĘPNA - COUNT 'ŚRODEK PRZEDZIAŁÓW'
