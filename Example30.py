lenght =int(input("Введите кол-во эллементов списка: "))
a1 =int(input("Первый эл-нт: "))
d =int(input("Разность: "))
list = []
list.append(int(a1))
i=1
n=i+1
while i<lenght:
    list.append(int(list[0]+((n-1)*d)))
    i+=1
    n+=1
print(list)
