print("Witaj w grze papier, kamien, nozyce")

gracz_1 = input("Podaj imię gracza 1 : " )
gracz_2 = input("Podaj imię gracza 2: ")

gracz_1_odp = input(" %s: Wybierz kamien, papier lub nozyce: " % gracz_1)
gracz_2_odp = input(" %s: Wybierz kamien, papier lub nozyce: " % gracz_2)

def porownaj( odpowiedz_1 , odpowiedz_2):
    if odpowiedz_1 == odpowiedz_2:
        return ("remis")
    elif odpowiedz_1 == "kamien":
        if odpowiedz_2 == "papier":
            return("Wygrywa papier")
        else:
            return("Wygrywa kamien")
            
    elif odpowiedz_1 == "nozyce":
        if odpowiedz_2 == "kamien":
            return("Wygrywa kamien")
        else:
            return("Wygrywa papier")

    elif odpowiedz_1 == "papier":
        if odpowiedz_2 == "nozyce":
            return("Wygrywaja nozyce")
        else:
            return("Wygrywa kamien")
         
        





print(porownaj(gracz_1_odp, gracz_2_odp))
