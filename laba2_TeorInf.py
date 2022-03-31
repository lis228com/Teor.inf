import networkx as nx
import matplotlib.pyplot as plt
#Первый абзац - ввод информации


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

gr5 = []
for i in range(len(bin_result)):
    if bin_result[i]==" ":
        gr5.append(i)
print("gr5",gr5)



kolvo_summatorov = int(input("Введите число сумматоров: "))
if (kolvo_summatorov == 1):
    a = input("Введите регистры для первого сумматора: ")
    a = a.split(",")
    a = list(a)
    for i in range(len(a)):
        a[i] = int(a[i])
    print(a)#убедившись в правильности, принты можно убрать. Чисто для проверки

    #Теперь пишем алгоритм для сумматора. Если сумматоров>1, то сделать функцию.
    for i in range(len(bin2_result)):
        gr.insert(0,bin2_result[i])
        c = gr[a[0]-1]
        d = gr[a[1]-1]
        e = c+d
        if (e%2==0):
            e=0
        else:
            e=1
        zakodirovannaya_posledovatelnost.append(e)
        zakodirovannaya_posledovatelnost.append(e1)
        i = i+1
    print(zakodirovannaya_posledovatelnost)
    zakodirovannaya_posledovatelnost1 = ''.join(str(n) for n in zakodirovannaya_posledovatelnost)
    print("Получили закодированную строку: ",zakodirovannaya_posledovatelnost1)
    
elif (kolvo_summatorov == 2):
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
    for i in range(len(bin2_result)):
        gr.insert(0,bin2_result[i])
        c = gr[a[0]-1]
        d = gr[a[1]-1]
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

elif (kolvo_summatorov ==3):
    a = input("Введите регистры для первого сумматора: ")
    b = input("Введите регистры для второго сумматора: ")
    z = input("Введите регистры для третьего сумматора: ")
    a = a.split(",")
    b = b.split(",")
    z = z.split(",")
    a = list(a)
    b = list(b)
    z = list(z)
    for i in range(len(a)):
        a[i] = int(a[i])
    for i in range(len(b)):
        b[i] = int(b[i])
    for i in range (len(z)):
        z[i] = int(z[i])
    print(a)
    print(b)
    print(z)
    for i in range(len(bin2_result)):
        gr.insert(0,bin2_result[i])
        c = gr[a[0]-1]
        d = gr[a[1]-1]
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
        #третий
        c2_ = gr[z[0]-1]
        d2_ = gr[z[1]-1]
        e2_ = c2_+d2_
        if (e2_%2==0):
            e2_=0
        else:
            e2_=1
        zakodirovannaya_posledovatelnost.append(e)
        zakodirovannaya_posledovatelnost.append(e1)
        zakodirovannaya_posledovatelnost.append(e2_)
        i = i+1
    print(zakodirovannaya_posledovatelnost)
    zakodirovannaya_posledovatelnost1 = ''.join(str(n) for n in zakodirovannaya_posledovatelnost)
    print("Получили закодированную строку: ",zakodirovannaya_posledovatelnost1)

else:
    print("Введено неверное значение")


#кодирование ЗАВЕРШЕНО
#Теперь декодируем
#Сделаем функцию (это цифры над линиями в Витерби)
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
#func1(1,1,1)#строка нужна, чтобы в графе не возникало ошибки list index out of range
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
nodes = []
for i in range(len(bin1_result)+1):#цикл для создания узлов графа
    u = "00"
    u_ = "10"
    u__ = "01"
    u___ = "11"
    p = str(i)
    nodes.append(u + p)
    nodes.append(u_ + p)
    nodes.append(u__ + p)
    nodes.append(u___ + p)
print("Список узлов",nodes)

#nodes = ["00(0)", "00(1)", "10(1)", "00(2)", "10(2)","01(2)","11(2)","00(3)","10(3)","01(3)","11(3)"]#узлы зададим точками на диаграмме Витерби. Опять же, вопрос в динамическом образовании этих точек
G.add_nodes_from(nodes)

