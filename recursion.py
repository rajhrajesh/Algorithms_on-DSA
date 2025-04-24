
def greet2(name):
    print("hi", name)

def bye():
    print("ok bye!")

def greet(name):
    print("my name is", name)
    greet2(name)
    bye()
greet("rajesh")


def factorial(n):
    if n == 1:
        return 1 
    else:
        return n * factorial(n - 1)
print(factorial(5))
