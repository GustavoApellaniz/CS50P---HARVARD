def main():
    shorten(input('Input: '))


def shorten(word):
    answer =''
    for i in word.lower():
        if i not in 'aeiou':
            answer +=i
    return answer
    


if __name__ == "__main__":
    main()
