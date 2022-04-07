import networkx as nx
import matplotlib.pyplot as plt

# Первый абзац - ввод информации


str_to_conv = input("введите строку: ")
bin_result = ' '.join(format(ord(x), 'b') for x in str_to_conv)
bin1_result = ''.join(format(ord(x), 'b') for x in str_to_conv)
print(bin1_result)  # строка из двоичного кода без пробелов
print(bin_result)  # строка бит с пробелами (каждый символ отдельно)
bin2_result = list(bin1_result)
for i in range(len(bin1_result)):
    bin2_result[i] = int(bin2_result[i])
print(bin2_result)
gr = [0, 0, 0]  # список для сумматоров. Из этого списка берутся эл-ты и складываются на сумматоре
zakodirovannaya_posledovatelnost = []  # в этот список будем класть элементы, получившиеся на сумматоре(сумматорах)

gr5 = []
for i in range(len(bin_result)):
    if bin_result[i] == " ":
        gr5.append(i)
print("gr5", gr5)

kolvo_summatorov = int(input("Введите число сумматоров: "))
spisok=[]
kolvo_summatorov = int(input("Введите число сумматоров: "))
for i in range(kolvo_summatorov):
    spisok.append([int(y) for y in input("Введите регистры для n-го сумматора: ").split()])
print(spisok)

    # Теперь пишем алгоритм для сумматора. Если сумматоров>1, то сделать функцию.
for i in range(len(bin2_result)):
    gr.insert(0, bin2_result[i])
    j=0
    for j in range(kolvo_summatorov):
        c = gr[spisok[j][0] - 1]
        d = gr[spisok[j][1] - 1]
        e = c + d
        if (e % 2 == 0):
            e = 0
        else:
            e = 1
        zakodirovannaya_posledovatelnost.append(e)
        j=j+1
print(zakodirovannaya_posledovatelnost)
zakodirovannaya_posledovatelnost1 = ''.join(str(n) for n in zakodirovannaya_posledovatelnost)
print("Получили закодированную строку: ", zakodirovannaya_posledovatelnost1)
# кодирование ЗАВЕРШЕНО
# Теперь декодируем
# Сделаем функцию (это цифры над линиями в Витерби)
gr1 = []
if (kolvo_summatorov == 1):
    def func1(x, y):
        b_ = [x, y]
        c2 = int(b_[a[0] - 1])
        d2 = int(b_[a[1] - 1])
        e2 = str((c2 + d2) % 2)
        gr1.append(e2)
        return (gr1)


    func1(0, 0)
    func1(0, 1)
    func1(1, 0)
    func1(1, 1)
    for i in range(len(gr1)):
        gr1[i] = int(gr1[i])
    print("gr1: ", gr1)

elif (kolvo_summatorov == 2):
    def func1(x, y, z):
        b_ = [x, y, z]
        c2 = int(b_[a[0] - 1])
        d2 = int(b_[a[1] - 1])
        e2 = str((c2 + d2) % 2)
        c3 = int(b_[b[0] - 1])
        d3 = int(b_[b[1] - 1])
        e3 = str((c3 + d3) % 2)
        gr1.append(e2)
        gr1.append(e3)
        return (gr1)


    func1(0, 0, 0)
    func1(1, 0, 0)
    func1(0, 1, 0)
    func1(1, 1, 0)
    func1(0, 0, 1)
    func1(1, 0, 1)
    func1(0, 1, 1)
    func1(1, 1, 1)
    for i in range(len(gr1)):
        gr1[i] = int(gr1[i])
    print(gr1)

elif (kolvo_summatorov == 3):
    def func1(x, y, p_, z_):
        b_ = [x, y, p_, z_]
        c2 = int(b_[a[0] - 1])
        d2 = int(b_[a[1] - 1])
        e2 = str((c2 + d2) % 2)
        c3 = int(b_[b[0] - 1])
        d3 = int(b_[b[1] - 1])
        e3 = str((c3 + d3) % 2)
        c4 = int(b_[z[0] - 1])
        d4 = int(b_[z[1] - 1])
        e4 = str((c4 + d4) % 2)
        gr1.append(e2)
        gr1.append(e3)
        gr1.append(e4)
        return (gr1)
    func1(0, 0, 0, 0)
    func1(1, 0, 0, 0)
    func1(0, 0, 0, 1)
    func1(1, 0, 0, 1)
    func1(0, 0, 1, 0)
    func1(1, 0, 1, 0)
    func1(0, 0, 1, 1)
    func1(1, 0, 1, 1)
    func1(0, 1, 0, 0)
    func1(1, 1, 0, 0)
    func1(0, 1, 0, 1)
    func1(1, 1, 0, 1)
    func1(0, 1, 1, 0)
    func1(1, 1, 1, 0)
    func1(0, 1, 1, 1)
    func1(1, 1, 1, 1)
    for i in range(len(gr1)):
        gr1[i] = int(gr1[i])
    print(gr1)

