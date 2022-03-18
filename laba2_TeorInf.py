kolvo_summatorov = int(input("Введите число сумматоров"))
if (kolvo_summatorov == 1):
    a = input("Введите регистры для первого сумматора: ")
    a = a.split(",")
    a = list(a)
    print(a)#убедившись в правильности, принты можно убрать. Чисто для проверки
elif(kolvo_summatorov == 2):
    a = input("Введите регистры для первого сумматора: ")
    b = input("Введите регистры для второго сумматора: ")
    a = a.split(",")
    b = b.split(",")
    a = list(a)
    b = list(b)
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
print(bin1_result[1])
bin2_result = list(bin1_result)
for i in range(7):
    bin2_result[i] = int(bin2_result[i])
print(bin2_result)
gr = []
for i in range(len(bin2_result)-1):
    c = bin2_result[i]
    d = bin2_result[i+1]
    e = c+d
    i = i+1
    gr.append(e)
print(gr)
   
