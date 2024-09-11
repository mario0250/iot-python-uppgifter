def till_titel_case(text):
    ord_lista = text.split()
    ny_lista = []

    for ord in ord_lista:
        nytt_ord = ord.capitalize()
        ny_lista.append(nytt_ord)
    return " ".join(ny_lista)  

    pass




# Exempel:
text = "hej världen"
print(till_titel_case(text))  # Output: "Hej Världen"

