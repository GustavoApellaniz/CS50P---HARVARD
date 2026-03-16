import re
import sys


def main():
    z =convert(input("Hours: "))
    print(z)


def convert(s):
    x = re.match(r'^(\d{1,2}(?:\:\d{1,2})?) ?(?:am)? to (\d{1,2}(?:\:\d{1,2})?) ?(?:pm)?$', s, flags= re.IGNORECASE)
    if x:
        if ':' in x.group(1):
            y = x.group(2)
            if ':' in y:
                h,m = y.split(':')
                if int(h)<12:
                    h = int(h)+12
                return(f'{str(x.group(1))} to {str(h)}:{str(m)}')
            else:
                g = int(x.group(2))+12
                return(f'{str(x.group(1))} to {str(g)}:00')
        else:
            y = x.group(2)
            if ':' in y:
                h,m = y.split(':')
                if int(h)<12:
                    h = int(h)+12
                return(f'{str(x.group(1))}:00 to {str(h)}:{str(m)}')
            else:
                g = int(x.group(2))+12
                return(f'{str(x.group(1))}:00 to {str(g)}:00')
if __name__ == "__main__":
    main()