def func3(index1,index2):#функция для постройки графа
    G.add_edge(nodes[index1], nodes[index1+4], weight=ves(zakodirovannaya_posledovatelnost[index2],zakodirovannaya_posledovatelnost[index2+1],gr1[0],gr1[1]))
    G.add_edge(nodes[index1], nodes[index1+5], weight=ves(zakodirovannaya_posledovatelnost[index2],zakodirovannaya_posledovatelnost[index2+1],gr1[2],gr1[3]))
    G.add_edge(nodes[index1+1], nodes[index1+6], weight=ves(zakodirovannaya_posledovatelnost[index2],zakodirovannaya_posledovatelnost[index2+1],gr1[4],gr1[5]))
    G.add_edge(nodes[index1+1], nodes[index1+7], weight=ves(zakodirovannaya_posledovatelnost[index2],zakodirovannaya_posledovatelnost[index2+1],gr1[6],gr1[7]))
    G.add_edge(nodes[index1+2], nodes[index1+4], weight=ves(zakodirovannaya_posledovatelnost[index2],zakodirovannaya_posledovatelnost[index2+1],gr1[8],gr1[9]))
    G.add_edge(nodes[index1+2], nodes[index1+5], weight=ves(zakodirovannaya_posledovatelnost[index2],zakodirovannaya_posledovatelnost[index2+1],gr1[10],gr1[11]))
    G.add_edge(nodes[index1+3], nodes[index1+6], weight=ves(zakodirovannaya_posledovatelnost[index2],zakodirovannaya_posledovatelnost[index2+1],gr1[12],gr1[13]))
    G.add_edge(nodes[index1+3], nodes[index1+7], weight=ves(zakodirovannaya_posledovatelnost[index2],zakodirovannaya_posledovatelnost[index2+1],gr1[14],gr1[15]))

m_=0
n_=0
for i in range(len(bin1_result)):#цикл для создания всех ребер графа.
        func3(m_,n_)
        m_=m_+4
        n_=n_+2
#func3(0,0)
#func3(4,2)
#func3(8,4)
#func3(12,6)
#func3(16,8)
#func3(20,10)
#func3(24,12)


pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)


gr2 = []
min=100
if (nx.dijkstra_path_length(G,"000",nodes[-4]) < nx.dijkstra_path_length(G,"000",nodes[-2])) and (nx.dijkstra_path_length(G,"000",nodes[-4]) < nx.dijkstra_path_length(G,"000",nodes[-3])) and (nx.dijkstra_path_length(G,"000",nodes[-4]) < nx.dijkstra_path_length(G,"000",nodes[-1])) :
    print(nx.dijkstra_path(G,"000",nodes[-4]))
    for i in range(1,len(bin1_result)+1):
        gr2.append(nx.dijkstra_path(G,"000",nodes[-4])[i][0])
    print("Изначальная последовательность: ",gr2)
elif (nx.dijkstra_path_length(G,"000",nodes[-2]) < nx.dijkstra_path_length(G,"000",nodes[-4])) and (nx.dijkstra_path_length(G,"000",nodes[-2]) < nx.dijkstra_path_length(G,"000",nodes[-3])) and (nx.dijkstra_path_length(G,"000",nodes[-2]) < nx.dijkstra_path_length(G,"000",nodes[-1])):
    print(nx.dijkstra_path(G,"000",nodes[-2]))
    for i in range(1,len(bin1_result)+1):
        gr2.append(nx.dijkstra_path(G,"000",nodes[-2])[i][0])
    print("Изначальная последовательность: ",gr2)
elif (nx.dijkstra_path_length(G,"000",nodes[-3]) < nx.dijkstra_path_length(G,"000",nodes[-4])) and (nx.dijkstra_path_length(G,"000",nodes[-3]) < nx.dijkstra_path_length(G,"000",nodes[-2])) and (nx.dijkstra_path_length(G,"000",nodes[-3]) < nx.dijkstra_path_length(G,"000",nodes[-1])):
    print(nx.dijkstra_path(G,"000",nodes[-3]))
    for i in range(1,len(bin1_result)+1):
        gr2.append(nx.dijkstra_path(G,"000",nodes[-3])[i][0])
    print("Изначальная последовательность: ",gr2)
elif (nx.dijkstra_path_length(G,"000",nodes[-1]) < nx.dijkstra_path_length(G,"000",nodes[-4])) and (nx.dijkstra_path_length(G,"000",nodes[-1]) < nx.dijkstra_path_length(G,"000",nodes[-3])) and (nx.dijkstra_path_length(G,"000",nodes[-1]) < nx.dijkstra_path_length(G,"000",nodes[-2])):
    print(nx.dijkstra_path(G,"000",nodes[-1]))
    for i in range(1,len(bin1_result)+1):
        gr2.append(nx.dijkstra_path(G,"000",nodes[-1])[i][0])
    print("Изначальная последовательность: ",gr2)
else:
    print("Путей с весом ноль нет")

plt.show()




#преобразуем последовательность в изначальную строку
#strOfStrings = ''.join(gr2)
for i in range(len(str_to_conv)-1):
    gr2.insert(gr5[i]," ")
strOfStrings = ''.join(gr2)
print(strOfStrings)
revert = ''.join([chr(int(s, 2)) for s in strOfStrings.split()])#из двоичной в обычную
print(revert)












   













   












   








   
















   














   














   














   















   
















   

   

   

