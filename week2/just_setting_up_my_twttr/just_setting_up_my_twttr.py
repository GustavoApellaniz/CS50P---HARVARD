def main():
    setting()


def setting():
    x = input('Input: ')
    for i in x:
        g = vogal(i)
        print(g,end='')

def vogal(x):
    y = x.lower()
    if (y == 'a') or (y =='e') or (y =='i') or (y=='o') or (y=='u'):
        f = y.replace(y, '')
        y = f
    return y


if __name__ == '__main__':
    main()