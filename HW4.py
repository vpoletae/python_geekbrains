#1
def calculate_salary(time, hour_rate, bonus):
    return time * hour_rate + bonus

salary = calculate_salary(260, 1000, 10000)
print(salary)

#2
def pretty_list(num_list:list):
    num_list_len = len(num_list)
    if num_list_len <= 1:
        return num_list
    
    index = 0
    offset = index + 1
    new_list = []
    while offset <= num_list_len - 1:
        if num_list[offset] > num_list[index]:
            new_list.append(num_list[offset])
        index += 1
        offset += 1
    return new_list

num_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
num_list = [1, 2]
new_list = pretty_list(num_list)
print(new_list)

#3
list_div_20_21 = [num for num in range(20, 240) if num % 20 == 0 or num % 21 == 0]
print(list_div_20_21)

#4
nums_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

def clean_list(nums_list):
    from collections import Counter
    c = Counter(nums_list)
    unique_values = []
    for pair in c.items():
        if pair[1] == 1:
            unique_values.append(pair[0])
    return unique_values

clean_list = clean_list(nums_list)
print(clean_list)

#5
from functools import reduce

def mul(a, b):
    return a * b

even = [num for num in range(100, 1001) if num % 2 == 0]
res = reduce(mul, even)
print(res)

#6
from itertools import count, cycle

def iter_1(start):
    for i in count(start):
        print(i)
        if i == 10:
            break

iter_1(4)

def iter_2(seq, limit):
    for _ in range(limit):
        for i in cycle(seq):
            print(i)
            if i == seq[-1]:
                break

seq = [1, 2, 3]
iter_2(seq, 2)

#7
def fact(n):
    num = 1
    res = num
    while num <= n:
        yield res
        num += 1
        res *= num

for el in fact(4):
    print(el)