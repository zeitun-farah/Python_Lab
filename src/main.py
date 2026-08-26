from utils import square, is_even, celsius_to_fahrenheit, greet

def main():
    # Ask for a name first
    name_input = input("Enter your name: ")
    print(greet(name_input))
    
    # Keep original math operations intact
    user_input = input("Enter a number: ")
    num = float(user_input)
    
    sq_val = square(num)
    even_status = "even" if is_even(num) else "odd"
    fah_val = celsius_to_fahrenheit(num)
    
    print(f"Square: {sq_val}")
    print(f"The number is {even_status}.")
    print(f"As Celsius, Fahrenheit equivalent: {fah_val}")

if __name__ == "__main__":
    main()
