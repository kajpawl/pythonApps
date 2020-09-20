# recursion example

def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)


print('5! = {:,},\n3! = {:,},\n11! = {:,}'.format(
    factorial(5),  # 120
    factorial(3),  # 6
    factorial(11)  # HUGE
))


# fibonacci numbers - generator method example

# traditional method
# def fibonacci(limit):
#     nums = []
#
#     current = 0
#     next = 1
#
#     while current < limit:
#         current, next = next, current + next
#         nums.append(current)
#
#     return nums
#
# for n in fibonacci(int(input('Fibonacci, limit: '))):
#     print(n, end=', ')

# generator method
def fibonacci_co(limit):
    current = 0
    next = 1

    while current < limit:
        current, next = next, current + next
        yield current

print('with yield')
for n in fibonacci_co(int(input('Fibonacci, limit: '))):
    if n > 1000:
        break

    print(n, end=', ')
