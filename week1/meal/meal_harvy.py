def main():
    x = input('what time is it? ')
    y =convert(x)
    
    if 7<=y<=8:
        print('breakfast')
    elif 12<=y<=13:
        print('lunch')
    elif 18<=y<=19:
        print('dinner')

def convert(time):
    hour, minute  = time.split(':')
    hour = float(hour)
    minute = float(minute)
    con = (minute/60) + hour
    return con


if __name__ == "__main__":
    main()