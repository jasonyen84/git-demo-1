import random

times = 0

x = random.randint(1, 50)
print(x)
for i in range(5):
    y = int(input("請猜一數字:"))
    if y == x:
        print("猜對了!")
        print(f"猜了{times}次")
        break
    else:
        if x > y:
            print("猜高一點")
            times += 1
        else:
            print("猜低一點")
            times += 1

if x != y:
    print(f"答案為:{x}")
