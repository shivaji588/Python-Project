s1=int(input("Enter sub 1 marks :"))
s2=int(input("Enter sub 2 marks :"))
s3=int(input("Enter sub 3 marks :"))
total=s1+s2+s3
avg=total/3
print("Total Marks :",total)
print("Average :",avg) 
if avg >=85 :
    print("Result :Distinction")
elif avg >=65 :
    print("Reault:first class")    
elif avg >=45 :
    print("Result :Pass Only")
else:
    print("failllllllllllllllllllllllll")