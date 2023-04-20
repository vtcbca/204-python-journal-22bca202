#python script to check string is palindrome or not
x=input("Enter any string :")
y=x[::-1]
if(x==y):
    print("String is palindrome !")
else:
    print("String is not palindrome !")
