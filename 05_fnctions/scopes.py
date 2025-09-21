#local scope --- the validation of this variable is just inside this method
def serve_chai():
    chai_type = "Massala"
    print(f"Inside function {chai_type}")

chai_type = "Lemon"
serve_chai()
print(f"Outside function: {chai_type}")

# Enclosing scope --- Inside one function, another function can use the variables of the outer (enclosing) function.
#(function inside a function --- nested function) 

def chai_counter():
    chai_order = "lemon"
    def print_order():
        chai_order = "Ginger"
        print("Inner:", chai_order)

    print("Outer:", chai_order)

#global scope Variables or functions that are created outside of all functions or classes and can be accessed from anywhere in the program.

chai_order = "Tulsi"
chai_counter()
print("Global :", chai_order)




