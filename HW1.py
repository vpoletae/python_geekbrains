#1
a = 'string'
b = 1
c = 1.12

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

print(f'Your name is {name}')
print(f'Your age is {age}')


#2
def convert_seconds():
    seconds = int(input('Please enter time in seconds: '))
    minutes = seconds // 60
    seconds = seconds % 60
    hours = minutes // 60
    minutes = minutes % 60
    if len(str(seconds)) < 2:
        seconds = '0' + str(seconds)
    if len(str(minutes)) < 2:
        minutes = '0' + str(minutes)
    if len(str(hours)) < 2:
        hours = '0' + str(hours)   
    print(f'Time is {hours}:{minutes}:{seconds}')

convert_seconds()

#3
def ask_num():
    check = 0
    while not check:
        try:
            rand_num = int(input('Please enter a number: '))
            check = 1
        except ValueError:
            pass
    return rand_num

def convert_num(rand_num):
    unit = str(rand_num)
    double = unit * 2
    triple = unit * 3
    sum_ = int(unit) + int(double) + int(triple)
    return sum_

rand_num = ask_num()
sum_ = convert_num(rand_num)
print(sum_)


#4
def find_max(rand_num):
    rand_num = str(rand_num)
    max_num = int()
    for digit in rand_num:
        digit = int(digit)
        if digit > max_num:
            max_num = digit
    return max_num

rand_num = ask_num()
max_ = find_max(rand_num)
print(max_)

#5
def ask_metric(metric):
    check = 0
    while not check:
        try:
            rand_num = float(input(f'Please enter {metric}: '))
            check = 1
        except ValueError:
            pass
    return rand_num

def calculate_metrics():
    revenue = ask_metric('Revenue')
    costs = ask_metric('Costs')
    profit = revenue - costs
    if profit <= 0:
        print(f'Your loss is {profit}')
    else:
        employees = ask_metric('Employees')
        return_on_employee = round(profit / employees, 2)
        print(f'Your profit is {profit}')
        print(f'Your return on employee is {return_on_employee}')

calculate_metrics()

#6
def count_day():
    daily_exercise = ask_metric('Daily exercises')
    target = ask_metric('Target')

    cumulative = daily_exercise
    day = 1
    while not cumulative > target:
        cumulative *= 1.1
        day += 1

    return day

day = count_day()
print(day)
