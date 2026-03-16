import sys
from PIL import Image, ImageOps


def main():
    if len(sys.argv)>3:
        sys.exit('too many inputs')
    elif len(sys.argv)<3:
        sys.exit('too few arguments')
    elif not sys.argv[1].lower().endswith(('.png' ,'.jpeg','jpg')) and sys.argv[2].lower().endswith(('.png','.jpeg','jpg'))  :
        sys.exit('not supoorted type')
    else:
        try:
            shirt_replace(sys.argv[1],sys.argv[2])
        except FileNotFoundError:
            sys.exit('file not found')


def shirt_replace(x,y):
    with Image.open(x) as bf, Image.open(y) as sht:
        photo =ImageOps.fit(bf , sht.size)
        photo.paste(sht,sht)
        photo.save('output.png')
        







main()
