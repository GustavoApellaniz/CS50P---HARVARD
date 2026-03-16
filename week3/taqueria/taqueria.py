tacos ={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    taq(tacos)


def taq(x):
    t = 0
    while True:
        y = input('Item: ').title()
        try:
            for i in x.keys():
                if y == i:
                    t += x[i]
                    print(f'${t}')
        except ValueError:
            pass
 



if __name__ == '__main__':
    main()