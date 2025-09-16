#you are building a ticket info system for a railway app.
#based on seat type, show its features.
#TASK: input: "sleeper", "AC", "General", "luxury"
#match using match-case and unknown -- show: "invalid seat type"

seat_type = input("Enter seat type (sleeper/AC/general/luxury)").lower()

#match and case
match seat_type: 
    case "sleeper":
        print("Sleeper - No AC, beds available")
    case "ac":
        print("AC - Air-conditioned, comfy ride")
    case "general":
        print("General - cheapest option, no reservation")
    case "luxury":
        print("Luxury - Premium seats wwith meals")
    case _:
        print("Invalid seat type.")

