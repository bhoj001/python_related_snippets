import decorator

my_coffee = decorator.ConcreteCoffee()
print(
    'Ingredients :', my_coffee.get_ingridents(),
    ', Cost :', my_coffee.get_price(),
    ', Sales Tax :',my_coffee.get_taxes()
)

my_coffee = decorator.Milk(my_coffee)
print(
    'Ingredients :', my_coffee.get_ingridents(),
    ', Cost :', my_coffee.get_price(),
    ', Sales Tax :',my_coffee.get_taxes()
)
my_coffee = decorator.Vanilla(my_coffee)
print(
    'Ingredients :', my_coffee.get_ingridents(),
    ', Cost :', my_coffee.get_price(),
    ', Sales Tax :',my_coffee.get_taxes()
)
my_coffee = decorator.Suger(my_coffee)
print(
    'Ingredients :', my_coffee.get_ingridents(),
    ', Cost :', my_coffee.get_price(),
    ', Sales Tax :',my_coffee.get_taxes()
)