user_inpt = input("Enter a positive number: ")
b = int(user_inpt)


def validate_input():
    if b <= 0:
        print("This is not a positive number")
    else:
        fun_with_newton()


def fun_with_newton():
    epsilon = 1
    x = b / 2
    new_x = 0
    count = 1
    while epsilon >= float(0.01):
        new_x = (x + (b / x)) / 2
        epsilon = (x - new_x)
        x = new_x
        print("After {} iteration(s), the guess is {}".format(count, x))
        count += 1
    print("The square root of {} is {}.".format(user_inpt, x))

validate_input()
