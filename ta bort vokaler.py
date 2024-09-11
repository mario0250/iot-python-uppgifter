def ta_bort_vokaler(text):
    vokaler = "aeiouåäöAEIOUÅÄÖ"  # Lista på vokaler både små och stora
    # din kod här
    ny_mening = ''

    for bokstav in text:
        if bokstav not in vokaler:
           ny_mening += bokstav
    return ny_mening




# Exempel:
text = "Hej världen"
print(ta_bort_vokaler(text))
# Output: "Hj vrldn"
