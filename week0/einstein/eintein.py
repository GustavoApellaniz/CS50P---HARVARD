def main():
    #input do usuário e entrega a resposta
    x = int(input('m: '))
    answer = ein(x)
    print(answer)


def ein(x):
    #usa a fórmula de einstein com o input do usuário
    e = x*(300000000**2)
    return e 


main()
