a=0
b=0
for i in range (15):
    print ("Введите число")
    c=int (input())
    if c>0:
        a=a+c
    else:
        b=b+c
print("Сумма положительных чисел составляет"+ str(a))
print("Сумма отрицательных чисел составляет"+ str(b))