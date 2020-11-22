from statistics import mean
import inquirer
import statistics
import numpy as np
from itertools import islice

# CHOOSE 'CECHA CIĄGŁA, CECHA NASTĘPNA, PUNKTOWA
def menu():
    """
    Chose a type of...
    """
    options = [
        inquirer.List('cecha', 
            message = 'Jaka cecha Xi?',
            choices = ['Punktowa', 'Ciągła'],
        ),
    ]
    answers = inquirer.prompt(options)
    print(answers['cecha'])

    """
    Menu with stat options and inputs
    """
    input_string = input("Enter a list elements separated by space: ")
    print("\n")
    userList = input_string.split()
    print("User list is: ", userList)
    return userList

    # if answers['cecha'] == 'Punktowa':
    #     print('asdf')
    # else:
    #     pass

# IF PUNKTOWA - INPUT X  - list



menu()
        
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
