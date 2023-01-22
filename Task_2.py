import re

print("Variant: " + str(367118 % 6))
tests = ["А ты знал, что ВТ – лучшая кафедра в ИТМО?",
         "ВТ      ВТ  ИТМО    ИТМО",
         "ВТ, КТ, ИС – поступай в ИТМО!",
         "шёл на ВТ, а попал в ИТМО",
         "почему на ВТ не учат делать ТВ в ИТМО?",
         "ВТ и а к ИТМОушен",
         "ВТорник оааирллг увкд ИТМО"
         ]
for test in tests:
    test = re.sub(r"[.,–?!]", " ", test)
    test = re.sub(r"\s+", " ", test)
    #print(test)

    L = []
    s = 0
    for i in range(1, len(test)):
        s += 1
        if test[i - 1] + test[i] == "ВТ":
            L.append(s - 1)
    #print(L)

    for i in range(5):
        pattern = "ВТ\s(?:\w+\s){" + str(i) + "}ИТМО(?:\s+|" + r"\b)"
        print(pattern)
        for l in L:
            print(test[l:])
            match = re.findall(pattern, test[l:])
            if len(match) > 0:
                print(match)
        print()
    print()
    print("***")
    print()