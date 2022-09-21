#przykłady palindromów: „Ala”, „Kajak”, 
# „Kobyła ma mały bok”, 
# „Może jutro ta dama da tortu jeżom”, 
# „Wódy żal dla Żydów”, 
# „Wół utył i ma miły tułów”, 
# „malajalam” – to taki język 🙂 
# jednocześnie jest to najdłuższe słowo palindrom 
# w języku polskim, 
# „687454786” – liczba też może być palindromem.

def is_palindrom(text):
    text = text.lower()    # zamieniam na małe litery
    text = [character for character in text if character.isalnum()]  # wybieram tylko litery i cyfry
    # teraz jest to lista, ale to nie szkodzi    
    return text == text[::-1]  # sprawdzam czy text to to samo co text wspak 
    
print("Program sprawdzajacy czy slowo jest palindromem")
print("Podaj slowo")
text = input() #pobieramy slowo
print("Podane slowo " + ("jest " if(is_palindrom(text)) else "nie jest ") + "palindromem")