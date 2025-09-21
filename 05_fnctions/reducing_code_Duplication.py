# REDUCING THE CODE DUPLICATION
#sometimes the code that we are writing needs to be utilized at multiple places , so why to write the code again and again maybe we can wrap that code.


# question
#you are managing a busy tea stall.
#you recieve many orders and want to print each customers name along with the type of chai they ordered.
#TASK : write a function print_order(name, chai_type)
#call it multiple times for different customers

def print_order(name, chai_type):
    print(f"{name} ordered {chai_type} chai")

#syntax advantage is that we can just pass on parameters
    

print_order("Aman", "massala")
print_order("Hitesh", "Ginger")
print_order("Jiya", "Tulsi")