# Variables & Assignment 
age = 34
city = "Toronto"
age = age + 1
print(age)

# example 2 
score = 10
score = score * 2
print(score)

# Core Data Types
name = "Ali"        
count = 12          
price = 9.99        
is_active = True 
print(name, count, price, is_active)

# example 
a = "5"
b = 5
print(a == b)

#Lists & Dictionaries
fruits = ["apple", "pear", "fig"]
print(fruits[0])          
user = {"name": "Ali", "role": "PM"}
print(user["role"])
print(user["name"])

city = ["okara", "lahore", "Multan"]
print(city[0])

role = {
    "tittle" : "Backend developer",
    "team" : "software devlepment"
}
print(role)
print(role["tittle"])
print(role["team"])

# Basic Operators
total = 3 + 4           
is_match = (3 == 3)      
can_ship = True and False  
can_view = True or False   

print(total, is_match, can_ship, can_view)
print(10 - 3 == 7 and 2 == 2)
# example 


customer = "Ali"
age = 22
is_student = True
items = ["book", "bag", "pen"]
prices = {"book": 10, "bag": 25, "pen": 3}
total = 0
total = total + prices["book"]
total = total + prices["bag"]
total = total + prices["pen"]
free_delivery = is_student and total > 30
print(customer)
print(items[1])
print(total)
print(free_delivery)
print(age >= 25)
print(is_student or age >= 60)