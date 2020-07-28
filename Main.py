print("HI!\n") 

from Parse import Parse

j = input("Enter 'a' for Yahoo and 'b' for rediffmoney : ")
if (j=='a'):
    i = str(input("enter the link for the stock : "))
    Parse(i, 0)
else:
    i = str(input("enter the link for the stock : "))
    Parse(i, 1)
