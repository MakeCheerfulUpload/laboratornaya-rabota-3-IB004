import re
print("Variant: " + str(367118%6) + ' ' + str(367118%4) + ' ' + str(367118%7))
tests = ["X-{|",
         "X-{|X-{|",
         "X-{|     X-{|",
         "X{-| -{|X {|X-",
         "123X-{|123"
         ]
for test in tests:
    match = re.findall(r"X-\{\|", test)
    print(len(match))

