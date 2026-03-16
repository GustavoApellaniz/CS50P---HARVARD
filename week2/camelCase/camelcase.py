def main():
    x = str(input('camel case: '))
    snake(x)

def snake(x):
    y = x.split()
    for i in y:
        y = print(i.lower(), end='_')


if __name__ == '__main__':
    main()