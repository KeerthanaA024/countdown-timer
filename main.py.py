'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import time
seconds=int(input("enter time in seconds:"))
while seconds>0:
    mins=seconds//60
    secs=seconds%60
    timer=f" {mins:02d}:{secs:02d} "
    print(timer,end="\r")
    time.sleep(1)
    seconds-=1
print("time up!")    