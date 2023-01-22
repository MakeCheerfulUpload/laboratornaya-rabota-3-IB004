#+(1-3 symb)
import re

tests = ["+7(980)391-13-90",
         "+273 (980) 391-13-90",
         "+7(20)391-13-90",
         "+7(220)391-1-90",
         "8(980)391-13-90",
         ]
for test in tests:
    test = re.sub(r"\s", "", test)
    print(test)
    match = re.match(r'\+?\d{1,3}\(\d{3}\)\d{3}\-\d{2}\-\d{2}', test)
    if match == None:
        print("OH NO!")
    else:
        print(match.group())

