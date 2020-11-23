import numbers
import statistics
# CHOOSE 'CECHA CIĄGŁA, CECHA PUNKTOWA'


def menu():
    """
    MENU
    """
    print("Choose a type of stat: ")
    print("\n")
    print("1. - Punktowa, 2. - Ciągła")
    choice = input()

    """
    INPUT
    """
    input_string = input("Enter a list elements separated by space: ")
    print("\n")
    pktList = input_string.split()
    print("User list is 'pkt': ", pktList)
    return choice, pktList


def divide_chunks(pktList, n):
    """
    PREP A LIST for 'Ciągła'
    """
    cglList = pktList
    for i in range(0, len(cglList), n):
        yield cglList[i:i+n]
    n = 5
    cglList = list(divide_chunks(cglList, 2))
    print("User list is 'cgl': ", cglList)
    return cglList
    
    
    # if menu.choice == 1:
    #     print("Prep list: ", pktList)
    #     return pktList
    # else:
    #     print("Prep list: ", cglList)
    #     return cglList
    
    
menu()
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
