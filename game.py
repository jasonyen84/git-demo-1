import random

right = True

x = random.randint(1, 50)
print(x)
for i in range(5):
    y = int(input("請猜一數字:"))
    if y == x:
        print("猜對了!")
        break
    else:
        print("猜錯了")
