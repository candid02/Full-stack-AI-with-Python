# a tea stall owner has a digital token display.fpr every customer in line,
# a token number is printed and chai is served.

# TASK : use a for loop to generate token numbers from 1 to 10 using range()
#print: "Serving chai to token #[number]"

#loop always starts with keywords like for or while

for token in range(1, 11):
    print(f"Serving chai to token #{token}")



# a chai shop makes tea in batches every 15 minutes. you want to simulate 4 batches.
#TASK : use range() to simulate batch numbers , print: "Preparing chai for batch #[number]"


for batch in range(1, 5):
    print(f"Preparing chai for batch #{batch}")


# looping through list -- order names

#you recieve a list of names for chai orders. the goal is to print out the order queue.
# TASK : use a list of names, print : "order ready for [name]"

orders = ["ritu", "ayushi", "riya", "ravnit"]

for name in orders:
    print(f"order ready for {name}")


#you're creating a tea menu board.each item must be numbered. 
# TASK : use enumerate() to print menu items with numbers.

# ENUMERATE : 
# in this each number gets numbered
# it adds a counter to an iterable and returns it in a form of enumerating object.

menu = ["Green", "Lemon", "Spiced", "Mint"]


for m in menu:
    print(f"Menu item is {m}")

for idx, item in enumerate(menu, start=1):
    print(f"Menu item {idx} is {item}")
 

# You're preparing an order summary with customer names and their total bill.
#TASK : use two lists: one for names and one for bills. print: "[Name]paid rupees [amount]"

#Zip -- combines two lists into a single iterable of tuples

names = ["Ritu", "Ayushi", "Riya", "Ravnit"]
bills = [50, 70, 100, 55]

for name, amount in zip(names, bills):
    print(f"{name} paid rupees {amount}")
