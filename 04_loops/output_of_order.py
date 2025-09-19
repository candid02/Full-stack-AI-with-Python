#   You want to skip those and stop entirely if someone requests a restricted flavor.
#TASK: skip if flavor is "Out of stock" , break if flavor is "Discontinued"



flavours = ["Ginger", "Out of stock", "Lemon", "Discontinued", "Tulsi"]

for flavor in flavours:
    if flavor == "Out of stock":
        continue
    if flavor == "Discontinued":
        break
    print(f"Discontinued item found")

# for else

staff = [("Amit", 16), ("Zara", 17), ("Raj", 15)]

for name, age in staff:
    if age <= 18:
        print(f"{name} is eligible to manage the staff")
        break
else:
    print("No one is eligible to manage the staff")