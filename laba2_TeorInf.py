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
print("Получили закодированную строку: ",zakodirovannaya_posledovatelnost1)

#кодирование ЗАВЕРШЕНО
#Теперь декодируем
#Сделаем функцию
gr1=[]
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
for i in range(len(gr1)):
    gr1[i] = int(gr1[i])
print(gr1)

#строим граф. Его вес рассчитаем зараннее в отдельных переменных
#Перед этим напишем функцию для расчета веса
def ves(e,e_,k,k_): #Здесь к и к_ - это ноль либо единица на графе Витерби, а е и е_ - это ноль либо единица в получившейся последовательности после кодирования.
    summ = 0
    if (k != e):
        summ = summ +1
    else:
        summ = summ
    if (k_ != e_):
        summ = summ + 1
    else:
        summ = summ
    return summ



G = nx.DiGraph()
 
nodes = ["00(0)", "00(1)", "10(1)", "00(2)", "10(2)","01(2)","11(2)","00(3)","10(3)","01(3)","11(3)"]#узлы зададим точками на диаграмме Витерби. Опять же, вопрос в динамическом образовании этих точек
G.add_nodes_from(nodes)
 
G.add_edge("00(0)", "00(1)", weight=ves(zakodirovannaya_posledovatelnost[0],zakodirovannaya_posledovatelnost[1],gr1[0],gr1[1]))
G.add_edge("00(0)", "10(1)", weight=ves(zakodirovannaya_posledovatelnost[0],zakodirovannaya_posledovatelnost[1],gr1[2],gr1[3]))
G.add_edge("00(1)", "00(2)", weight=ves(zakodirovannaya_posledovatelnost[2],zakodirovannaya_posledovatelnost[3],gr1[0],gr1[1]))
G.add_edge("00(1)", "10(2)", weight=ves(zakodirovannaya_posledovatelnost[2],zakodirovannaya_posledovatelnost[3],gr1[2],gr1[3]))
G.add_edge("10(1)", "01(2)", weight=ves(zakodirovannaya_posledovatelnost[2],zakodirovannaya_posledovatelnost[3],gr1[4],gr1[5]))
G.add_edge("10(1)", "11(2)", weight=ves(zakodirovannaya_posledovatelnost[2],zakodirovannaya_posledovatelnost[3],gr1[6],gr1[7]))
G.add_edge("00(2)", "00(3)", weight=ves(zakodirovannaya_posledovatelnost[4],zakodirovannaya_posledovatelnost[5],gr1[0],gr1[1]))
G.add_edge("00(2)", "10(3)", weight=ves(zakodirovannaya_posledovatelnost[4],zakodirovannaya_posledovatelnost[5],gr1[2],gr1[3]))
G.add_edge("10(2)", "01(3)", weight=ves(zakodirovannaya_posledovatelnost[4],zakodirovannaya_posledovatelnost[5],gr1[4],gr1[5]))
G.add_edge("10(2)", "11(3)", weight=ves(zakodirovannaya_posledovatelnost[4],zakodirovannaya_posledovatelnost[5],gr1[6],gr1[7]))
G.add_edge("01(2)", "00(3)", weight=ves(zakodirovannaya_posledovatelnost[4],zakodirovannaya_posledovatelnost[5],gr1[8],gr1[9]))
G.add_edge("01(2)", "10(3)", weight=ves(zakodirovannaya_posledovatelnost[4],zakodirovannaya_posledovatelnost[5],gr1[10],gr1[11]))
G.add_edge("11(2)", "01(3)", weight=ves(zakodirovannaya_posledovatelnost[4],zakodirovannaya_posledovatelnost[5],gr1[12],gr1[13]))
G.add_edge("11(2)", "11(3)", weight=ves(zakodirovannaya_posledovatelnost[4],zakodirovannaya_posledovatelnost[5],gr1[14],gr1[15]))
G.add_edge("00(3)", "00(4)", weight=ves(zakodirovannaya_posledovatelnost[6],zakodirovannaya_posledovatelnost[7],gr1[0],gr1[1]))
G.add_edge("00(3)", "10(4)", weight=ves(zakodirovannaya_posledovatelnost[6],zakodirovannaya_posledovatelnost[7],gr1[2],gr1[3]))
G.add_edge("10(3)", "01(4)", weight=ves(zakodirovannaya_posledovatelnost[6],zakodirovannaya_posledovatelnost[7],gr1[4],gr1[5]))
G.add_edge("10(3)", "11(4)", weight=ves(zakodirovannaya_posledovatelnost[6],zakodirovannaya_posledovatelnost[7],gr1[6],gr1[7]))
G.add_edge("01(3)", "00(4)", weight=ves(zakodirovannaya_posledovatelnost[6],zakodirovannaya_posledovatelnost[7],gr1[8],gr1[9]))
G.add_edge("01(3)", "10(4)", weight=ves(zakodirovannaya_posledovatelnost[6],zakodirovannaya_posledovatelnost[7],gr1[10],gr1[11]))
G.add_edge("11(3)", "01(4)", weight=ves(zakodirovannaya_posledovatelnost[6],zakodirovannaya_posledovatelnost[7],gr1[12],gr1[13]))
G.add_edge("11(3)", "11(4)", weight=ves(zakodirovannaya_posledovatelnost[6],zakodirovannaya_posledovatelnost[7],gr1[14],gr1[15]))
G.add_edge("00(4)", "00(5)", weight=ves(zakodirovannaya_posledovatelnost[8],zakodirovannaya_posledovatelnost[9],gr1[0],gr1[1]))
G.add_edge("00(4)", "10(5)", weight=ves(zakodirovannaya_posledovatelnost[8],zakodirovannaya_posledovatelnost[9],gr1[2],gr1[3]))
G.add_edge("10(4)", "01(5)", weight=ves(zakodirovannaya_posledovatelnost[8],zakodirovannaya_posledovatelnost[9],gr1[4],gr1[5]))
G.add_edge("10(4)", "11(5)", weight=ves(zakodirovannaya_posledovatelnost[8],zakodirovannaya_posledovatelnost[9],gr1[6],gr1[7]))
G.add_edge("01(4)", "00(5)", weight=ves(zakodirovannaya_posledovatelnost[8],zakodirovannaya_posledovatelnost[9],gr1[8],gr1[9]))
G.add_edge("01(4)", "10(5)", weight=ves(zakodirovannaya_posledovatelnost[8],zakodirovannaya_posledovatelnost[9],gr1[10],gr1[11]))
G.add_edge("11(4)", "01(5)", weight=ves(zakodirovannaya_posledovatelnost[8],zakodirovannaya_posledovatelnost[9],gr1[12],gr1[13]))
G.add_edge("11(4)", "11(5)", weight=ves(zakodirovannaya_posledovatelnost[8],zakodirovannaya_posledovatelnost[9],gr1[14],gr1[15]))
G.add_edge("00(5)", "00(6)", weight=ves(zakodirovannaya_posledovatelnost[10],zakodirovannaya_posledovatelnost[11],gr1[0],gr1[1]))
G.add_edge("00(5)", "10(6)", weight=ves(zakodirovannaya_posledovatelnost[10],zakodirovannaya_posledovatelnost[11],gr1[2],gr1[3]))
G.add_edge("10(5)", "01(6)", weight=ves(zakodirovannaya_posledovatelnost[10],zakodirovannaya_posledovatelnost[11],gr1[4],gr1[5]))
G.add_edge("10(5)", "11(6)", weight=ves(zakodirovannaya_posledovatelnost[10],zakodirovannaya_posledovatelnost[11],gr1[6],gr1[7]))
G.add_edge("01(5)", "00(6)", weight=ves(zakodirovannaya_posledovatelnost[10],zakodirovannaya_posledovatelnost[11],gr1[8],gr1[9]))
G.add_edge("01(5)", "10(6)", weight=ves(zakodirovannaya_posledovatelnost[10],zakodirovannaya_posledovatelnost[11],gr1[10],gr1[11]))
G.add_edge("11(5)", "01(6)", weight=ves(zakodirovannaya_posledovatelnost[10],zakodirovannaya_posledovatelnost[11],gr1[12],gr1[13]))
G.add_edge("11(5)", "11(6)", weight=ves(zakodirovannaya_posledovatelnost[10],zakodirovannaya_posledovatelnost[11],gr1[14],gr1[15]))
G.add_edge("00(6)", "00(7)", weight=ves(zakodirovannaya_posledovatelnost[12],zakodirovannaya_posledovatelnost[13],gr1[0],gr1[1]))
G.add_edge("00(6)", "10(7)", weight=ves(zakodirovannaya_posledovatelnost[12],zakodirovannaya_posledovatelnost[13],gr1[2],gr1[3]))
G.add_edge("10(6)", "01(7)", weight=ves(zakodirovannaya_posledovatelnost[12],zakodirovannaya_posledovatelnost[13],gr1[4],gr1[5]))
G.add_edge("10(6)", "11(7)", weight=ves(zakodirovannaya_posledovatelnost[12],zakodirovannaya_posledovatelnost[13],gr1[6],gr1[7]))
G.add_edge("01(6)", "00(7)", weight=ves(zakodirovannaya_posledovatelnost[12],zakodirovannaya_posledovatelnost[13],gr1[8],gr1[9]))
G.add_edge("01(6)", "10(7)", weight=ves(zakodirovannaya_posledovatelnost[12],zakodirovannaya_posledovatelnost[13],gr1[10],gr1[11]))
G.add_edge("11(6)", "01(7)", weight=ves(zakodirovannaya_posledovatelnost[12],zakodirovannaya_posledovatelnost[13],gr1[12],gr1[13]))
G.add_edge("11(6)", "11(7)", weight=ves(zakodirovannaya_posledovatelnost[12],zakodirovannaya_posledovatelnost[13],gr1[14],gr1[15]))


 
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

