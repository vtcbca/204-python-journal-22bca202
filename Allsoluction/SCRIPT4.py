#write a listb of menudriven 
x=[]
y="a"
while y=="a" or y=="A":

  print("\n1.Add iteams in list.\n2.print string with even character in length.\n3.Replace odd character of string with index no.\n4.enter start and end value and extraxt character from the string\n")
  c=int(input("Enter your choice!!"))

  match z:
    case 1:
          x1="a"
          while x1=="a" or x1=="A":
            i=input("Enter a string you want to enter:")
            x.append(i)
            a1=input("do you add more string press (a/A):")
               
    case 2:
          p=[]
          count=0
          for i in x:
            if(len(i)%2==0):
              p.append(i)
              count+=1
          if count>0:    
            print(f"Strings with even character is {x}")
          else:  
            print("String has no even charcater in it.....")     
 # case 3:

    case 4:
          s=int(input("Enter start index:"))
          e=int(input("Enter end index:"))
          res=" ".join([sub for sub in x])[s:e]
          print(f"Your string is {res}")          

  y=input("Do youy want to continue:(a/A):")