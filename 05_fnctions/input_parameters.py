#strings does not chaange. we are just passing on the value of chai here.
chai = "Ginger chai"

def prepare_chai(order):
    print("Preparing", order)

prepare_chai(chai)
print(chai)


#lists can be changed.
chai = [1, 2, 3]

def edit_chai(cup): #cup, here is parameter
    cup[1] = 42

edit_chai(chai)  #chai is an args here
print(chai)


def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("darjeeling", "yes", "low") #positional
make_chai(tea="Green", sugar="Medium", milk="No") #keywords


# this is the practical example of args and *kwargs
#some of the parameters dont have a name while some have names, args with names are also called kwargs
def special_chai(*ingredients, **extras):
    print("Ingredients", ingredients)
    print("Extras", extras)

special_chai("Cinnamon", "Cardamom", sweetner="Honey", foam="yes")

