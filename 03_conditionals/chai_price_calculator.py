#a tea stall offers different prices for different cup sizes.write a program that 
#calculates the price based on size.
#TASK: input : "small","medium","large"
#small = 10 rupees, medium = 15 rupees, large = 20 rupees
#if invalid: show "unknown cup size"

 
cup = input("Choose your cup size (small/medium/large): ").lower()

if cup == "small":
    print("Price is 10 rupees")
elif cup == "medium":
    print("Price is 15 rupees")
elif cup == "large":
    print("Price is 20 rupees")
else: 
    print("Unknown cup size")