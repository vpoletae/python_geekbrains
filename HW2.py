#1
type_list = [1, 'a', (1,2,3), {1,2,3}, [1,2,3], {'a':1, 'b':2}]
for elem in type_list:
    print(type(elem))

#2
def ask_elem_num():
    check = 0
    while not check:
        try:
            elem_num = int(input('Please enter a number: '))
            check = 1
        except ValueError:
            pass
    return elem_num

def create_list(elem_num):
    user_list = []
    for _ in range(elem_num):
        elem = input('Please enter element of list: ')
        user_list.append(elem)
    return user_list

def swap(user_list):

    last_elem = None
    if len(user_list) % 2 != 0:
        last_elem = user_list.pop(-1)

    odd = []
    even = []
    counter = 1
    for elem in user_list:
        if counter % 2 == 0:
            even.append(elem)
        else:
            odd.append(elem)
        counter += 1

    swapped_list = []
    for index in range(len(odd)):
        swapped_list.append(even[index])
        swapped_list.append(odd[index])

    if last_elem:
        swapped_list.append(last_elem)

    return swapped_list

elem_num = ask_elem_num()
user_list = create_list(elem_num)
swapped_list = swap(user_list)
print(swapped_list)

#3
def ask_month():
    check = 0
    while not check:
        try:
            month_num = int(input('Please enter month number number: '))
            if 1 <= month_num <= 12:
                check = 1
            else:
                print('Month number must be between 1 and 12')
        except ValueError:
            print('Please enter a number')
    return month_num

def check_month_with_list(month_num):
    winter = [1,2,12]
    spring = [3,4,5]
    summer = [6,7,8]
    fall = [9,10,11]
    season = str()
    if month_num in winter:
        season = 'Winter'
    elif month_num in spring:
        season = 'Spring'
    elif month_num in summer:
        season = 'Summer'
    else:
        season = 'Fall'
    return season

month_num = ask_month()
season = check_month_with_list(month_num)
print(f'Season is {season}')

#4
def split_word():
    word_line = input('Please enter a text separated with a space: ')
    words_list = word_line.split(' ')
    for i, word in enumerate(words_list):
        print(f'{i+1}. {word}')

split_word()

#5
def create_random_list(n_elems, min_, max_):
    import random
    random_list = []
    for _ in range(n_elems):
        random_list.append(random.randint(min_, max_))
    random_list = sorted(random_list, reverse=True)
    return random_list

def ask_new_rating():
    check = 0
    while not check:
        try:
            new_rating = int(input('Please enter new rating: '))
            check = 1
        except ValueError:
            print('Please enter a number')
    return new_rating

def insert_new_rating(random_list, new_rating):
    if not random_list:
        return [new_rating]

    new_list = random_list.copy()
    new_list.insert(0, new_rating)
    new_list_len = len(new_list)
    if new_list_len == 1:
        return new_list
    else:
        index = 0
        offset = 1
        while not new_list[index] > new_list[offset] and offset < new_list_len-1:
            new_rating = new_list[index]
            new_list[index] = new_list[offset]
            new_list[offset] = new_rating
            index += 1
            offset += 1
        return new_list

random_list = create_random_list(10, 1, 10)
new_rating = ask_new_rating()
new_list = insert_new_rating(random_list, new_rating)
print(random_list)
print(new_list)

#6
def ask_metric(metric):
    check = 0
    while not check:
        try:
            measure = float(input(f'Please enter {metric}: '))
            check = 1
        except ValueError:
            print('Please enter a number')
    return measure

def ask_for_sku():
    sku_dict = dict()
    name = input('Please enter SKU name: ')
    price = ask_metric('SKU price')
    amount = ask_metric('SKU amount')
    measure = input('Please enter SKU measure: ')
    sku_dict['Name'] = name
    sku_dict['Price'] = price
    sku_dict['Amount'] = amount
    sku_dict['Measure'] = measure
    return sku_dict

def create_sku_list():
    exit_ = 'n'
    sku_list = []
    counter = 1
    while not exit_ == 'y':
        sku_dict = ask_for_sku()
        sku_list.append((counter, sku_dict))
        exit_ = str(input('Would you like to exit? (y/n)')).lower()
    return sku_list

def get_analytics(sku_list):
    from collections import defaultdict
    analytics = defaultdict(list)
    for _, sku in sku_list:
        analytics['Name'].append(sku['Name'])
        analytics['Price'].append(sku['Price'])
        analytics['Amount'].append(sku['Amount'])
        analytics['Measure'].append(sku['Measure'])
    return analytics

sku_list = create_sku_list()
analytics = get_analytics(sku_list)
print(sku_list)
print(analytics)
