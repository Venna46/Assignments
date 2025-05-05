# from functools import lru_cache
#
#
# def fibonacci(n):
#
#     if n == 1:
#         return 1
#     elif n ==2:
#         return 1
#     elif n > 2:
#         return fibonacci(n-1)+ fibonacci(n-2)
#     return None
#
#
# for i in range(1,5):
#     print(i,":", fibonacci(i))
#
#
# #dictionary holds {key, value}
# cache = {} #dictionary
# cache1 = () #tuple
# cache2 = [] #list
#
# value = 0
#
# def fib2(n):
#     if n in cache:
#         return cache[n]
#
#     if n ==1:
#         value = 1
#     elif n ==2:
#         value = 1
#     elif n>2:
#         value = fib2(n-1) + fib2(n-2)
#
#         cache[n] = value
#     return value
#
# for i in range (1, 10):
#     print(f"{i} Term: {fib2(i)}")
#
# # L -> LAST, R-RECENTLY, C-CACHE
# @lru_cache(maxsize=1000)
# def fib3(n):
#
#     if n ==1 or n ==2:
#         return 1
#     elif n>2:
#         return fib3(n-1) + fib3(n-2)
#     return None
#
#
# for i in range(1, 20):
#     print(i, ":", fib3(i))


def TowerOfManoi(n, source, destination_rod, auxiliary_rod):

    if n ==1:
        print("Move disk 1 from source", source, "to destination", destination_rod)
        return
    TowerOfManoi(n-1, source, auxiliary_rod, destination_rod)
    print("Move disk ", n, "from source",source, "to destination", destination_rod)
    TowerOfManoi(n-1, auxiliary_rod, destination_rod, source)

n = 5
TowerOfManoi(n, 'A', 'B', 'C')


