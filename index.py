# between 2 and 100 we pass a condition if the number is divisible by 3
# it is fizz if the number is divisible by 5 it is Buzz but if the number
# is divisible by both then it is FizzBuzz
limit = 100
for i in range(2, limit + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
