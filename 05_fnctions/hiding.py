#You're building a simple app that register users.
#you want to seperate concerns: getting input, validating it, and saving it.
#TASK : write register_user that calls:
#get_input() 
#validate_input()
#save_to_db()

def get_input():
    print("Getting user input")

def validate_input():
    print("Validating the user info")

def save_to_db():
    print("saving to database")

def register_user():
    get_input()
    validate_input()
    save_to_db()
    print("User regitration complete")

register_user()