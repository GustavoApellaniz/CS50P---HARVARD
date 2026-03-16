def main():
    #acredito que deixei mais complicado de que realmente deveria
        shop()



def shop():
    z = []
    a = 1
    while True:
        x = input('')
        try:
            y ={x:a}
            for i in z:
                if x in i:
                    y.update(a = +1)
            z.append(y)
            print(z)
            

        except EOFError:
            pass


if __name__ == '__main__':
    main()