import time
x=int(input("enter no of seconds"))
for i in range(x, 0, -1):
     seconds=i%60
     minutes=int(i/60)%60
     hours=int(i/3600)
     print(f"{hours:02}:{minutes:02}:{seconds:02}")

print("time is up")     
     
