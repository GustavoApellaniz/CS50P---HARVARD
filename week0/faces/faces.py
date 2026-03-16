def main():
    #chama duas funções e retorna um emoj feliz/trsite
    emoji = input('feliz ou triste ')
    x = change_sad(emoji)
    y = change_happy(x)
    print(y)


def change_sad(x):
    #chama o emoj triste pelo cod
    f = x.replace(':(',"\U0001F97A")
    return f

def change_happy(x):
    #chama o emoj feliz pelo cod
    b = x.replace(':)','\U0001F600')
    return b 




main()
