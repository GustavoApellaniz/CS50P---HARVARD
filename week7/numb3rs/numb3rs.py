import re

def main():
    print(validate(input("IPv4 Address: ").strip()))

def validate(ip):
    x = ip.split('.')
    padrao = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'
    if _:= re.search(padrao,ip):
        for i in x:
            if int(i)>255:
                return 'invalid'
            else:
                print(i)
                return 'valid'
    else:
        return 'invalid'

if __name__ == "__main__":
    main()