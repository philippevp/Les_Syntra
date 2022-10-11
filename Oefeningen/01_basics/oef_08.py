

def sum_of_n_natural_numbers(n, including_zero=True):
    sum = 0
    if including_zero:
        for x in range(n):
            sum += x
    else:
        for x in range(n):
            sum += (x+1)
    return sum

aantal_getallen = int(input("Geef een geheel getal"))

print(f"De sum van de eerst {aantal_getallen} nummers (0 incluis) is {sum_of_n_natural_numbers(aantal_getallen)}")
print(f"De sum van de eerst {aantal_getallen} nummers (0 niet meegerekend) is {sum_of_n_natural_numbers(aantal_getallen, False)}")