else:
    print("Неверное кол-во сумматоров")

# строим граф. Его вес рассчитаем зараннее в отдельных переменных
# Перед этим напишем функцию для расчета веса
if (kolvo_summatorov == 1):
    def ves(e,
            k):  # Здесь к и к_ - это ноль либо единица на графе Витерби, а е и е_ - это ноль либо единица в получившейся последовательности после кодирования.
        summ = 0
        if (k != e):
            summ = summ + 1
        else:
            summ = summ
        return summ

elif (kolvo_summatorov == 2):
    def ves(e, e_, k,
            k_):  # Здесь к и к_ - это ноль либо единица на графе Витерби, а е и е_ - это ноль либо единица в получившейся последовательности после кодирования.
        summ = 0
        if (k != e):
            summ = summ + 1
        else:
            summ = summ
        if (k_ != e_):
            summ = summ + 1
        else:
            summ = summ
        return summ

elif (kolvo_summatorov == 3):
    def ves(e, e_, e__, k, k_,
            k__):  # Здесь к и к_ - это ноль либо единица на графе Витерби, а е и е_ - это ноль либо единица в получившейся последовательности после кодирования.
        summ = 0
        if (k != e):
            summ = summ + 1
        else:
            summ = summ
        if (k_ != e_):
            summ = summ + 1
        else:
            summ = summ
        if (k__ != e__):
            summ = summ + 1
        else:
            summ = summ
        return summ
else:
    print("Неверное кол-во сумматоров")

G = nx.DiGraph()
nodes = []
if (kolvo_summatorov == 1):
    for i in range(len(bin1_result) + 1):  # цикл для создания узлов графа
        u = "0"
        u_ = "1"
        p = str(i)
        nodes.append(u + p)
        nodes.append(u_ + p)
    print("Список узлов", nodes)

    G.add_nodes_from(nodes)


    def func3(index1, index2):  # функция для постройки графа
        G.add_edge(nodes[index1], nodes[index1 + 2], weight=ves(zakodirovannaya_posledovatelnost[index2], gr1[0]))
        G.add_edge(nodes[index1], nodes[index1 + 3], weight=ves(zakodirovannaya_posledovatelnost[index2], gr1[1]))
        G.add_edge(nodes[index1 + 1], nodes[index1 + 2], weight=ves(zakodirovannaya_posledovatelnost[index2], gr1[2]))
        G.add_edge(nodes[index1 + 1], nodes[index1 + 3], weight=ves(zakodirovannaya_posledovatelnost[index2], gr1[3]))


    m_ = 0
    n_ = 0
    for i in range(len(bin1_result)):  # цикл для создания всех ребер графа.
        func3(m_, n_)
        m_ = m_ + 2
        n_ = n_ + 1

elif (kolvo_summatorov == 2):
    for i in range(len(bin1_result) + 1):  # цикл для создания узлов графа
        u = "00"
        u_ = "10"
        u__ = "01"
        u___ = "11"
        p = str(i)
        nodes.append(u + p)
        nodes.append(u_ + p)
        nodes.append(u__ + p)
        nodes.append(u___ + p)
    print("Список узлов", nodes)

    G.add_nodes_from(nodes)


    def func3(index1, index2):  # функция для постройки графа
        G.add_edge(nodes[index1], nodes[index1 + 4],
                   weight=ves(zakodirovannaya_posledovatelnost[index2], zakodirovannaya_posledovatelnost[index2 + 1],
                              gr1[0], gr1[1]))
        G.add_edge(nodes[index1], nodes[index1 + 5],
                   weight=ves(zakodirovannaya_posledovatelnost[index2], zakodirovannaya_posledovatelnost[index2 + 1],
                              gr1[2], gr1[3]))
        G.add_edge(nodes[index1 + 1], nodes[index1 + 6],
                   weight=ves(zakodirovannaya_posledovatelnost[index2], zakodirovannaya_posledovatelnost[index2 + 1],
                              gr1[4], gr1[5]))
        G.add_edge(nodes[index1 + 1], nodes[index1 + 7],
                   weight=ves(zakodirovannaya_posledovatelnost[index2], zakodirovannaya_posledovatelnost[index2 + 1],
                              gr1[6], gr1[7]))
        G.add_edge(nodes[index1 + 2], nodes[index1 + 4],
                   weight=ves(zakodirovannaya_posledovatelnost[index2], zakodirovannaya_posledovatelnost[index2 + 1],
                              gr1[8], gr1[9]))
        G.add_edge(nodes[index1 + 2], nodes[index1 + 5],
                   weight=ves(zakodirovannaya_posledovatelnost[index2], zakodirovannaya_posledovatelnost[index2 + 1],
                              gr1[10], gr1[11]))
        G.add_edge(nodes[index1 + 3], nodes[index1 + 6],
                   weight=ves(zakodirovannaya_posledovatelnost[index2], zakodirovannaya_posledovatelnost[index2 + 1],
                              gr1[12], gr1[13]))
        G.add_edge(nodes[index1 + 3], nodes[index1 + 7],
                   weight=ves(zakodirovannaya_posledovatelnost[index2], zakodirovannaya_posledovatelnost[index2 + 1],
                              gr1[14], gr1[15]))


    m_ = 0
    n_ = 0
    for i in range(len(bin1_result)):  # цикл для создания всех ребер графа.
        func3(m_, n_)
        m_ = m_ + 4
        n_ = n_ + 2


