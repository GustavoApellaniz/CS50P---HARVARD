def main():
    #input do usuário 
    x = str(input('qual a resposta do universo ').strip())
    deep(x)


def deep(x):
    #True se o input for uma variação de 42
    if x == ('42' or 'forty-two' or 'Forty Two'):
        print('yes')
    else:
        print('no')



main()