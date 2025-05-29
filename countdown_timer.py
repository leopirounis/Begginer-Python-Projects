import time

my_time = int(input("Enter time in seconds: "))

for x in range(my_time,0,-1):
    seconds = x % 60 #modulo 60
    minutes = int(x / 60) % 60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}") #02 gia dio psifia
    time.sleep(1) # 1 second gia kathe x
print("Time's up!")