name = input("What is your name?: ").strip()

if name:
    biggest_letter = max(name)
    print(f"The biggest letter in '{name}' is: {biggest_letter}")