#теперь сравним 4 пути и выбираем с наименьшим весом - это и будет "наш"
gr2 = []
if (nx.dijkstra_path_length(G,"00(0)","00(7)")==0):
    print(nx.dijkstra_path(G,"00(0)","00(7)"))
    for i in range(1,8):
        gr2.append(nx.dijkstra_path(G,"00(0)","00(7)")[i][0])
    print("Изначальная последовательность: ",gr2)
elif (nx.dijkstra_path_length(G,"00(0)","01(7)")==0):
    print(nx.dijkstra_path(G,"00(0)","01(7)"))
    for i in range(1,8):
        gr2.append(nx.dijkstra_path(G,"00(0)","01(7)")[i][0])
    print("Изначальная последовательность: ",gr2)
elif (nx.dijkstra_path_length(G,"00(0)","10(7)")==0):
    print(nx.dijkstra_path(G,"00(0)","10(7)"))
    for i in range(1,8):
        gr2.append(nx.dijkstra_path(G,"00(0)","10(7)")[i][0])
    print("Изначальная последовательность: ",gr2)
elif (nx.dijkstra_path_length(G,"00(0)","11(7)")==0):
    print(nx.dijkstra_path(G,"00(0)","11(7)"))
    for i in range(1,8):
        gr2.append(nx.dijkstra_path(G,"00(0)","11(7)")[i][0])
    print("Изначальная последовательность: ",gr2)
else:
    print("Путей с весом ноль нет")

plt.show()

#преобразуем последовательность в изначальную строку
strOfStrings = ''.join(gr2)
print(strOfStrings)
revert = ''.join([chr(int(s, 2)) for s in strOfStrings.split()])#из двоичной в обычную
print(revert)












   
















   














   














   














   















   
















   

   

   

