# If input = 0, return 0
# otherwise,
# Start with an input number, user_num b
# make a rough guess of the sqrt, root_guess x
# use that to revise the input number
# repeat

# formula = root_guess = 1/2 ( root_guess + user_num/root_guess)

user_inpt = input("Enter a positive number: ")
b = int(user_inpt)

def validate_input():
    if b <= 0:
        print("This is not a positive number")
    else:
        fun_with_newton()
#    try:
#        value = int(user_inpt)
#    except ValueError:
#        print("This is not valid input.")

#    if user_inpt == int(user_inpt):
#        fun_with_newton
#    else:
#        print("This is not valid input.")

def fun_with_newton():
    epsilon = 1
    x = b/2
    new_x = 0
    count = 1
    while epsilon > float(0.01):
        new_x = (x + (b/x))/2
        epsilon = (x - new_x)
        x = new_x
        print("After ",count, "iteration(s), the guess is", x)
        print
        count += 1
    print("The square root of ", user_inpt, "is", x, ".")

validate_input()
