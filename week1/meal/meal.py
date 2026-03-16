def main():
    x = input('time ').replace(':','')
    y = float(x)
    convert(y)


def convert(time):
    if 700<=time<=800:
        print('breakfast')
    elif 1200<=time<= 1300:
        print('lunch')
    elif 1800<=time<=1900:
        print('dinner') 

if __name__ == "__main__":
    main()