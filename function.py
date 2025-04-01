


def func1():
    print("a")
    print("b")



def func2(lcal_element):
    print(lcal_element, lcal_element * 2)



for one_element in [1, 2, 3, "hello!"]:
    func2(one_element)


def fun3(name, surname):
    print(f'name is {str(name)}, surname is {str(surname)}')


fun3("Ivan", "petrov")

def sum2(a, b):
    result = a + b
    return(result)

print(sum2(2, 5))


def any_fun(a, b):
    result1 = a + b
    result2 = a * b
    return result1, result2

var1, var2 = any_fun(5, 4)
print(var1)
print(var2)