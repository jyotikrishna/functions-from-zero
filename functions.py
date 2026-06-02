def simple():pass

def simple2():
    print("simple")

#Most useful functions

def my_worker(fruit):
    statement = f"My favourite meal is chicken and {fruit}"
    meals ={"dinner" : statement}
    return meals 

meal = my_worker("mango")
type(meal)
meal.keys()

def human(food):
    consume = food["dinner"]
    return consume
my_meal = human(meal)
print(my_meal)