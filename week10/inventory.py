# Reflection 1:
# The most surprising thing about Python lists is that they can be changed after
# they are created. I can add, remove, and sort items without creating a new list.

# Reflection 2:
# In a business class, I could use a Python list to store daily sales amounts.
# Python could calculate totals and averages automatically instead of doing them manually in Excel.


# Exercise 1
inventory = ["pen","notebook","stapler","tape","marker"]
print(inventory)
print(len(inventory))

# Exercise 2
print(inventory[0])
print(inventory[-1])
middle = len(inventory) // 2
print(inventory[middle])

# Exercise 3 
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# Exercise 4
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

# Exercise 5
coords = (40.7128, -74.0060)

try: 
    coords[0] = 99
except TypeError as error: 
    print(f"TypeError caught {error}")
    print("Tuples protect coordinates from being changed by accident")
print(coords)

# Exercise 6
# Exercise 6
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count

print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")
# Exercise 7 
prices = [9.99,14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    discounted.append(round(price * 0.90, 2))

print(prices)
print(discounted) 

# Exercise 8 
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print(high_sales)
print("Count:", len(high_sales))
print("Avg:", round(sum(high_sales) / len(high_sales), 2))

