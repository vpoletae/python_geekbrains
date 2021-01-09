#1
def ask_num():
    check = 0
    while not check:
        try:
            rand_num = int(input('Please enter a number: '))
            check = 1
        except ValueError:
            print('A number must be enetered!')
    return rand_num

def divide(a, b):
    try:
        res = a / b
        return res
    except ZeroDivisionError:
        print('Can not divide on zero!')
        return 'Error'

a = ask_num()
b = ask_num()
div = divide(a, b)
print(div)

#2
def user_info(name:str, surname:str, birth:str, city:str, email:str, phone:str):
    print(f'User info: {name}, {surname}, {birth}, {city}, {email}, {phone}')

user_info(
    name='Vadim',
    surname='Poletaev',
    birth='01.01.1901',
    city='Moscow',
    email='pewpew@mail.ru',
    phone='+7 495 111 11 11',
)

#3
def sum_of_two_max(a, b, c):
    num_list = sorted([a, b, c], reverse=True)
    return num_list[0] + num_list[1]

sum_ = sum_of_two_max(1, 2, 3)
print(sum_)

#4
def power_neg(x, y):
    power = 1
    for _ in range(abs(y)):
        power *= x
    return 1/power

power = power_neg(10, -3)
print(power)

#5
def get_nums():
    nums = input('Please enter a list of numbers separated by space: ')
    return nums

def sum_nums(nums:str):
    try:
        sum_ = int()
        nums_list = nums.split(' ')
        for num in nums_list:
            sum_ += int(num)
        return sum_
    except:
        print('Numbers separated by space must be entered!')

def calc_iter():
    exit_ = 'n'
    sum_ = int()
    while not exit_ == 'y':
        nums = get_nums()
        input_sum = sum_nums(nums)
        sum_ += input_sum
        print(f'Current sum is {sum_}')
        exit_ = str(input('For exit please enter "y"')).lower()

calc_iter()

#6
def capitalize_(x:str):
    x = str(x)
    return x.capitalize()

def capitalize_text(x:str):
    words_list = x.split(' ')
    capitalized_list = []
    for word in words_list:
        capitalized_list.append(capitalize_(word))
    return ' '.join(capitalized_list)


text = input('Please enter words separated by space: ')
cap_text = capitalize_text(text)
print(cap_text)

