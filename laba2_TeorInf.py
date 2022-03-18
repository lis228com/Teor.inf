#Первый абзац - ввод информации
kolvo_summatorov = int(input("Введите число сумматоров"))
if (kolvo_summatorov == 1):
    a = input("Введите регистры для первого сумматора: ")
    a = a.split(",")
    a = list(a)
    for i in range(len(a)):
        a[i] = int(a[i])
    print(a)#убедившись в правильности, принты можно убрать. Чисто для проверки
elif(kolvo_summatorov == 2):
    a = input("Введите регистры для первого сумматора: ")
    b = input("Введите регистры для второго сумматора: ")
    a = a.split(",")
    b = b.split(",")
    a = list(a)
    b = list(b)
    for i in range(len(a)):
        a[i] = int(a[i])
    for i in range(len(b)):
        b[i] = int(b[i])
    print(a)
    print(b)
#затем через элиф добавим 3 сумматора. А в else напишем, чтобы выводило ошибку (например, если ноль сумматоров)
else:
    print("Введено неверное значение")



str_to_conv = input("введите строку: ")
bin_result = ' '.join(format(ord(x), 'b') for x in str_to_conv)
bin1_result = ''.join(format(ord(x), 'b') for x in str_to_conv)
print(bin1_result)#строка из двоичного кода без пробелов
print(bin_result)#строка бит с пробелами (каждый символ отдельно)
revert = ''.join([chr(int(s, 2)) for s in bin_result.split()])#из двоичной в обычную
print(revert)
print(len(bin1_result))
bin2_result = list(bin1_result)
for i in range(len(bin1_result)):
    bin2_result[i] = int(bin2_result[i])
print(bin2_result)
gr = [0,0,0]   #список для сумматоров. Из этого списка берутся эл-ты и складываются на сумматоре
zakodirovannaya_posledovatelnost = []  #в этот список будем класть элементы, получившиеся на сумматоре(сумматорах)

#Теперь пишем алгоритм для сумматора. Если сумматоров>1, то сделать функцию.
for i in range(len(bin2_result)):
    gr.insert(0,bin2_result[i])
    c = gr[a[0]-1]
    print("c= ",c)
    d = gr[a[1]-1]
    print("d= ",d)
    e = c+d
    if (e%2==0):
        e=0
    else:
        e=1
    #теперь второй сумматор
    c1 = gr[b[0]-1]
    d1 = gr[b[1]-1]
    e1 = c1+d1
    if (e1%2==0):
        e1=0
    else:
        e1=1
    zakodirovannaya_posledovatelnost.append(e)
    zakodirovannaya_posledovatelnost.append(e1)
    i = i+1
print(zakodirovannaya_posledovatelnost)
zakodirovannaya_posledovatelnost1 = ''.join(str(n) for n in zakodirovannaya_posledovatelnost)
print(zakodirovannaya_posledovatelnost1)

#кодирование ЗАВЕРШЕНО
#Теперь декодируем

a_=[]
b_ = [0,0,0,1,0,0,0,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1]
#for i in range(6):
c2 = str(b_[a[0]-1])
d2 = str(b_[a[1]-1])
e2 = c2+d2
print(e2)















   

   

   

