import csv
import sys

def main():
    if len(sys.argv)<3:
        print('Too few command-line arguments')
        exit()

    if len(sys.argv)>3:
        print('Too many command-line arguments')
        exit()

    try:
        with open(sys.argv[1]) as bef, open(sys.argv[2], 'w', newline= '') as aft :
            reader = csv.DictReader(bef)
            writer =csv.DictWriter(aft, fieldnames= ['name','last','house'])
            writer.writeheader()
            for row in reader:
                name, last =row['name'].split(',')
                writer.writerow({'name':name,'last':last,'house':row['house']})
                print(name)
    except FileNotFoundError:
            print('Could not read invalid_file.csv')
            exit()

def exit():
    return sys.exit()   

if __name__ == '__main__':
    main()