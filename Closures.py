# def transmit_to_space(message):
#     "This is the enclosing function"
#     def data_transmitter():
#         "The nested function"
#         print(message)
#     data_transmitter()

# print(transmit_to_space("Test message"))

# def print_msg(number):
#     a=50
#     def printer():
#         "Here we are using the nonlocal keyword"
#         nonlocal number
#         number=3
#         a=2
#         print(number)
#         print(a)
#     printer()
#     print(a)

# print_msg(9)

def multiplier_of(num):
    def fn(): print(123)
    return  fn
        
multiplywith5 = multiplier_of(5)
multiplywith5(9)