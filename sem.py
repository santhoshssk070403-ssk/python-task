year=int(input("Enter the year (1-3):"))
sem=int(input("Enter the semeter(1-6):"))
print("the year and semester")

if year==1:
   if sem==1:
       print("tam \n eng \n c \n ")
   elif sem==2:
       print("tam \n eng \n c++ \n")
   else:
           print( "the semester is invalid")
    
elif year == 2:
     if sem==3:
        print("aa \n bb\n ccc \n ")
     elif sem==4:
       print("dd \n ee \n ff \n")
     else:
        print( "the semester is invalid")
    
elif year==3:
    if sem==5:
        print("gg \n hh \n ii \n ")
    elif sem==6:
        print("jj\n kk \n ll \n")
    else:
        print( "the semester is invalid")

else:
       print("the year is invalid")
