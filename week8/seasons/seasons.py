from datetime import date
import re
import sys
from operator import __sub__
from inflect import engine

def main():
    nascimento = input('Data de nascimento: ')
    time_life(padrao_data(nascimento))


def padrao_data(nascimento):
    padrao = re.match(r'^\d{1,4}-\d{1,2}-\d{1,2}$',nascimento)
    if padrao:
        y,m,d = nascimento.split('-')
        x = date(int(y),int(m),int(d))
        return x
    else:
        print('wrong syntax')
        sys.exit()


def time_life(x):
    p = engine()
    data = date.today()
    calculo = __sub__(data, x)
    return(p.number_to_words(calculo.days* 24 * 60, andword=''))

if __name__ == "__main__":
    main()