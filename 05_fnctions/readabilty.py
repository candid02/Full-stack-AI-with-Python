# you sell different chai sizes.
#Instead of writing formulas everywhere, create a function.
#TASK :
#write calculate_bill(cups, price_per_cup)
#return total bill 
#use this function for multiple orders


def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup

my_bill = calculate_bill(3, 22)
print(my_bill)

#we can call this method directly like this
print("Order for table 2:", calculate_bill(2, 50))