sum = 0

for i in range(1, 51):
    sum += i

print(f"The total of all the integers between 1 and 50 is: {sum}")

"""
#BONUS
while True:
    user_input = input("Enter a positive whole number: ")

    if user_input.isdigit():
        n = int(user_input)
        if n > 0:
            break
        else:
            print("Please enter a number greater than 0.")
    else:
        print("Invalid input. Please enter a whole number (no decimals or letters).")

total_sum = n * (n + 1) // 2
print(f"The sum of numbers from 1 to {n} is: {total_sum}")
"""