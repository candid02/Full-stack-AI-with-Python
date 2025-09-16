#list

ingredients = ["water", "milk", "black tea"]
ingredients.append("sugar")  #add

print(f"Ingredients are: {ingredients}")

ingredients.remove("water")
print(f"Ingredients after removing water: {ingredients}")


# add spice to our chai
spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"] 
chai_ingredients.extend(spice_options)
print(f"chai: {chai_ingredients}")

#insert add at specific positions

chai_ingredients.insert(2, "black tea")
print(f"chai: {chai_ingredients}")


#remove something from a particular position

last_added = chai_ingredients.pop()
print(f"{last_added}")
print(f"chai: {chai_ingredients}")


# operator overloading

base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor
print(f"Liquid mix: {full_liquid_mix}")


strong_brew = ["black tea", "water"] * 3
print(f"Strong brew: {strong_brew}")

from operator import itemgetter

# we can have one element in the list but i want a lis with just this string
# bytearray -- in this each element is treated as array

raw_spice_data = bytearray(b"CINNAMON")
print(f"bytes: {raw_spice_data}")


#sets
essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices
# | known as union
print(f"All spices: {all_spices}")


# & known as intersection
common_spices = essential_spices & optional_spices
print(f"Common spices: {common_spices}")

# - known as difference
only_in_essential = essential_spices - optional_spices
print(f"Only in essential: {only_in_essential}")

#membership test

print(f"Is 'cloves' an optional spice? {'cloves' in optional_spices}")

#frozenset -- immutable set to freeze the set

#dictionary -- key value pair

chai_order = dict(type="Massala chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"recipe base: {chai_recipe['base']}")
 #del -- to delete any component
del chai_recipe["liquid"]
print(f"recipe liquid: {chai_recipe['liquid']}")

print(f"Order details (keys): {chai_order.keys()}")
print(f"Order details (values): {chai_order.values()}")
print(f"Order details (items): {chai_order.items()}")


last_item = chai_order.popitem()
print(f"Last item removed: {last_item}")

