# from symbol import decorator
# @decorator
# def functions(arg):
#     return "value"
# def decorator(function):
#     def new_fn(arg,dcf):
#         function(arg)
#         function(arg)
#     return new_fn
# # @decorator
# def fn(arg):
#     print("value"+arg)
#     # return "value"+arg
# # function = decorator(function)

# fn = decorator(fn)
# print(fn("123",123))
def type_check(correct_type):
    #put code here
    def generator(old_fn):
        def check(arg):
            if correct_type != type(arg):
                print("Bad Type")
                return
        return old_fn
    return generator

@type_check(int)
def times2(num):
    return num*2

print(times2(2))
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])