def main():
    x =fuel()
    print(x)

def mod():
    while True:
        try:
            x = input('Fraction ')
            f = x.split('/')
            y,z = f
            y = int(y)
            z = int(z)
            if y>z:
                raise ValueError
            if y<0:
                 raise ValueError
            return y/z
        except ValueError:
            pass
        except ZeroDivisionError:
             pass
        
def fuel():
        x =mod()
        if 0.35 <x<= 0.50:
            return '50%'
        elif 0.10<x<0.35:
            return '25%'
        elif x<=0.10:
                return 'E'
        elif 0.50<x<0.90:
            return '75%'
        else:
            return 'F'
        
if __name__ == '__main__':
    main()