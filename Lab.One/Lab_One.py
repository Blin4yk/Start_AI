int_variable = 1  # int
assert isinstance(int_variable, int)

float_variable = 1.2  # float
assert isinstance(float_variable, float)

string_variable = "1"  # string
assert isinstance(string_variable, str)

bool_variable = True # bool
assert isinstance(bool_variable, bool)
list_variable = [1, 2.3, "34", True, [1,2,3,4,5,6]]  # list
assert isinstance(list_variable, list)

tuple_variable = (1, 2, 3, 4, 5, 6)  # tuple
assert isinstance(tuple_variable, tuple)

set_variable = set(tuple_variable)  # set unique
assert isinstance(set_variable, set)

dict_variable = {"keys":"values", "a":10, "ahahaha":"heheheheheh"}  # dict
assert isinstance(dict_variable, dict)

def difference_of_two_numbers(first, second):
    """Возвращает разницу между первым и вторым аргументом"""
    return first - second


assert difference_of_two_numbers(2, 1) == 1
assert difference_of_two_numbers(4, 1) == 3
assert difference_of_two_numbers(10, 0) == 10
assert difference_of_two_numbers(-5, -6) == 1

def condition_function(input_number):
    """
    Если входное число меньше либо равно 0, то умножить его на 2.
    В противном случае, если число больше 0, но меньше или равно 10, умножить на 3.
    Во всех прочих случаях поделить на 10.
    """
    if input_number <= 0:
        return input_number * 2
    elif input_number <= 10:
        return input_number * 3
    else:
        return input_number / 10


assert condition_function(0) == 0
assert condition_function(-1) == -2
assert condition_function(1) == 3
assert condition_function(10) == 30
assert condition_function(11) == 1.1
assert condition_function(20) == 2

def calculator(number_1, operation, number_2):
    """
    Простой оператор, способный выполнять операции +, -, *, /.
    На входе первое число, операция в виде строки и второе число.
    """
    if operation == "+":
        return number_1 + number_2
    elif operation == "-":
        return number_1 - number_2
    elif operation == "*":
        return number_1 * number_2
    elif operation == "/":
        return number_1 / number_2
    else:
        raise ValueError("Неподдерживаемая операция")


assert calculator(1, "+", 2) == 3
assert calculator(3, "-", 1) == 2
assert calculator(4, "*", 3) == 12
assert calculator(2, "/", 2) == 1

def number_of_unique_elements(input_list):
    """
    Считает количество уникальных элементов в листе.
    """
    return len(set(input_list))


assert number_of_unique_elements([1, 2, 3]) == 3
assert number_of_unique_elements([1] * 93) == 1
assert number_of_unique_elements(list(range(1000))) == 1000

def counter(input_list):
    """
    Считает количество вхождений каждого из элементов листа.
    Возвращает словарь вида {число: количество вхождений}
    """
    count_dict = {}
    for item in input_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict


assert counter([1, 1, 1, 2, 3]) == {1: 3, 2: 1, 3: 1}
assert counter([1] * 1000) == {1: 1000}
assert counter([1, 3, 5] * 100) == {1: 100, 3: 100, 5: 100}

def multiply_nums(input_string):
    """
    Перемножить числа, переданные в строке, перечисленные через запятую.
    """
    numbers = map(int, input_string.split(", "))
    result = 1
    for num in numbers:
        result *= num
    return result


assert multiply_nums("2, 3") == 6
assert multiply_nums("1, 1, 1, 1, 1, 1, 1") == 1
assert multiply_nums("345, 4576, 794, 325, 0") == 0

import math

def custom_function(x):
    """
    Реализует функцию y = sin(x) * cos(x)
    """
    return math.sin(x) * math.cos(x)


assert round(custom_function(1), 3) == 0.455
assert round(custom_function(1.5), 3) == 0.071
assert round(custom_function(2), 3) == -0.378
assert custom_function(0) == 0















