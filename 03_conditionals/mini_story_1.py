# Project 1 : mini projects on conditionals

#you are creating a system notification system for a smart kettle.
#it should remind the user only when the kettle has finished boiling.
#a variable kettle_boiled = True
#if boiled, show: "Kettle done! Time to make chai."

kettle_boiled = True

if kettle_boiled:
    print("Kettle Done! Time to make chai.")

#PROJECT 2:

#a local cafe wants a program that suggests a snack. 
# if a customer asks for a cookies or samosa, it confirms the order, otherwise it says its not available.

#Task 1. take snaks input.
#if its cookies or samosa confirm the order else, show unavailability
# (how to take input from command line)

snack = input("Enter your preferred snack: ")
print(f"user said: {snack}")

snack = input("Enter your preferred snack: ").lower()

if snack == "cookies" or snack == "samosa":
    print(f"Great choice ! We'll  serve you {snack}")
else:
    print(f"Sorry, we only serve cookies or samosa with tea")



