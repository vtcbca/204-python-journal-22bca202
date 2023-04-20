#write a script to enter any sentence and print those word which is palindrome also print total number of palindrome word.
def palicount(a):
    x=x.split(" ")
    z=0
    y=[]
    for i in y:
        if (i==i[::-1]):
            z=z+1
            y.append(i)
    if z>0:
        print(f'The number of palindrome word in sentence is {z} and palindrome words are:{y}.')
    else:
        print("There is no palindrome word in sentence!!!")    
x=input("enter a sentece:")
palicount(x)