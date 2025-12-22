
def main():
    while True:
        inpt = int(input("\nВведите любое натуральное число: "))

        output = 0
        for i in range(1, inpt + 1):
            print(f"{output} + {i} = {output + i}")
            output += i

        print(f"\nсумма всех входящих чисел в {inpt} = {output}")

main()