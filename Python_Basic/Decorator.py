
# Decorator...................................................

# def my_decorator(func):
#     def decorate():
#         print("--------------")
#         func()
#         print("--------------")
#     return decorate
#
# def print_raw():
#     print("Clear Text")

# decorated_function = my_decorator(print_raw)
# decorated_function()

def My_Decorator(fnc):
    def Decorator():
        print('<<<--------------Author :: Aushomapto----------------->>>')
        fnc()
        print('<<<--------------Author :: Aushomapto----------------->>>')
    return Decorator

def My_Print():
    print('Hy Bro! Whats Up?')


My_First_Create_Decorator = My_Decorator(My_Print)
My_First_Create_Decorator()
