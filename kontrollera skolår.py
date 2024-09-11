year = int(input('Skriv in ett årtal för att kontrollera om det är ett skottår: '))


if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "är ett skottår.")
else:
    print(year, "är inte ett skottår.")
