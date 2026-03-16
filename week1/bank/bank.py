def main():
    #input do usuário
    x = str(input('greeting ')).strip()
    hello(x)


def hello(x):
    #condicional sobre o greeting do usuário
    if x == "hello" :
        print(0)
    elif 'h' in x[0]:
        print(20)
    else:
        print(100)
    


main()