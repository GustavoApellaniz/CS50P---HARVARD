def main():
    cal =frutas(input('Item '))
    print(cal)


def frutas(prompt):
    tabela = { 'apple': 130, 'avocado': 50, 'banana': 110, 'cantaloupe': 50, 'lemon': 15, 'orange': 80}
    print(prompt)
    for k,v in tabela.items():
        if prompt in k:
            return v



if __name__ == '__main__':
    main()
    