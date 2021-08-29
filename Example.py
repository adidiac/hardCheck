from hardcheck import cpuOverUsage
from hardcheck import diskOverUsage

isOverUsage,message=cpuOverUsage()

print(isOverUsage) #will print true or false

print(message) #will print "It's using more than 50%" or "It's using less than 50%"

isOverUsage,message=diskOverUsage('./') #will raise a Value Error if path doesn't exists

print(isOverUsage) #will print true or false

print(message) #will print "It's using more than 50%" or "It's using less than 50%"