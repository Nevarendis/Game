import random

print("Witaj w grze papier, kamień, nożyce")

c = ["kamień", "papier", "nożyce"]


gracz = None
komputer = random.choice(c)


while gracz not in c:
   gracz = input("Wybierz papier, kamień, nożyce: ")


if gracz == komputer:
    print("komputer: ", komputer)
    print("gracz: ", gracz)
    print("Remis")
elif gracz == "kamień":
    if komputer == "papier":
        print("komputer: ", komputer)
        print("gracz: ", gracz)
        print("Przegrałeś")
    if komputer == "nożyce":
        print("komputer: ", komputer)
        print("gracz: ", gracz)
        print("Wygrałeś")
elif gracz == "nożyce":
    if komputer == "kamień":
        print("komputer: ", komputer)
        print("gracz: ", gracz)
        print("Przegrałeś")
    if komputer == "papier":
        print("komputer: ", komputer)
        print("gracz: ", gracz)
        print("Wygrałeś")
elif gracz == "papier":
    if komputer == "nożyce":
        print("komputer: ", komputer)
        print("gracz: ", gracz)
        print("Przegrałeś")
    if komputer == "kamień":
        print("komputer: ", komputer)
        print("gracz: ", gracz)
        print("Wygrałeś")

