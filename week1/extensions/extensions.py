def main():
    #input do usua. e separação do palavra pelo .
    x = str(input('arquivo ')).strip()
    y =(x.split('.'))  
    arq(y)


def arq(x):
    #output pelo formato do arquivo
    match x[1]:
        case 'gif':
            print('image/gif')
        case 'jpg':
            print('image/jpeg')
        case'jpeg':
            print('image/jpeg')
        case'png':
            print('image/png')
        case'pdf':
            print('application/pdf')
        case'txt':
            print('text/plain')
        case 'zip':
            print('application/zip')
        case _:
            print('formato inválido')

main()