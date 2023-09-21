# def logger(name = "unknown"):
#     # print("log call ",name)
#     return 123


# print(logger("abc"))
# print(logger())

arr = [1, -1,4,7,-2]
maxm = 0
# minm = 0
# for i in arr:
#     if i >maxm:
#         maxm = i
#     if i < minm:
#         minm =i
# print("sum=",maxm+minm)

# maxminsum([1, -1,4,7,-2]) #=>  5
# maxminsum([4,17,-2])      #=>  15
# maxminsum([4,17,2])      #=>   19

def maxminsum(arr):
    maxm = 0
    minm = 0
    for i in arr:
        if i >maxm:
            maxm = i
        if i < minm:
            minm =i
    print("sum=",maxm+minm)

maxminsum([1, -1,4,7,-2]) #=>  5
maxminsum([4,17,-2])      #=>  15
maxminsum([4,17,2])      #=>   19