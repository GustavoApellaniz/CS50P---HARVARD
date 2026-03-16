def main():
    plate = input("Plate: ").strip().lower()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if len(s) == 2 and s.isalpha():
        return True
    
    if not (2<=len(s)<=6):
        return False
    
    if not (s[:2].isalpha()):  
        return False
    
    if (s[-1].isalpha()):
        return False
    
    number = True
    for c in s:
        if c.isdigit():
            if number:
                if c == '0':
                    return False
                number = False
    return True
               
                    
if __name__ == '__main__':
    main()