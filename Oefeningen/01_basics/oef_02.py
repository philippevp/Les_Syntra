def collatz (number):
    if int(number) % 2 == 0:
        result = number // 2
        print(f"{result}" )
        return result
    else:
        result = 3 * number + 1
        print(f"{result}")
        return result

collatz(17)