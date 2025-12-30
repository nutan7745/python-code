num = int(input("Enter a number: "))

if num >= 0:
    last_digit = num % 10
else:
    last_digit = (-num) % 10

print("Last digit is:", last_digit)
