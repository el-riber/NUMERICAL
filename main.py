def convert_to_decimal(number_str, base_from):
    return int(number_str, base_from)

def convert_from_decimal(decimal_number, base_to):
    if decimal_number == 0:
        return "0"
    digits = "0123456789ABCDEF"
    result = ""
    while decimal_number > 0:
        result = digits[decimal_number % base_to] + result
        decimal_number //= base_to
    return result

def main():
    print(" Multi-Base Converter (Supports Base 2 to 16)")
    
    number_str = input("Enter the number: ").strip().upper()
    base_from = int(input("Enter the base of the input number (2-16): "))
    base_to = int(input("Enter the base to convert to (2-16): "))
    
    if not (2 <= base_from <= 16 and 2 <= base_to <= 16):
        print(" Error: Bases must be between 2 and 16.")
        return

    try:
        decimal_value = convert_to_decimal(number_str, base_from)
        converted = convert_from_decimal(decimal_value, base_to)
        print(f" {number_str} (base {base_from}) = {converted} (base {base_to})")
    except ValueError:
        print(" Error: Invalid number for the specified base.")

if __name__ == "__main__":
    main()
