def main():
    #chama as duas funções e calcula a gorjeta final em float
    dollars = dollars_to_float(input("How much was the meal?"))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #realoca o $ para nada e dps transforma em float
    x = d.replace('$', '')
    f = float(x)
    return f

def percent_to_float(p):
    #realoca o % para nada e transforma em float 
    x = p.replace('%', '')
    x = float(x)
    per = x/100
    return per


main()