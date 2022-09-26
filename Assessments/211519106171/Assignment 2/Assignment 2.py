import random

temp = random.randint(20,100)
print(temp,"degrees")

if(temp < 40):
    print("Alarm: Normal Temperature")
elif(40 < temp < 80):
    print("Alarm: High Temperature!!")
elif(80 < temp < 90):
    print("Alarm: Very High Temperature!!")
elif(temp > 90):
    print("Alarm: Critically High Temperature!! Attention is needed!!")



