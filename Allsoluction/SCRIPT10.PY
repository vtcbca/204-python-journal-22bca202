def consecutivecoomon(x):
    count=0
    y=[]
    for i in range(len(x)-2):
        if x[i]==x[i+1] and x[i+1]==x[i+2]:
            b.append(x[i])
            count+=1
    if count>0:
        print(f"Consecutive common number in list {x} as follow:{y}")
    else:
        printf("No consecutive number in list!!")
def takeinput():
    c=[]
    y=int(input("How many number you want to enter in list:"))
    for i in range(y):
        c=int(input("Enter value:"))
        a.append(c)
    consecutivecoomon(a)        

takeinput()    