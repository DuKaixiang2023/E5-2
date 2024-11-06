//一个时钟函数

import time

minutes = int(input("Enter time"))
total_seconds = minutes * 60

while total_seconds:
    mins, secs = divmod(total_seconds, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    time.sleep(1)
    total_seconds -= 1
print("Focus timer complete!")


//2024.11.06
//18.57
