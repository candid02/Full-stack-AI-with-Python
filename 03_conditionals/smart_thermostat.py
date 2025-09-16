#You are building a smart thermostat alert system:
#if the device_status is "active" and temperature > 35 -- warn : "high temperature" 
#else: "temperature normal" , if device is off -- "device is offline"


device_status = "active"
temperature = 38

if device_status == "active":
    pass
else:
    print("Device is offline")


# device is active , now we will simply check for if temp is above 35 it will put a warning
#otherwise we say temperature is normal.

device_status = "active"
temperature = 38

if device_status == "active":
    if temperature > 35:
        print("High Temperature alert!")
    else:
        print("Temperature is normal.")
else:
    print("Device is offline")
