print("Binary to Decimal")
binary = input('enter a number: ')
decimal = 0
for digit in binary:
    decimal = decimal*2 + int(digit)
print (decimal)


print("Decimal to Binary")
def decimalToBinary(num):
    if num > 1:
        decimalToBinary(num // 2)
    print(num % 2, end='')
number = int(input("Enter any decimal number: "))
decimalToBinary(number)

