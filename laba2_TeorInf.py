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
for i in range(kolvo_summatorov):
    spisok.append([int(z) for z in input("Введите регистры для n-го сумматора: ").split()])
print("spisok = ",spisok)

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
kod=[]
for i in range(len(zakodirovannaya_posledovatelnost)):
    kod.append(zakodirovannaya_posledovatelnost[i])
zakodirovannaya_posledovatelnost1 = ''.join(str(n) for n in zakodirovannaya_posledovatelnost)
print("Получили закодированную строку: ", zakodirovannaya_posledovatelnost1)
# кодирование ЗАВЕРШЕНО
# Теперь декодируем
# Сделаем функцию (это цифры над линиями в Витерби)


res=[]
for i in range(2**kolvo_summatorov):
    s=''
    for j in range(kolvo_summatorov):
        s=str(i%2)+s
        i=i//2
    res.append(s)
print("res = ",res)

gruppa=[]
for i in range(len(res)):
    for j in range(kolvo_summatorov):
        gruppa.append(int(res[i][j]))
print("gruppa = ",gruppa)#целочисленные значения битовой последовательности типа 00,01,10,11
    


gr1 = []
gruppa1=[]#исправить при большом кол-ве регистров

for x in range(len(res)):
    for i in range(kolvo_summatorov):
        gruppa1.append(gruppa[i])
        
    for j in range(2):
        gruppa1.insert(0,j)
        for i in range(2):
            m=gruppa1[spisok[i][0]-1]
            n=gruppa1[spisok[i][1]-1]
            k=(m+n)%2
            gr1.append(k)
        gruppa1.pop(0)
    gruppa1=[]
    for y in range(kolvo_summatorov):
        gruppa.pop(0)
    
print("gr1(числа над линиями витерби)= ",gr1)

                 
#пишем код для расчета веса хэминга
zakod_posl=[]
sum=0
gr2=[]
for i in range(len(zakodirovannaya_posledovatelnost) // kolvo_summatorov):
    #print(zakodirovannaya_posledovatelnost)
    for z in range(kolvo_summatorov):
        zakod_posl.append(zakodirovannaya_posledovatelnost[0])
        zakodirovannaya_posledovatelnost.pop(0)
    #print(zakod_posl)
    for j in range(len(gr1)):
        for x in range(kolvo_summatorov):
            if (gr1[x] != zakod_posl[x]):
                sum=sum+1
            else:
                sum=sum
            x=x+1
        gr2.append(sum)
        for p in range(kolvo_summatorov):
            gr1.append(gr1.pop(0))
        sum=0
        x=0
    for q in range(kolvo_summatorov):
        zakod_posl.pop(0)
        
                                            
        
#print("gr2(вес хэминга)=",gr2)#почему-то выводит в 2 раза больше чисел, чем нужно
gr4=[]
for i in range(len(kod) // kolvo_summatorov):
    for j in range(len(gr1) // kolvo_summatorov):
        gr4.append(gr2[0])
        gr2.pop(0)
    for k in range(len(gr1) // kolvo_summatorov):
        gr2.pop(0)
    
print("Вес хэминга = ",gr4)



# строим граф. Его вес рассчитали зараннее (gr4)
#сначала создадим узлы графа, затем ребра
G = nx.DiGraph()
nodes = []
#nodes_=[]
for i in range(len(nodes)):
    nodes_.append(nodes[i])
    

for i in range(len(kod) // kolvo_summatorov + 1):
    for j in range(len(res)):
        nodes.append(res[j]+"("+str(i)+")")
print("Узлы = ",nodes)

#for i in range(len(nodes)):
#    nodes_.append(nodes[i])# доп.список для узлов

#G.add_nodes_from(nodes)


for k in range(len(kod) // kolvo_summatorov  ):
    for j in range(2):
        i=0#???
        G.add_edge(nodes[j] , nodes[i+len(res)] , weight = gr4[0])
        #print(nodes[j] + " " + nodes[i+len(res)])
        G.add_edge(nodes[j] , nodes[i+len(res)+len(res)//2] , weight = gr4[1])
        #print(nodes[j] + " " + nodes[i+len(res)+len(res)//2])
        gr4.pop(0)
        gr4.pop(0)
        #j=j+1
    nodes.pop(0)
    for j in range(2):
        G.add_edge(nodes[j+1] , nodes[i+len(res)] , weight = gr4[0])
        #print(nodes[j+1] + " " + nodes[i+len(res)])
        G.add_edge(nodes[j+1] , nodes[i+len(res)+len(res)//2] , weight = gr4[1])
        #print(nodes[j+1] + " " + nodes[i+len(res)+len(res)//2])
        gr4.pop(0)
        gr4.pop(0)
    nodes.pop(0)
    nodes.pop(0)
    nodes.pop(0)
nodes.pop(0)
nodes.pop(0)
nodes.pop(0)
nodes.pop(0)



for i in range(len(kod) // kolvo_summatorov + 1):
    for j in range(len(res)):
        nodes.append(res[j]+"("+str(i)+")")
G.add_nodes_from(nodes)




print(nx.dijkstra_path(G, nodes[0], nodes[-1]))
print(nx.dijkstra_path_length(G, nodes[0], nodes[-1]))
print(nx.dijkstra_path(G, nodes[0], nodes[-2]))
print(nx.dijkstra_path_length(G, nodes[0], nodes[-2]))
print(nx.dijkstra_path(G, nodes[0], nodes[-3]))
print(nx.dijkstra_path_length(G, nodes[0], nodes[-3]))
print(nx.dijkstra_path(G, nodes[0], nodes[-4]))
print(nx.dijkstra_path_length(G, nodes[0], nodes[-4]))

i=1
min=100
for i in range(len(res)+1):
    if (nx.dijkstra_path_length(G, nodes[0], nodes[-1*i])<=min):
        min=nx.dijkstra_path_length(G, nodes[0], nodes[-1*i])
        aa=nx.dijkstra_path(G, nodes[0], nodes[-1*i])
    i=i+1
print(aa)

        

# преобразуем последовательность в изначальную строку
# strOfStrings = ''.join(gr2)
for i in range(len(str_to_conv) - 1):
    gr2.insert(gr5[i], " ")
strOfStrings = ''.join(gr2)
print(strOfStrings)
revert = ''.join([chr(int(s, 2)) for s in strOfStrings.split()])  # из двоичной в обычную
print(revert)
















            