elif (kolvo_summatorov == 3):
    for i in range(len(bin1_result) + 1):  # цикл для создания узлов графа
        u = "000"
        u_ = "001"
        u__ = "010"
        u___ = "011"
        u____ = "100"
        u_____ = "101"
        u______ = "110"
        u_______ = "111"
        p = str(i)
        nodes.append(u + p)
        nodes.append(u_ + p)
        nodes.append(u__ + p)
        nodes.append(u___ + p)
        nodes.append(u____ + p)
        nodes.append(u_____ + p)
        nodes.append(u______ + p)
        nodes.append(u_______ + p)
    print("Список узлов", nodes)

    G.add_nodes_from(nodes)


    def func3(index1, index2):  # функция для постройки графа
        G.add_edge(nodes[index1], nodes[index1 + 8],
                   weight=ves(zakodirovannaya_posledovatelnost[index2], zakodirovannaya_posledovatelnost[index2 + 1],
                              zakodirovannaya_posledovatelnost[index2 + 2], gr1[0], gr1[1], gr1[2]))
        G.add_edge(nodes[index1], nodes[index1 + 12],
                   weight=ves(zakodirovannaya_posledovatelnost[index2], zakodirovannaya_posledovatelnost[index2 + 1],
                              zakodirovannaya_posledovatelnost[index2 + 2], gr1[3], gr1[4], gr1[5]))
        G.add_edge(nodes[index1 + 1], nodes[index1 + 8],
                   weight=ves(zakodirovannaya_posledovatelnost[index2], zakodirovannaya_posledovatelnost[index2 + 1],
                              zakodirovannaya_posledovatelnost[index2 + 2], gr1[6], gr1[7], gr1[8]))
        G.add_edge(nodes[index1 + 1], nodes[index1 + 12],
                   weight=ves(zakodirovannaya_posledovatelnost[index2], zakodirovannaya_posledovatelnost[index2 + 1],
                              zakodirovannaya_posledovatelnost[index2 + 2], gr1[9], gr1[10], gr1[11]))
        G.add_edge(nodes[index1 + 2], nodes[index1 + 9],
                   weight=ves(zakodirovannaya_posledovatelnost[index2], zakodirovannaya_posledovatelnost[index2 + 1],
                              zakodirovannaya_posledovatelnost[index2 + 2], gr1[12], gr1[13], gr1[14]))
        G.add_edge(nodes[index1 + 2], nodes[index1 + 13],
                   weight=ves(zakodirovannaya_posledovatelnost[index2], zakodirovannaya_posledovatelnost[index2 + 1],
                              zakodirovannaya_posledovatelnost[index2 + 2], gr1[15], gr1[16], gr1[17]))
        G.add_edge(nodes[index1 + 3], nodes[index1 + 9],
                   weight=ves(zakodirovannaya_posledovatelnost[index2], zakodirovannaya_posledovatelnost[index2 + 1],
                              zakodirovannaya_posledovatelnost[index2 + 2], gr1[18], gr1[19], gr1[20]))
        G.add_edge(nodes[index1 + 3], nodes[index1 + 13],
                   weight=ves(zakodirovannaya_posledovatelnost[index2], zakodirovannaya_posledovatelnost[index2 + 1],
                              zakodirovannaya_posledovatelnost[index2 + 2], gr1[21], gr1[22], gr1[23]))
        G.add_edge(nodes[index1 + 4], nodes[index1 + 10],
                   weight=ves(zakodirovannaya_posledovatelnost[index2], zakodirovannaya_posledovatelnost[index2 + 1],
                              zakodirovannaya_posledovatelnost[index2 + 2], gr1[24], gr1[25], gr1[26]))
        G.add_edge(nodes[index1 + 4], nodes[index1 + 14],
                   weight=ves(zakodirovannaya_posledovatelnost[index2], zakodirovannaya_posledovatelnost[index2 + 1],
                              zakodirovannaya_posledovatelnost[index2 + 2], gr1[27], gr1[28], gr1[29]))
        G.add_edge(nodes[index1 + 5], nodes[index1 + 10],
                   weight=ves(zakodirovannaya_posledovatelnost[index2], zakodirovannaya_posledovatelnost[index2 + 1],
                              zakodirovannaya_posledovatelnost[index2 + 2], gr1[30], gr1[31], gr1[32]))
        G.add_edge(nodes[index1 + 5], nodes[index1 + 14],
                   weight=ves(zakodirovannaya_posledovatelnost[index2], zakodirovannaya_posledovatelnost[index2 + 1],
                              zakodirovannaya_posledovatelnost[index2 + 2], gr1[33], gr1[34], gr1[35]))
        G.add_edge(nodes[index1 + 6], nodes[index1 + 11],
                   weight=ves(zakodirovannaya_posledovatelnost[index2], zakodirovannaya_posledovatelnost[index2 + 1],
                              zakodirovannaya_posledovatelnost[index2 + 2], gr1[36], gr1[37], gr1[38]))
        G.add_edge(nodes[index1 + 6], nodes[index1 + 15],
                   weight=ves(zakodirovannaya_posledovatelnost[index2], zakodirovannaya_posledovatelnost[index2 + 1],
                              zakodirovannaya_posledovatelnost[index2 + 2], gr1[39], gr1[40], gr1[41]))
        G.add_edge(nodes[index1 + 7], nodes[index1 + 11],
                   weight=ves(zakodirovannaya_posledovatelnost[index2], zakodirovannaya_posledovatelnost[index2 + 1],
                              zakodirovannaya_posledovatelnost[index2 + 2], gr1[42], gr1[43], gr1[44]))
        G.add_edge(nodes[index1 + 7], nodes[index1 + 15],
                   weight=ves(zakodirovannaya_posledovatelnost[index2], zakodirovannaya_posledovatelnost[index2 + 1],
                              zakodirovannaya_posledovatelnost[index2 + 2], gr1[45], gr1[46], gr1[47]))


    m_ = 0
    n_ = 0
    for i in range(len(bin1_result)):  # цикл для создания всех ребер графа.
        func3(m_, n_)
        m_ = m_ + 8
        n_ = n_ + 3

