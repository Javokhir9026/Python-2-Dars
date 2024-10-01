import os; os.system("cls")

i = 1; son = 10

while( i <= 10):     # 1 dan 10 gacha
    print(i)
    i+=1
while(son >= 1):       # 10 dan 1 gacha
    print(son, end = " ")
    son-=1

s =int(input("\nSON: "))
j = 1
while(j <= s):           # 1 dan son gacha
    if(j % 8 == 0):       # agar j 8 ga bolinsa
        print(s, end = " ")
    j+=1
