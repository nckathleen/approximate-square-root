def get_valid_input():
    num = input("Please enter a positive number: ")
    try:
        float(num)
    except:
        print("{} is not a number at all.".format(num))
        return get_valid_input()
    if float(num) < 0:
        print("{} is not a positive number.".format(num))
        return get_valid_input()
    else:
        num = float(num)
        return num


def fun_with_newton():
    epsilon = 0.01
    x = num / 2
    new_x = 0
    count = 1
    while abs(x * x - num) > epsilon:
        new_x = (x + (num / x)) * 0.5
        x = new_x
        print("After {} iteration(s), the guess is {}".format(count, x))
        count += 1
    print("The square root of {} is {}.".format(num, x))


num = get_valid_input()
fun_with_newton()
