# Control Flow & Functions
temperature = 15

if temperature > 25:
    print("It's hot")
elif temperature > 10:
    print("It's mild")
else:
    print("It's cold")

# exmaple 
stock = 0

if stock > 10:
    print("In stock")
elif stock > 0:
    print("Low stock")
else:
    print("Out of stock")

# for & while loops
tasks = ["design", "build", "ship"]

for task in tasks:
    print("Working on:", task)

retries = 0
while retries < 3:
    print("Attempt", retries + 1)
    retries = retries + 1

# example 
# Write a for loop that prints each letter in "product"
for letter in "product":
    print(letter)

# Write a while loop that counts down from 5 to 1
count = 5

while count >= 1:
    print(count)
    count = count - 1

# Defining a Function
def apply_discount(price, percent_off):
    savings = price * (percent_off / 100)
    return price - savings

final_price = apply_discount(80, 25)
print(final_price) 

# example 
def greet(name):
    return "Hi, " + name + "!"

print(greet("Sam"))

# without a function — the same math, three separate places to break
a_total = 50 - (50 * (10 / 100))
b_total = 80 - (80 * (10 / 100))
c_total = 20 - (20 * (10 / 100))

# with a function — one place to fix, three places to call it
a_total = apply_discount(50, 10)
b_total = apply_discount(80, 10)
c_total = apply_discount(20, 10)

# main exmaple 
def shipping_cost(weight_kg, is_member):
    if is_member:
        return 0
    elif weight_kg <= 2:
        return 5
    else:
        return 5 + (weight_kg - 2) * 2

orders = [1, 3, 6]
is_member = False

total_shipping = 0
for order_weight in orders:
    cost = shipping_cost(order_weight, is_member)
    total_shipping = total_shipping + cost
    print("Order weight", order_weight, "costs", cost)

print("Total shipping:", total_shipping)