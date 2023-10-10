#Write a python to find the maximum of three numbers 
def maximum_value(a, b, c):
    if a>b and a>c:
        print(f"{a} is greaterthan {b} and {c}")
    elif b>c and b>a:
        print(f"{b} is greaterthan {c} and {a}")
    else:
        print(f"{c} is greater than {b} and {a}")
maximum_value(70, 80, 63)


#write a python function to sum all the numbers in a list
def sum_of_numbers(a, b, c, d, e):
    result=[a+b+c+d+c]
    print(result)
sum_of_numbers(8, 2, 3, 0, 7)

#Write a python function to multiply all numbers in a list [ 8, 2, 3, -1, 7]
def product_of_numbers(a, b, c, d, e,):
    result=[a*b*c*d*e]
    print(result)
product_of_numbers(8, 2, 3, -1, 7)

#Write a python function to reverse a string 
def my_string(str):
    str="1234abcd"
    reversed_string=(str)
    for i in reversed(str):
        print(i)
my_string("1234abcd")

#Write a python programme to print the even numbers in a given list[1, 2, 3, 4, 5, 6, 7, 8, 9]
def normal_list(a, b, c, d, e, f, g, j, k):
    even_list=[b, d, f, j]
    print(even_list)
normal_list(1, 2, 3, 4, 5, 6, 7, 8, 9)
