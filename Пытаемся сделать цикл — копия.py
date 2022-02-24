import sys
#функция 1 (расширенный алгоритм Евклида)
def func1(aaaa, b):
    schetchik = 0
    y0=0
    y1=1
    q = b//aaaa
    print("q=",q)
    z = b%aaaa #ostatok ot deleniya
    print("z=",z)
    y2 = y0 - q*y1
    h = (b-z) / q
    print("h=",h)

    if (z==1):
        y = y2
        schetchik = schetchik + 1
    else:
        q = h//z
        print("q=",q)
        z = h%z
        print("z=",z)
        y3 = y1 - q*y2
        h = (h-z)/q
        print("h=",h)

    if(z == 1) and (schetchik == 0):
        y = y3
        schetchik = schetchik + 1
    elif (z == 1) and (schetchik == 1):
        print("f")
    else:
        q = h//z
        print("q=",q)
        z = h%z
        print("z=",z)
        y4 = y2-q*y3
        h = (h-z)/q
        print("h=",h)

    if(z==1) and (schetchik == 0):
        y = y4
        schetchik = schetchik + 1
    elif (z == 1) and (schetchik == 1):
        print("f")
    else:
        q = h//z
        print("q=",q)
        z = h%z
        print("z=",z)
        y5 = y3-q*y4
        h = (h-z)/q
        print("h=",h)

    if(z==1) and (schetchik == 0):
        y = y5
        schetchik = schetchik + 1
    elif (z == 1) and (schetchik == 1):
        print("f")
    else:
        q = h//z
        print("q=",q)
        z = h%z
        print("z=",z)
        y6 = y4-q*y5
        h = (h-z)/q
        print("h=",h)
    if(z==1) and (schetchik == 0):
        y = y6
    elif (z == 1) and (schetchik == 1):
        print("f")
    else:
        q = h//z
        print("q=",q)
        z = h%z
        print("z=",z)
        y7 = y5-q*y6
        h = (h-z)/q
        print("h=",h)
    if(y<0):
        y=b+y
    else:
        y=y
    y = int(y)
    return str(y)
    

def func2(yuh):#на вход поступает только строка
    u = 0
    stroka = ''
    new_stroka = ''
    for i in range (len(yuh)):
        if (yuh[i]=='*') and (yuh[i+1]=='-'):#ищем число с минус первой степенью
            u = u+1
            if (yuh[i-3]=='1') or (yuh[i-3]=='2') or (yuh[i-3]=='3') or (yuh[i-3]=='4') or (yuh[i-3]=='5') or (yuh[i-3]=='6') or (yuh[i-3]=='7') or (yuh[i-3]=='8') or (yuh[i-3]=='9'):
                bb = yuh[i-3]
                aa = yuh[i-2]
                aaa = bb+aa
                e = yuh.index(yuh[i+2])
                f = yuh.index(yuh[i-2])
                r = yuh[:f-1]
                print("r=",r)
                rr = yuh[e+1:]
                print("rr=",rr)
                aaaa = int(aaa)
                r_ = func1(aaaa, b)
                print("r_ = ",r_)
                stroka = r + r_ + rr
                break
               
            
            else:
                aa = yuh[i-2]
                aaa = aa
                e = yuh.index(yuh[i+2])
                f = yuh.index(yuh[i-3])
                r = yuh[:f-1]#первый срез
                print("r=",r)
                rr = yuh[e+1:]#второй срез
                print("rr=",rr)
                aaaa = int(aaa)
                r_ = func1(aaaa,b)
                print("r_ = ",r_)
                stroka = r + r_ + rr
                break
        else:
            print("e")
    if(u==0):
        new_stroka = yuh
    else:
        new_stroka = stroka
    return new_stroka



def func3(bbb):
    new3_stroka = ''
    scetchik1 = 0
    srez = ''
    for i in range (len(bbb)):
        if(bbb[i] == '/'):
            scetchik1 = scetchik1 + 1
            ee= bbb.index(bbb[i])
            t = bbb[i+1]
            if (bbb[i+2] == "1") or (bbb[i+2] == "2") or (bbb[i+2] == "3") or (bbb[i+2] == "4") or (bbb[i+2] == "5") or (bbb[i+2] == "6") or (bbb[i+2] == "7") or (bbb[i+2] == "8") or (bbb[i+2] == "9"):
                tt = bbb[i+2]
                simvol_1 = t+tt #находим число в минус первой степени для дальнейшего вычисления (при условии, что оно может состоять либо из одной, либо из двух цифр)
                srez1 = bbb[:ee]
                print("srez1=",srez1)
                srez2 = bbb[ee+3:]
                print("srez2=",srez2)
                srez = srez1 + '*' + func1(int(simvol_1),b) + srez2
                break
            else:
                simvol_1 = t
                chislo = bbb[i+1]
                srez1 = bbb[:ee]
                print("srez1=",srez1)
                srez2 = bbb[ee+2:]
                print("srez2=",srez2)
                func1(simvol_1,b)
                srez = srez1 + '*' + func1(int(simvol_1),b) + srez2
                break
        else:
            print("r")
    if(scetchik1==0):
        new3_stroka = bbb
    else:
        new3_stroka = srez
    return new3_stroka


#Основная программа
new1_stroka = ''
compiled_str = ''
k=0
uu = 0
u = 0
a=input("Введите строку: ") #ввод строки
b = int(input('Введите значение поля: '))#обозначаем за a и b для последующего уравнения вида: ax+by=1
for o in range(2, b // 2+1):# Проверка числа на простоту
    if (b % o == 0):
        k = k+1
if (k <= 0):
    for j in range(3):
        new1_stroka = func2(a)
        a = new1_stroka
else:
    sys.exit()
   
print(new1_stroka)

for v in range(3):
    novaya_stroka = func3(new1_stroka)
    new1_stroka = novaya_stroka
print(novaya_stroka)





#выходим на финишную прямую. Осталось перевести строку в числовой вид и вычислить
compiled_str = compile(novaya_stroka, 'string', 'eval')
c = eval(compiled_str)
if (float(c) < float(b)) and (float(c)>0):
    Otvet = float(c)
elif (float(c)<0):
    Otvet = float(c)%float(b)
else:
    Otvet = float(c) % float(b)
print("Otvet = ",Otvet)


