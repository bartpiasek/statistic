import inquirer

# CHOOSE 'CECHA CIĄGŁA, CECHA NASTĘPNA, PUNKTOWA
options = [
    inquirer.List('cecha', 
    message = 'Jaka cecha Xi?',
    choices = ['Punktowa', 'Ciągła', 'Następna'],
    ),
]
answers = inquirer.prompt(options)
print(answers['cecha'])
# IF PUNKTOWA - INPUT X  - list
if answers['cecha'] == 'Punktowa':
    numberList = []

    n = int(input("Enter the size of the list "))
print("\n")
numberList = list(int(num) for num in input("Enter the list numbers separated by space ").strip().split())[:n]
print("User List: ", numberList)

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
