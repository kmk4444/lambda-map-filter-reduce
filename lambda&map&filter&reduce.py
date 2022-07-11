################################# lambda #################################
def summer(a,b):
    return a+b

summer(1, 3) * 9

# lambda could be used when the function is wanted.
# lambda is disposable function.
#providing that lambda is used with apply or map, it will really work.
new_sum = lambda a, b: a + b
new_sum(4,5)

################################ map #################################

# we do not need to writer loop by the means of map function.

salaries = [1000, 2000, 3000, 4000, 5000]

# salary will be incrased.
def new_salary(x):
    return x * 20/100 + x

new_salary(1000)

for salary in salaries:
    print(new_salary(salary))

list(map(new_salary, salaries))
#the first item is function
#the second item is list which could be looped.

# lambda & map
list(map(lambda x: x * 20 / 100 + x, salaries))

list(map(lambda x: x ** 2, salaries))

################################ filter #################################
# filter ensure to query
list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x: x % 2 == 0, list_store))
#the first item is query
#the second item is list which could be looped.


################################ reduce #################################
from functools import reduce

# iteratively processing related elements
list_store = [1, 2, 3, 4]
reduce(lambda a, b: a+b, list_store)
