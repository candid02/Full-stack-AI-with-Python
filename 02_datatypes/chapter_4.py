masala_spices = ("cardamom", "cloves", "cinamomom")

(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}")


#special ratios

ginger_ratio, cardamom_ratio = 2, 1
print(f"Ratio is G: {ginger_ratio}, C: {cardamom_ratio} and C : {cardamom_ratio}")

# if we want to switch/ swap the values
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(f"Ratio is G: {ginger_ratio}, C: {cardamom_ratio} and C : {cardamom_ratio}")


#membership
print(f"Is ginger in masala spices ? {'ginger' in masala_spices}")