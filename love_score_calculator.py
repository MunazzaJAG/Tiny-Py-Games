love score calculator
def calculate_love_score(name1, name2):
    names=[name1, name2]
    tcount,lcount=0,0
    for i in names:
        i.lower()
        for j in "true":
            if j in i:
                tcount+=i.count(j)
        for k in "love":
            if k in i:
                lcount+=i.count(k)      
    print(f"{tcount}{lcount}")

name1=input("name1: ")
name2=input("name2: ")
names=[name1, name2]
calculate_love_score(names)