def collatz (number):
    if int(number) % 2 == 0:
        result = number // 2
        print(f"{result}" )
        return result
    else:
        result = 3 * number + 1
        print(f"{result}")
        return result

def collatz_sequence():
    getal = int(input("geef een geheel getal"))
    result = getal
    while result != 1:
        result = collatz(result)
        
collatz_sequence()
