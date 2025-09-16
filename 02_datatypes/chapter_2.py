#Integers

#Addition
black_tea_grams = 14
ginger_grams = 3
total_grams = black_tea_grams + ginger_grams
print(f"Total grams of base tea is: {total_grams}")

#Subtraction
remaining_tea = black_tea_grams - ginger_grams
print(f"Remaining grams of black tea is: {remaining_tea}")

# Division
milk_litres = 7
servings = 4
milk_per_servings = milk_litres / servings
print(f"Milk per serving is: {milk_per_servings}")


# we use two slashes if we want exact numbers not the decimals

total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"while tea bags per pot: {bags_per_pot}")


# modulus operator
total_cardamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cardamom_pods % pods_per_cup
print(f"Leftover cardamom pods: {leftover_pods}")

# Scaling (exponential power)

base_flavor_strength = 2
scale_factor = 3
powerful_flavour = base_flavor_strength ** scale_factor
print(f"Powerful flavour strength: {powerful_flavour}")


# python separates the large numbers with underscores for better readability
total_tea_leaves_harvested = 1_000_000_000

print(f"Total tea leaves harvested: {total_tea_leaves_harvested}")


#BOOLEANS 

is_boiling = True
stir_count = 5
total_actions = stir_count + is_boiling #upcasting (true will automatically get converted to one)

print(f"Total actions: {total_actions}")

milk_present = 0 #no milk
print(f"is there milk? {bool(milk_present)}")


#logical operators(and, or, not)

water_hot = True
tea_added = False

can_serve = water_hot and tea_added
print(f"Can serve chai? {can_serve}")

water_hot = True
tea_added = True

can_serve = water_hot and tea_added
print(f"Can serve chai? {can_serve}")


# Real numbers (floating point number)

ideal_temp = 95.5
current_temp = 95.499999999


print(f"Ideal temp {ideal_temp}")
print(f"current temp {current_temp}")
print(f"difference temp {ideal_temp - current_temp}")

# the answer is so precise so when we deal with higher numbers there are packages, we simply take that and work on it,python is a very favored language for scientific computings, mathematicians

import sys
print(sys.float_info)