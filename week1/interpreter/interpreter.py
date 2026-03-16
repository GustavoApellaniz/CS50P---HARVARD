def main():
    x = str(input('expression ')).split()
    y =expression(x)
    print(y)

def expression(x):
    y = float(x[0])
    z = float(x[2])
    e = (x[1])

    match e:
        case '+':
            return y+z
        case '/':
            return y/z
        case '*':
            return y*z
        case '-':
            return  y-z
        case _:
            print('formato inválido')

main()