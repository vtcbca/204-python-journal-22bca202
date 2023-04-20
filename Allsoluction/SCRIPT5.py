def symmetric(k):
    half=(len(k)//2)
    first=n[:half]
    second=n[half:]
    if first==second:
        print(f"String {k} is symmetric!!!!")
    else:
        print(f"String {k} is not symmetric!!!")

def input1():
     x=input("Enter a string:")
     symmetric(x)
     
input1()     