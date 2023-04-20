def evenodd(a):
    even,odd=[],[]
    count1,count2=0,0
    for i in a:
        if i%2==0:
            even.append(i)
            count1+=1
        else:
            odd.append(i)
            count2+=1
    
    print(f"The even numbers are {count1} and numbers:")
    printlist(even)
    
    print(f"The odd numbers are {count2} and numbers:")
    printlist(odd)


def printlist(x):
    for i in x:
        print(i)

def createlist():
    a=[]
    b=int(input("How many numbers you want to enter in list:"))
    for i in range(x):
        y=int(input("Enter a number:"))
        a.append(y)
    evenodd(a)

createlist()