# HAPPY NUMBER PROGRAM IN PYTHON
# User Input
user_no = int(input("Enter a no: "))


# function which evaluates the sum of the square of the digits passed as argument
def happy_no(num):
    global result
    sum1 = 0
    while num != 0:
        num1 = num % 10
        sum1 += num1**2
        num = num // 10
    result = sum1


# duplicate copy of user_no created which will change as sum of squares of digits change
result = user_no
# non_happy_no_numbers = 4, 16, 37, 58, 89, 145, 42, 20, 4 ... which is repetitive
# if our result is = to [ANY] non_happy_no_numbers then the original no. i.e user_no is not a happy no
# if result becomes 1 than our user_no is a happy no
while result != 1 and result != 89:
    happy_no(result)
if result == 1:
    print("{} is a happy no".format(user_no))
elif result == 89:
    print("{} is not a happy no".format(user_no))