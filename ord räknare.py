def rakna_ord(text):
    ord_lista= text.split()
    antal_ord= len(ord_lista)
    return antal_ord

    pass

# Exempel:
text = input('Skriv en mening: ')

print(rakna_ord(text))
# Input: "Detta är en mening"
# Output: 4