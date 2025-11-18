students = {}

while True:
    name = str(input("Enter name: "))
    if name == "stop" or name == "":
        break
    try:
        mark = int(input("Enter marks: "))
    except ValueError:
        print("Enter a number")
        continue
    if name not in students:
        students[name] = mark

mid_mark = []
for popa in students.values():
    mid_mark.append(popa)
average_mark = sum(mid_mark) / len(mid_mark)

nerds = {}
good_gay = {}
autistic_gay = {}
gay = {}

for name, mark in students.items():
    if 12 <= mark >= 10:
        nerds[name] = mark
    elif 9 <= mark >= 7:
        good_gay[name] = mark
    elif 6 <= mark >= 4:
        autistic_gay[name] = mark
    elif 3 <= mark >= 1:
        gay[name] = mark
if nerds:
    print("Відмінники",len(nerds),":")
    for name, mark in nerds.items():
        print(f"{name}: {mark}")
if good_gay:
    print("Хорошисти",len(good_gay),":")
    for name, mark in good_gay.items():
        print(f"{name}: {mark}")
if autistic_gay:
    print("Піде",len(autistic_gay),":")
    for name, mark in autistic_gay.items():
        print(f"{name}: {mark}")
if gay:
    print("Не здав",len(gay),":")
    for name, mark in gay.items():
        print(f"{name}: {mark}")
print("Сер.значення групи",":",average_mark)
