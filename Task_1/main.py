while True:
    n = input("Enter an integer:")
    try:
        n = int(n)
        break

    except ValueError:
        print("Please enter an integer (no letters or decimals)")
if n % 2 != 0:
    print(f"The number {n} is an odd number")
else:
    print(f"The number {n} is an even number")