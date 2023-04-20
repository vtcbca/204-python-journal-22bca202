def makedict(n):
    dic={}
    a=int(input("Enter minimum word of length:"))
    for i in n:
        if len(i)>=a:
            dic[i]=len(i)

    print(dic)

def input():
    str=input("Enter a sentence:")
    x=str.split(" ")
    makedict(x)

input()