#pos = nx.spring_layout(G)
#nx.draw(G, pos, with_labels=True)
#labels = nx.get_edge_attributes(G, 'weight')
#nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

print(nx.dijkstra_path(G, nodes[0], nodes[-4]))
print(nx.dijkstra_path(G, nodes[0], nodes[-3]))
print(nx.dijkstra_path(G, nodes[0], nodes[-2]))
print(nx.dijkstra_path(G, nodes[0], nodes[-1]))


gr2 = []
min = 100
if (kolvo_summatorov==1):
    if (nx.dijkstra_path_length(G, nodes[0], nodes[-1]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-2])) :
        for i in range(1, len(bin1_result) + 1):
            gr2.append(nx.dijkstra_path(G, nodes[0], nodes[-1])[i][0])
        print("Изначальная последовательность: ", gr2)
    else:
        for i in range(1, len(bin1_result) + 1):
            gr2.append(nx.dijkstra_path(G, nodes[0], nodes[-2])[i][0])
        print("Изначальная последовательность: ", gr2)

elif (kolvo_summatorov==2):
    if (nx.dijkstra_path_length(G, nodes[0], nodes[-4]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-2])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-4]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-3])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-4]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-1])):
        for i in range(1, len(bin1_result) + 1):
            gr2.append(nx.dijkstra_path(G, nodes[0], nodes[-4])[i][0])
        print("Изначальная последовательность: ", gr2)
    elif (nx.dijkstra_path_length(G, nodes[0], nodes[-2]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-4])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-2]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-3])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-2]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-1])):
        for i in range(1, len(bin1_result) + 1):
            gr2.append(nx.dijkstra_path(G, nodes[0], nodes[-2])[i][0])
        print("Изначальная последовательность: ", gr2)
    elif (nx.dijkstra_path_length(G, nodes[0], nodes[-3]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-4])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-3]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-2])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-3]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-1])):
        for i in range(1, len(bin1_result) + 1):
            gr2.append(nx.dijkstra_path(G, nodes[0], nodes[-3])[i][0])
        print("Изначальная последовательность: ", gr2)
    elif (nx.dijkstra_path_length(G, nodes[0], nodes[-1]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-4])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-1]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-3])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-1]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-2])):
        for i in range(1, len(bin1_result) + 1):
            gr2.append(nx.dijkstra_path(G, nodes[0], nodes[-1])[i][0])
        print("Изначальная последовательность: ", gr2)
    else:
        print("Путей с весом ноль нет")
