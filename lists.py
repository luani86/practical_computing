def oddNumbers(firstNumber, secondNumber):
    numbers = []
    for i in range(firstNumber, secondNumber):
        if i % 2 != 0:
            numbers.append(i)
    return numbers
# print oddNumbers(0, 10)

def symetric_list(number):
    list_1 = []
    list_2 = []
    for i in range(1, number+1):
        list_1.append(i)
    list_2 = list_1[::-1]
    list_3 = list_1 + list_2[1:]
    return list_3
# print symetric_list(10)

# def fibonacci(number):
#     fibonacci_numbers = [0, 1]
#     for i in range(2, number + 1):
#         fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
#     return fibonacci_numbers
# print fibonacci(6)

# def fibonacci(number):
#     list_1 = []
#     list_2 = []
#     for i in range(1, number + 1):
#         list_1.append(i)
#         if list_1[i] == list_1[i-1] + list_1[i-2]:
#             list_2.append(list_1[i])
#     return list_2
# print fibonacci(6)



# --------------------------- Basic fibonacci function: ---------------------------

def fibonacci_basic(n):
    if n == 1: 
        return 1
    if n == 2:
        return 1
    if n > 2:
        return fibonacci_basic(n - 1) + fibonacci_basic(n - 2)

# for n in range(1, 11):
#     print n, ' : ', fibonacci(n) 
# print fibonacci_basic(6)

# --------------------------- Memoization: ---------------------------
fibonacci_cache = {}
def fibonacci_memo(n):
    # Validation:
    if type(n) != int:
        raise TypeError('n must be a positiv int')
    if n < 1:
        raise TypeError('n must be a positiv int')
    # If we cashed the value, then return it:
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # Compute the Nth term
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci_memo(n-1) + fibonacci_memo(n-2) 

    # Cash the value and return it:
    fibonacci_cache[n] = value
    return value

# Print the fibonacci numbers:
# for n in range(1, 11):
#     print n, ' : ', fibonacci_memo(n)

# Print the ratio between the fibonacci numbers to see how quickly they increase:
for n in range(1, 51):
    print n, ' : ', float(fibonacci_memo(n+1)) / float(fibonacci_memo(n))

# The ratio of consecutive members of a fibonacci array converges to the golden ratio. 


# --------------------------- Memoization simplified: ---------------------------

# from functools import lru_cache (not working)
# def fibonacci_memo_simple(n):
#     if n == 1: 
#         return 1
#     if n == 2:
#         return 1
#     if n > 2:
#         return fibonacci_memo_simple(n - 1) + fibonacci_memo_simple(n - 2)

# for n in range(1, 11):
#     print n, ' : ', fibonacci_memo_simple(n) 
