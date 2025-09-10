random_shit = [1,31,21,554,4,16,25,28,146,798,"Ананас","Яблуко","Огірок","Виноград","Кавун","Груша","Гарбуз","Диня","Слива","Капуста"]
a=[]
b=[]
sort_numbers=[]
caps_words=[]

for i in random_shit:
    if type(i)==int:
        a.append(i)
    elif type(i)==str:
        b.append(i)
a.sort(), b.sort()
sortik = a+b

for i in a:
    if i%2==0:
        sort_numbers.append(i)
for i in b:
    caps_words.append(i.upper())

print(random_shit)
print(sortik)
print(sort_numbers)
print(caps_words)
