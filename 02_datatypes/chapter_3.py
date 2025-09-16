#strings

chai_type = "Ginger chai"
customer_name = "Ritu"

print(f"Order for {customer_name}: {chai_type} please !")

chai_description = "Aromatic and Bold"
print(f"First word: {chai_description[0:7]}")


print(f"First word: {chai_description[::-1]}") #-1 is a shorthand for reversing the whole string



# Encoded strings 
label_text = "Chai Spe`cial"
encoded_label = label_text.encode("utf-8")
print(f"Non encoded label: {label_text}")
print(f"Encoded label: {encoded_label}")

decoded_label = encoded_label.decode("utf-8")
print(f"decoded label: {decoded_label}")