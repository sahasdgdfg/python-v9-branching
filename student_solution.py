# В этом файле необходимо реализовать функции task1() ... task10()
# НИЧЕГО НЕ УДАЛЯТЬ
def task1():
    a = int(input())
    if a % 2 == 0:
        print("Even")
    else:
        print("Odd")


def task2():
    age = int(input())
    if age < 18:
        print("Minor")
    elif age <= 64:
        print("Adult")
    else:
        print("Senior")


def task3():
    st = float(input())
    act = input()
    nd = float(input())
    
    match act:
        case "+":
            print(st + nd)
        case "-":
            print(st - nd)
        case "*":
            print(st * nd)
        case "/":
            print(st / nd)


def task4():
    st = int(input())
    nd = int(input())
    rd = int(input())
    
    if st >= nd and st >= rd:
        print(st)
    elif nd >= st and nd >= rd:
        print(nd)
    else:
        print(rd)


def task5():
    year = int(input())
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap year")
    else:
        print("Not leap year")


def task6():
    t = int(input())
    if t < 0:
        print("Freezing")
    elif t <= 20:
        print("Cool")
    elif t <= 30:
        print("Warm")
    else:
        print("Hot")


def task7():
    score = int(input())
    if score >= 90:
        print("A")
    elif score >= 75:
        print("B")
    elif score >= 60:
        print("C")
    elif score >= 40:
        print("D")
    else:
        print("F")


def task8():
    day = int(input())
    match day:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")


def task9():
    a = float(input())
    b = float(input())
    c = float(input())
    
    if a + b > c and a + c > b and b + c > a:
        print("Triangle exists")
    else:
        print("Triangle does not exist")


def task10():

# По условию задачи "12345678" должен быть Medium, а тест хочет чтобы это было Strong
# Задача невыполнима поскольку условия задачи протевоерчат тестам

    pwd = input()
    
    if len(pwd) < 8:
        print("Weak")
    else:
        has_digit = False
        if ('0' in pwd) or ('1' in pwd) or ('2' in pwd) or ('3' in pwd) or ('4' in pwd) or ('5' in pwd) or ('6' in pwd) or ('7' in pwd) or ('8' in pwd) or ('9' in pwd):
            has_digit = True
        
        has_upper = False
        if pwd != pwd.lower():
            has_upper = True
        
        if has_digit and has_upper:
            print("Strong")
        elif has_digit:
            print("Medium")
        else:
            print("Weak")
