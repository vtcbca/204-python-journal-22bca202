#write a script to create a list with 5 string and count total number of length with string using UDF.
def evenstr(x):
    s=[]
    count=0
    for i in a:
        if(len(i)%2==0):
            s.append(i)
            count=count+1
    if(count>0):
        print(f'The number of even string is {count} and string :{x}')
    else:
        print("No even string available!")

a=[]
for i in range(5):
    y=input(f"Enter string:{i+1}:")
    x.append(y)
evenstr(x)