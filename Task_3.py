import re

print("Variant: " + str(367118%5))
tests = [["Петров П.П. P0000", "Анищенко А.А. P33113", "Примеров Е.В. P0000", "Иванов И.И. P0000"],
         ["Петров П.П. P0000", "Анищенко А.А. P33113", "Примеров Е.Е. P0000", "Иванов И.И. P0000"],
         ["Петров П.П. P0000", "Анищенко А.А. P0000", "Примеров Е.Е. P0000", "Сидоров И.И. P0000"],
         ["Петров-Сидоров П.П. P0000", "Анищенко-Каменьщиков А.А. P0000", "Примеров Е.Е. P0000", "Сидоров И.И. P0000"],
         ["Петров П.П. P0000", "Анищенко А.А. P33113", "Примеров Е.В. P0000", "Иванов И.И. P0000"]]

for test in tests:
    print(test)
    removeId = []
    for person in test:
        match = re.findall(r"\w+(?:-\w+)*\s+(\w\.)(\w\.)\sP0000", person)
        if len(match)>0:
            print(match)
        if len(match) > 0 and (match[0][0] == match[0][1]):
            removeId.append(person)
    if len(removeId)>0:
        for person in removeId:
            test.remove(person)

    print(test)
    print()

