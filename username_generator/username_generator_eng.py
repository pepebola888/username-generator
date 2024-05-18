import time

print("welcome to username generator v1.0")
print("by pepe bola")
print("what's ur name?")
name = input(str)
    
while len(name) <= 2:
    print("try again:")
    name = input(str)
    
print("what's ur last name?")
last_name = input(str)

while len(last_name) <= 2:
    print("try again:")
    last_name = input(str)

print("how old r u?")
age = input(int)

while len(age) <= 0 and type(age) == int:
    print("try again:")
    age = input(int)

print('generating username, this may take some seconds...')
time.sleep(5)
print("ur brand new username is:")

age = int(age)
age = age * 18
    
name = name.capitalize()
last_name = last_name.capitalize()
age = str(age)

print("Xx_"+ name + last_name + "Pro" + age + "_xX")
print("do ya' like it? (Y/N)")

answer = input(str)
answer = answer.upper()

if answer == "Y":
    print("YAY =D")
    time.sleep(4)
else:
    counter = 1
    while counter <= 1000:
        print("KILL UR SELF")
        counter += 1
time.sleep(0.15)
quit()