#nonlocal --- a keyword that refers something that is outside the scope of it means not the global scope but the nearest enclosing scope.

def update_order():
    chai_type = "Elaichi"
    def kitchen():
        nonlocal chai_type
        chai_type = "kesar"
    kitchen()
    print("After kitchen update", chai_type)

update_order()