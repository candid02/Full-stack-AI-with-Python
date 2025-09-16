#you run an online tea store. if the order amount is more than rupees 300
#the delivery is free otherwise, it costs rupees 30.
#TASK: input: order_amount , use ternary operators to decide delivery fees. 

order_amount = int(input("Enter the order amount: "))

#print(f"order amount: {type(order_amount)}")

#using ternary operator

delivery_fees = 0 if order_amount > 300 else 30

print(f"Delivery fees is : {delivery_fees}")





