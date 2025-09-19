# You want to simulate tea heating. it starts at 40C and boils at 100 c
# TASK : use a while loop.
# Increase temperature by 15 until it reaches or exceeds 100.print each temperature step.

# while loops

temperature = 40

while temperature < 100:
    print(f"Current temperature: {temperature}C")
    #temperature = temperature + 15
    temperature += 15

print("Tea is ready to boil")

