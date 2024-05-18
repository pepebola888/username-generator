import time

print("generador de nombres de usuario v1.0")
print("hecho por pepe bola")
print("cual es tu nombre?")
name = input(str)
    
while len(name) <= 2:
    print("intentalo denuevo:")
    name = input(str)
    
print("cual es tu apellido?")
last_name = input(str)

while len(last_name) <= 2:
    print("intentalo denuevo:")
    last_name = input(str)

print("cuandtos años tienes?")
age = input(int)

while len(age) <= 0 and type(age) == int:
    print("intentalo denuevo:")
    age = input(int)

print('generando nombre de usuario, esto podria tomar unos segundos...')
time.sleep(5)
print("tu nuevo nombre de usuario es:")

age = int(age)
age = age * 18
    
name = name.capitalize()
last_name = last_name.capitalize()
age = str(age)

print("Xx_"+ name + last_name + "Pro" + age + "_xX")
print("te gusta? (Y/N)")

answer = input(str)
answer = answer.upper()

if answer == "Y":
    print("=)")
    time.sleep(4)
else:
    counter = 1
    while counter <= 1000:
        print("puta >=(")
        counter += 1
time.sleep(0.15)
quit()