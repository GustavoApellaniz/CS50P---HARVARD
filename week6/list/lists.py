import sys

def main():
    x = 0
    if len(sys.argv)>2:
        print('Too many command-line arguments')
        sys.exit()
    
    if 'py' not in sys.argv[1]:
        print('not a python file')
        sys.exit()
    

    try:
        with open(sys.argv[1]) as file:
            content = file.readlines()
            for line in content:
                if line.startswith('#'):
                    continue
                if line == '\n':
                    continue
                x += 1
            print(x)
    except FileNotFoundError:
        print('File does not exist')
            


main()