def time_converter(n):
    """
    Определяет время на электронных часах по количеству минут с начала суток.
    """
    hours = (n // 60) % 24
    minutes = n % 60
    return f"{hours} {minutes}"

assert time_converter(2782) == '22 22'
assert time_converter(4733) == '6 53'
assert time_converter(1766) == '5 26'
assert time_converter(3865) == '16 25'
assert time_converter(4628) == '5 8'
assert time_converter(4353) == '0 33'
assert time_converter(268) == '4 28'
assert time_converter(4373) == '0 53'
assert time_converter(2722) == '21 22'
assert time_converter(1531) == '1 31'


def min_of_three_values(a, b, c):
    """
    Находит минимум из трех чисел.
    """
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c

assert min_of_three_values(1, 2, 3) == 1
assert min_of_three_values(1, 1, 9) == 1
assert min_of_three_values(18, 7, 11) == 7
assert min_of_three_values(2, 10, 10) == 2
assert min_of_three_values(17, 14, 17) == 14
assert min_of_three_values(9, 2, 10) == 2
assert min_of_three_values(7, 4, 7) == 4
assert min_of_three_values(0, 8, 3) == 0
assert min_of_three_values(8, 10, 6) == 6
assert min_of_three_values(1, 4, 8) == 1


def remove_symbol(string, symbol):
    """
    Удаляет все вхождения символа из строки.
    """
    return string.replace(symbol, '')

assert remove_symbol('aaaaaaaa', 'a') == ''
assert remove_symbol('abababa', 'b') == 'aaaa'
assert remove_symbol('12341234', '3') == '124124'


def remove_each_third_sym(string):
    """
    Удаляет каждый третий символ в строке, считая индексы с 1.
    """
    return ''.join([char for idx, char in enumerate(string, start=1) if idx % 3 != 0])

assert remove_each_third_sym('abcdef') == 'abde'
assert remove_each_third_sym('sdfasdfasdfsfa') == 'sdasfadffa'
assert remove_each_third_sym('123456789') == '124578'
assert remove_each_third_sym('987654321') == '986532'


def find_max(input_list):
    """
    Находит максимальный элемент в листе и его индекс.
    """
    max_value = input_list[0]
    max_index = 0
    for index, value in enumerate(input_list):
        if value > max_value:
            max_value = value
            max_index = index
    return max_value, max_index

assert find_max([1, 2, 3, 4, 5]) == (5, 4)
assert find_max([5, 4, 3, 2, 1]) == (5, 0)
assert find_max([96, 82, 72, 48, 93, 88, 79]) == (96, 0)
assert find_max([49, 75, 65, 65, 65, 18]) == (75, 1)
assert find_max([69, 16, 64, 54, 36, 70, 89, 29]) == (89, 6)
assert find_max([17, 80, 27, 36, 21, 85, 63, 27]) == (85, 5)
assert find_max([76, 27, 73, 65, 52]) == (76, 0)
assert find_max([33, 26, 69, 40, 93]) == (93, 4)
assert find_max([87, 5, 95, 52, 21, 76, 22]) == (95, 2)
assert find_max([75, 18, 89, 99, 70]) == (99, 3)


def append_to_list(input_list, value):
    """
    Вставляет элемент в конец листа.
    """
    input_list.append(value)
    return input_list

assert append_to_list([1, 2], 3) == [1, 2, 3]
assert append_to_list([1, 2], None) == [1, 2, None]
assert append_to_list([1, 's'], True) == [1, 's', True]


def number_unique_elements(input_list):
    """
    Возвращает количество уникальных элементов в листе.
    """
    return len(set(input_list))

assert number_unique_elements([1, 2, 3]) == 3
assert number_unique_elements([1, 2, 1]) == 2
assert number_unique_elements([1, 1, 1, 1]) == 1
assert number_unique_elements([1, 2, 1, 2]) == 2



class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


veh1 = Vehicle(100, 50)
assert (veh1.max_speed, veh1.mileage) == (100, 50)

veh2 = Vehicle(200, 3)
assert (veh2.max_speed, veh2.mileage) == (200, 3)


class Truck(Vehicle):
    def __init__(self, max_speed, mileage):
        super().__init__(max_speed, mileage)


truck1 = Truck(50, 1000)
assert (truck1.max_speed, truck1.mileage) == (50, 1000)

truck2 = Truck(43, 235)
assert (truck2.max_speed, truck2.mileage) == (43, 235)


class MyList:
    def __init__(self, input_list):
        self.input_list = input_list
    
    def return_sum(self):
        """
        Возвращает сумму всех элементов сохраненного листа.
        Пользоваться sum нельзя!
        """
        total = 0
        for num in self.input_list:
            total += num
        return total
    
    def make_reverse(self):
        """
        Разворачивает сохраненный лист.
        """
        return self.input_list[::-1]
    
    def make_slice(self, start, stop):
        """
        Делает слайсинг сохраненного листа.
        """
        return self.input_list[start:stop]


a = MyList([1, 2, 3, 4])
assert a.return_sum() == 10
assert a.make_reverse() == [4, 3, 2, 1]
assert a.make_slice(0, 2) == [1, 2]

b = MyList([5, 6, 6, 5])
assert b.return_sum() == 22
assert b.make_reverse() == [5, 6, 6, 5]
assert b.make_slice(1, 2) == [6]
