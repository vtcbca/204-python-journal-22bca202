
def changename(a):
    filechange=[]
    p=".c"
    for i in a:
        if p in i: 
            b=i.replace(".c",".py")
            filechange.append(b)
        else:
            filechange.append(i)    

    print(filechange)    

filesname = ["program.c","stdio.c","sample.c","a.py","math.py","hpp.py"]
changename(filesname)