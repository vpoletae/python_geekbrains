#1
with open('input_text.txt', 'a', encoding='UTF8') as f:
    exit_ = False
    while not exit_ == 'y':
        data = input('Please enter some text: ')
        f.write(data + '\n')
        exit_ = str(input('Would you like to exit? [y/n]:')).lower()
    f.write('\n')

#2
file_name = 'test_file.txt'
with open(file_name, 'r', encoding='UTF8') as f:
    lines = f.readlines()
    lines_total = len(lines)
    words_in_line = dict()
    counter = 1
    for line in lines:
        words = len(line.split(' ')) #ignoring test of what's word
        words_in_line[counter] = words
        counter += 1
    print(f'Lines total: {lines_total}')
    for line, count in words_in_line.items():
        print(f'{line} line: {count} words')

#3
file_name = 'salaries.txt'
threshold = 20000

def create_lists(file_name, threshold):
    below_20 = []
    all_salaries = []
    with open(file_name, 'r', encoding='UTF8') as f:
        for row in f:
            line = row.split('-')
            salary = int(line[1])
            if salary < threshold:
                below_20.append(line[0])
            all_salaries.append(salary)
    return below_20, all_salaries

below_20, all_salaries = create_lists(file_name, threshold)
avg_salary = sum(all_salaries)/len(all_salaries)

print('Below 20K salaries:')
for emp in below_20:
    print(emp)

print('-'*50)

print(f'Average salary is {avg_salary}')

#4
map_ = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре',}
file_name_input = 'ex4.txt'
file_name_output = 'ex4_translated.txt'

with open(file_name_input, 'r', encoding='UTF8') as f1:
    with open(file_name_output, 'a', encoding='UTF8') as f2:
        for row in f1:
            line = row.split(' — ') # can be added as a param in func
            word, num = line
            word_tr = map_[word]
            f2.write(f'{word_tr} - {num}')

#5
import random
random.seed(42)

min_num = 1
max_num = 100
nums_amount = 100

# create a list of random numbers
nums = [str(random.randint(min_num, max_num)) for _ in range(nums_amount)]

# write numbers to a file
with open('nums.txt', 'w', encoding='UTF8') as f:
    f.write(' '.join(nums))

# read nums and calc sum
with open('nums.txt', 'r', encoding='UTF8') as f:
    num_row = f.read()
    nums = num_row.split(' ')
    nums_sum = int()
    for num in nums:
        nums_sum += int(num)
    print(f'Total sum is: {nums_sum}')

#6
import re
from pprint import pprint

pattern = re.compile(r'\d+')
subj_dict = dict()

with open('subjects.txt', 'r', encoding='UTF8') as f:
    for row in f:
        line = row.split(':')
        subj, lessons = line
        hours = re.findall(pattern, lessons)
        hours_total = int()
        for h in hours:
            hours_total += int(h)
        subj_dict[subj] = hours_total
    pprint(subj_dict)

#7
import json

firm_profit_dict = dict()
profits = []
avg_profit_dict = dict()

with open('firms_data.txt', 'r', encoding='UTF8') as f:
    for row in f:
        line = row.split(' ')
        firm, type_, rev, exp = line
        profit = int(rev) - int(exp)
        firm_profit_dict[firm] = str(profit)
        profits.append(profit)
    avg_profit = sum(profits)/len(profits)
    avg_profit_dict['average_profit'] = str(avg_profit)

with open('financials_dump.json', 'w') as f:
    json.dump([firm_profit_dict, avg_profit_dict], f)
