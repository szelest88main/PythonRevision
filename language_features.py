# a method doing something (printing text), 
# not returning anything ("procedure")
def simply_print_some_text():
    print("To be or not to be")

# a function taking a numeric parameter and returing its squared value
def get_value_squared(x):
    return x*x

# a function taking a function as parameter and printing
# its first 10 non-negative values
def show_first_10_values(some_function):
    for a in range(0,10): #from 0 to 9
        print(some_function(a),end=', ')

def main():
    # call the first function:
    simply_print_some_text()

    # print the value returned by the squaring function with param "3":
    print(get_value_squared(3))

    # call the values-printing method with squaring function as param
    show_first_10_values(get_value_squared)
    print() # print a new line character

    # call the third function with a lambda (also returning squared value)
    show_first_10_values(lambda x: x*x)
    print()


if __name__ == "__main__":
    main()
