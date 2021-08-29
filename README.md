# hardCheck
### This is python package for check your cpu and disk usage

### Developed by Diac Adrian and inspired from the 'Using Python to interact with the operating system' from Google


## Example of how to use:
``` python
from hardcheck import cpuOverUsage
from hardcheck import diskOverUsage

isOverUsage,message=cpuOverUsage()

print(isOverUsage) #will print true or false

print(message) #will print "It's using more than 50%" or "It's using less than 50%"

isOverUsage,message=diskOverUsage('./') #will raise a Value Error if path doesn't exists

print(isOverUsage) #will print true or false

print(message) #will print "It's using more than 50%" or "It's using less than 50%"
```
### For now verifies just the cpu and disk and also uses psutil and shutil

## Also included a test workflow for the two modules