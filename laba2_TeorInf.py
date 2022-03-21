import networkx as nx
import matplotlib.pyplot as plt
#Первый абзац - ввод информации
kolvo_summatorov = int(input("Введите число сумматоров: "))
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
#Сделаем функцию
gr1=[]
#b_ = [0,0,0,1,0,0,0,1,0,1,1,0,0,0,1,1,0,1,0,1,1,1,1,1]
def func1(x,y,z,):
    b_ = [x,y,z]
    c2 = int(b_[a[0]-1])
    d2 = int(b_[a[1]-1])
    e2 = str((c2+d2)%2)
    c3 = int(b_[b[0]-1])
    d3 = int(b_[b[1]-1])
    e3 = str((c3+d3)%2)
    #gr1.append(e2+e3)
    gr1.append(e2)
    gr1.append(e3)
    return(gr1)
func1(0,0,0)
func1(1,0,0)
func1(0,1,0)
func1(1,1,0)
func1(0,0,1)
func1(1,0,1)
func1(0,1,1)
func1(1,1,1)
print(gr1)

#строим граф. Его вес рассчитаем зараннее в отдельных переменных (??? как-то в цикле реализовать для разного кол-ва эл-тов)

G = nx.Graph()
 
nodes = ["00(0)", "00(1)", "10(1)", "00(2)", "10(2)","01(2)","11(2)","00(3)","10(3)","01(3)","11(3)"]#узлы зададим точками на диаграмме Витерби. Опять же, вопрос в динамическом образовании этих точек
G.add_nodes_from(nodes)
 
G.add_edge("00(0)", "00(1)", weight=1.0)
G.add_edge("00(0)", "10(1)", weight=2.0)
G.add_edge("00(1)", "00(2)", weight=3.0)
G.add_edge("00(1)", "10(2)", weight=4.0)
G.add_edge("10(1)", "01(2)", weight=5.0)
G.add_edge("10(1)", "11(2)", weight=6.0)
G.add_edge("00(2)", "00(3)", weight=7.0)
G.add_edge("00(2)", "10(3)", weight=8.0)
G.add_edge("10(2)", "01(3)", weight=9.0)
G.add_edge("10(2)", "11(3)", weight=1.0)
G.add_edge("01(2)", "00(3)", weight=1.0)
G.add_edge("01(2)", "10(3)", weight=2.0)
G.add_edge("11(2)", "01(3)", weight=3.0)
G.add_edge("11(2)", "11(3)", weight=4.0)

 
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
print(nx.dijkstra_path(G,"00(0)","01(2)"))
 
plt.show()













   















   
















   

   

   

