# try:
#     a = 1000;
#     b = int(input("Please enter a divisor to divide 1000 : "))
#     print(a/b)
# except ZeroDivisionError:
#     print('You enter 0 which is not permitted')
#
#

# try:
#     print('Hello')
#     print(10/0)
# except ZeroDivisionError:
#     print('Divided By Zero')
# finally:
#     print('This code will run no matter what!')

try:
    print(10/0)
except:
    raise
