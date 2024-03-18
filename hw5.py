import random

pravda = ["Скільки тобі років", "Який твій секрет", "Де ти живеш"]
dia = ["присядь 10 разів", "пострибай 20 разів", "не ворушися 10 секунд"]



def pravdaabodia():
    q = input("Введи правду або дію - ")
    if q.lower() == "правда" or q.lower() == "п":
        p = random.choice(pravda)
        l = (random.randint(1, y))
        print(l, "-ий", p)
    elif q.lower() == "дія" or q.lower() == "д":
        d = random.choice(dia)
        m = (random.randint(1, y))
        print(m, "-ий", d)
    p = input("Грати ще? ")
    if p.lower() == "так" or p.lower() == "т":
        pravdaabodia()
    elif p.lower() == "ні" or p.lower() == "н":
        print("бувай")


j = input("Почати гру? ")
if j.lower() == "так" or j.lower() == "т":
    y = int(input("Кількість людей - " ))
    pravdaabodia()
elif j.lower() == "ні" or j.lower() == "н":
    print("Бувай")