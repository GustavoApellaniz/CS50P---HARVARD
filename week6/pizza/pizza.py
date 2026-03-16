import tabulate
import sys
import csv

def main():
    if len(sys.argv)>2:
        print('Too many command-line arguments')
        sys.exit()
    if len(sys.argv)<2:
        print('Too few command-line arguments  ')
        sys.exit()
    if '.csv' not in sys.argv[1]:
        print('Not a CSV file')
        sys.exit()

    try:
        with open(sys.argv[1], 'r') as file:
            content = csv.DictReader(file)
            print(tabulate.tabulate(content, tablefmt= 'grid'))
    except FileNotFoundError:
        print('file not found')




if __name__ == '__main__':
    main()