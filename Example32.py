import random
lenght =int(input("Введите кол-во эллементов списка: "))
min =int(input("Минимум: "))
max =int(input("Максимум: "))
list = []
result = []
while len(list) <lenght:
    list.append(int(random.randint(1, 10)))
print(list)
i=0
while i<len(list):
    if list[i]>min and list[i]<max:
        result.append(int(i))
        i=+1
    else:
        i=+1
print(result)
