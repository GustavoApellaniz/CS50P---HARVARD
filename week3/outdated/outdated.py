def main():
    while True:
        try:   
            x = input()
            if '/' in x:
                date(x)
            else:
                strdata(x)
        except EOFError:
            break

def date(x):
    try:
        z =x.split('/')
        z.reverse()
        y,m,d = z
        if int(d)<=31 and int(m)<=12:
            print(f'{y}-{m:}-{d:}')
    except ValueError:
        pass
        
def strdata(x):
    mes = [
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
]
    try:
        z= x.split(' ') 
        b =z[1].replace(',','')
        b =int(b)
        for i in range(len(mes)):
            if z[0] in mes[i]:
                print(f'{i+1:02}-{b:02}-{z[2]}')
    except IndexError:
        pass

if __name__ ==  '__main__':
    main()