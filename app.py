
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
    userList = input_string.split()
    print("User list is: ", userList)

    """
    PREP A LIST
    """
    def divide_chunks(userList, n):
        for i in range(0, len(userList), n):
            yield userList[i:i+n]
    n = 5
    cglList = list(divide_chunks(userList, 2))
    # pktList =
    
    if choice == 1:
        print(pktList)
        return pktList
    else:
        print(cglList)
        return cglList


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
