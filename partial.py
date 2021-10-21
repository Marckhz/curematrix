import sys
import re
import csv
# Math Questions

def divisibles_by_five_but_seven(x: int, y: int):
    return [n for n in range(x, y) if n % 5 == 0 and n % 7 != 0]
# print(divisibles_by_five_but_seven(1, 1000))


def transform_to_base_b(x: int, y: int):
    base = ""
    while x > 0:
        dig = int(x % y)
        if dig < 10:
            base += str(dig)
        x //= y
    return base[::-1]

# print(transform_to_base_b(5,3)) 

def generator_perfect_squares(N: int):
    return (n ** 2 for n in range(1, N))

def generator_perfect_squares_w_yield(N: int):
    for n in range(1,N):
        yield n ** 2


def check_phrase_exists(sentence: str, f):
    with open(f, 'r') as __file:
        text = __file.read()
        m = re.search(sentence, text)
        return True if m else False
# print(check_phrase_exists("death", sys.argv[1]))

def sum_columns(colum_number: int, __file):
    matrix = []
    res = 0
    with open(__file, 'r') as f:
        reader = csv.reader(f)
        for line in reader:
            matrix.append(line)
    
    for x in matrix:
        for y in range(len(x)):
            if y == colum_number:
                res += int(x[y])
    return res

print(sum_columns(2, sys.argv[1]))