else:
    if (nx.dijkstra_path_length(G, nodes[0], nodes[-4]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-2])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-4]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-3])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-4]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-1])) and (nx.dijkstra_path_length(G, nodes[0], nodes[-4]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-7])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-4]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-5])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-4]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-6])):
        for i in range(1, len(bin1_result) + 1):
            gr2.append(nx.dijkstra_path(G, nodes[0], nodes[-4])[i][0])
        print("Изначальная последовательность: ", gr2)
    elif (nx.dijkstra_path_length(G, nodes[0], nodes[-2]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-4])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-2]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-3])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-2]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-1])) and (nx.dijkstra_path_length(G, nodes[0], nodes[-2]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-7])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-2]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-5])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-2]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-6])):
        for i in range(1, len(bin1_result) + 1):
            gr2.append(nx.dijkstra_path(G, nodes[0], nodes[-2])[i][0])
        print("Изначальная последовательность: ", gr2)
    elif (nx.dijkstra_path_length(G, nodes[0], nodes[-3]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-4])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-3]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-2])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-3]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-1])) and (nx.dijkstra_path_length(G, nodes[0], nodes[-3]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-7])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-3]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-5])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-3]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-6])):
        for i in range(1, len(bin1_result) + 1):
            gr2.append(nx.dijkstra_path(G, nodes[0], nodes[-3])[i][0])
        print("Изначальная последовательность: ", gr2)
    elif (nx.dijkstra_path_length(G, nodes[0], nodes[-1]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-4])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-1]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-3])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-1]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-2])) and (nx.dijkstra_path_length(G, nodes[0], nodes[-1]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-7])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-1]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-5])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-1]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-6])):
        for i in range(1, len(bin1_result) + 1):
            gr2.append(nx.dijkstra_path(G, nodes[0], nodes[-1])[i][0])
        print("Изначальная последовательность: ", gr2)
    elif (nx.dijkstra_path_length(G, nodes[0], nodes[-5]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-2])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-5]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-3])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-5]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-1])) and (nx.dijkstra_path_length(G, nodes[0], nodes[-5]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-7])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-5]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-4])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-5]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-6])):
        for i in range(1, len(bin1_result) + 1):
            gr2.append(nx.dijkstra_path(G, nodes[0], nodes[-5])[i][0])
        print("Изначальная последовательность: ", gr2)
    elif (nx.dijkstra_path_length(G, nodes[0], nodes[-6]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-4])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-6]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-3])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-6]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-1])) and (nx.dijkstra_path_length(G, nodes[0], nodes[-6]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-7])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-6]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-2])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-6]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-5])):
        for i in range(1, len(bin1_result) + 1):
            gr2.append(nx.dijkstra_path(G, nodes[0], nodes[-6])[i][0])
        print("Изначальная последовательность: ", gr2)
    elif (nx.dijkstra_path_length(G, nodes[0], nodes[-7]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-4])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-7]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-2])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-7]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-1])):
        for i in range(1, len(bin1_result) + 1):
            gr2.append(nx.dijkstra_path(G, nodes[0], nodes[-7])[i][0])
        print("Изначальная последовательность: ", gr2)
    elif (nx.dijkstra_path_length(G, nodes[0], nodes[-8]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-4])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-8]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-3])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-8]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-2])) and (nx.dijkstra_path_length(G, nodes[0], nodes[-8]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-7])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-8]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-1])) and (
            nx.dijkstra_path_length(G, nodes[0], nodes[-8]) <= nx.dijkstra_path_length(G, nodes[0], nodes[-5])):
        for i in range(1, len(bin1_result) + 1):
            gr2.append(nx.dijkstra_path(G, nodes[0], nodes[-8])[i][0])
        print("Изначальная последовательность: ", gr2)

# преобразуем последовательность в изначальную строку
# strOfStrings = ''.join(gr2)
for i in range(len(str_to_conv) - 1):
    gr2.insert(gr5[i], " ")
strOfStrings = ''.join(gr2)
print(strOfStrings)
revert = ''.join([chr(int(s, 2)) for s in strOfStrings.split()])  # из двоичной в обычную
print(revert)
