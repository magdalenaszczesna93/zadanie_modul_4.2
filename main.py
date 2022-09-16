#przykłady palindromów: „Ala”, „Kajak”, 
# „Kobyła ma mały bok”, 
# „Może jutro ta dama da tortu jeżom”, 
# „Wódy żal dla Żydów”, 
# „Wół utył i ma miły tułów”, 
# „malajalam” – to taki język 🙂 
# jednocześnie jest to najdłuższe słowo palindrom 
# w języku polskim, 
# „687454786” – liczba też może być palindromem.

def is_Palindrom(s1):
    for character in s1:
        if character.isalnum(): #sprawdzamy czy znaki we frazie są alfanumeryczne
            #zwraca wartość true albo false
            s2 = ""
            s2 += character.lower() #zmieniamy wszystkie literki, 
            n = len(s2) #zmienna pomocnicza przechowujaca dlugosc slowa
            for i in range(n-1):
                if s2[i] == s2[n-1-i]: #jezeli znak po przeciwnej stronie 
                    #(w tej samej kolejnosci od konca) 
                    return True; #jezeli nie napotkano problemow, 
                    #zwroc true return(x)
print("Program sprawdzajacy czy slowo jest palindromem")
print("Podaj slowo")
s1 = input() #pobieramy slowo
print("Podane slowo " + ("jest " if(is_Palindrom(s1)) else "nie jest ") + "palindromem")