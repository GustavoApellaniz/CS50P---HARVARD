def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    x_str, y_str = fraction.split("/")

    x = int(x_str)
    y = int(y_str)

    if y == 0:
        raise ZeroDivisionError

    if x > y:
        raise ValueError

    percentage = round((x / y) * 100)
    return percentage


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
