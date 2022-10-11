

aantal_getallen = int(input('Hoeveel getallen wil je optellen?'))
getallen = []

for x in range(aantal_getallen):
    getallen.append(int(input("Geef getal")))

result = 0
for x in getallen:
    result += x

print(f"De som van deze getallen is {result}")