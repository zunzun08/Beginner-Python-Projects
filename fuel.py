
while True:
    user_input = (input("Fraction: "))

    # Split our Fraction
    try:
        x, y = user_input.split('/')

    # Convert x and y into fractions
        integer_x = int(x)
        integer_y = int(y)

    # Create a fraction for x and y
        fraction = integer_x / integer_y
        if fraction <= 1:
            break
    except(ValueError, ZeroDivisionError):
        pass
# Create a percentage

Percent = int(fraction * 100)

# Create the conditions

if Percent <= 1:
    print('E')
elif Percent >= 99:
    print('F')
else:
    print(f"{Percent}%")
