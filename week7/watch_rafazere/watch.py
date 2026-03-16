import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search((r'<iframe src="http://www.youtube.com/(^")"></iframe>'),s)
    if match:
        print(match.group(1))


if __name__ == "__main__":
    main()