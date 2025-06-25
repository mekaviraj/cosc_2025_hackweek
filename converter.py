
import argparse

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert temperatures between Celsius and Fahrenheit.")

    parser.add_argument("value", type=float, help="Temperature value to convert")
    parser.add_argument("--to", choices=["c", "f"], required=True,
                        help="Convert to 'c' (Celsius) or 'f' (Fahrenheit)")

    args = parser.parse_args()

    if args.to == "f":
        result = celsius_to_fahrenheit(args.value)
        print(f"{args.value}°C is {result:.2f}°F")
    else:
        result = fahrenheit_to_celsius(args.value)
        print(f"{args.value}°F is {result:.2f}°C")
