def rakna_vokaler(text):
    vokaler = "aeiouåäöAEIOUÅÄÖ"  # Lista på vokaler både små och stora
    # din kod här
    antal_vokaler = 0
    for bokstav in text:
        if bokstav in vokaler:
            antal_vokaler += 1
    return antal_vokaler

# Exempel:
text = "Hej världen"
print(rakna_vokaler(text))
# Output: 3
