def main():
    coke()

def coke():
    y = 50
    while y > 0:
        print('Amount Due:',y)
        x = int(input('insert coin: '))
        if (x == 5 or x == 10 or x == 25):
            y -= x
        else:
            print('só aceitamos 5 cents, 10 cents ou 25 cents')
    y = str(y)
    print('change owed', y.replace('-',''))




if __name__ == '__main__':
    main()