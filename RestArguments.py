def bar(first, second, third, **options):
    print(options)
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first
# action = "sum"
# number = "first"
# # bar(1,2,3,action,number)
result = bar(1, 2, 3, action = "sum", number = "first")
# bar(1,2,3,4,5,6,7)
# def bar(a,b,c,*rest):
#     print(len(rest))
# bar(1,2,3,4,5,6)