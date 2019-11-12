n = int(input("Введите количество элементов: "))   # считываем количество элемент в списке
a = []  # заводим пустой список
nomer_element = 1
for i in range(n):
    new_element = int(input('Введите  элемент:{0} '.format(i+1))) # считываем очередной элемент
    a.append(new_element)  # добавляем его в список
print(a)