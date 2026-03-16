def main():
    #chama um input e adiciona ... após cada termo individual
    x =input('slow down ')
    f =slow(x)
    v = '...'.join(f)
    print(v + '.')


def slow(x):
    #separa cada termo 
    low = x.split()
    return low



main()

